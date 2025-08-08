from flask.views import MethodView
from flask import render_template, jsonify, request, session
from utils.decorators import login_required, admin_required

class BaseView(MethodView):
    """Base view class với các method chung"""
    
    def __init__(self):
        self.template = None
        self.title = None
        self.context = {}
    
    def get_context(self):
        """Override để thêm context data"""
        return self.context
    
    def render_template(self, template=None, **kwargs):
        """Render template với context"""
        template = template or self.template
        context = self.get_context()
        context.update(kwargs)
        if self.title:
            context['title'] = self.title
        return render_template(template, **context)

class BaseAPIView(MethodView):
    """Base API view class"""
    
    def __init__(self):
        self.serializer = None
    
    def get_success_response(self, data=None, message="Success", status_code=200):
        """Trả về response thành công"""
        response = {
            'success': True,
            'message': message
        }
        if data is not None:
            response['data'] = data
        return jsonify(response), status_code
    
    def get_error_response(self, message="Error", status_code=400, errors=None):
        """Trả về response lỗi"""
        response = {
            'success': False,
            'message': message
        }
        if errors:
            response['errors'] = errors
        return jsonify(response), status_code

class AuthRequiredView(BaseView):
    """View yêu cầu authentication"""
    decorators = [login_required]

class AdminRequiredView(BaseView):
    """View yêu cầu quyền admin"""
    decorators = [login_required, admin_required]
