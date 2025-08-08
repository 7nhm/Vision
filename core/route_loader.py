import json
import importlib
from flask import Blueprint

class RouteLoader:
    """Class để load và đăng ký routes từ JSON config"""
    
    def __init__(self, app=None):
        self.app = app
        self.blueprints = {}
        
    def load_routes_from_json(self, config_path='config/routes.json'):
        """Load routes từ JSON file"""
        with open(config_path, 'r', encoding='utf-8') as f:
            routes_config = json.load(f)
        
        return routes_config
    
    def create_blueprints(self, routes_config):
        """Tạo blueprints từ config"""
        for blueprint_name, config in routes_config.items():
            # Tạo blueprint
            blueprint = Blueprint(
                blueprint_name,
                __name__,
                url_prefix=config.get('url_prefix')
            )
            
            # Đăng ký routes cho blueprint
            self.register_routes_for_blueprint(blueprint, config['routes'])
            
            self.blueprints[blueprint_name] = blueprint
    
    def register_routes_for_blueprint(self, blueprint, routes):
        """Đăng ký routes cho một blueprint"""
        for route_config in routes:
            view_class = self.get_view_class(route_config['view_class'])
            
            # Áp dụng decorators
            view_func = view_class.as_view(route_config['endpoint'])
            view_func = self.apply_decorators(view_func, route_config)
            
            # Đăng ký route
            blueprint.add_url_rule(
                route_config['url'],
                endpoint=route_config['endpoint'],
                view_func=view_func,
                methods=route_config['methods']
            )
    
    def get_view_class(self, view_class_name):
        """Import và trả về view class"""
        # Map view classes to their modules
        view_modules = {
            'DashboardView': 'views.dashboard',
            'SignInView': 'views.auth',
            'SignUpView': 'views.auth',
            'ProfileView': 'views.auth',
            'LogoutView': 'views.auth',
            'UserManagementView': 'views.management',
            'CustomView': 'views.management',
            'UserAPIView': 'views.api',
            'UserDetailAPIView': 'views.api'
        }
        
        module_name = view_modules.get(view_class_name)
        if not module_name:
            raise ImportError(f"Unknown view class: {view_class_name}")
        
        module = importlib.import_module(module_name)
        return getattr(module, view_class_name)
    
    def apply_decorators(self, view_func, route_config):
        """Áp dụng decorators dựa trên config"""
        from utils.decorators import login_required, admin_required
        
        if route_config.get('auth_required'):
            view_func = login_required(view_func)
        
        if route_config.get('admin_required'):
            view_func = admin_required(view_func)
        
        return view_func
    
    def register_blueprints(self, app):
        """Đăng ký tất cả blueprints với app"""
        for blueprint in self.blueprints.values():
            app.register_blueprint(blueprint)
    
    def init_app(self, app):
        """Initialize với Flask app"""
        self.app = app
        routes_config = self.load_routes_from_json()
        self.create_blueprints(routes_config)
        self.register_blueprints(app)
