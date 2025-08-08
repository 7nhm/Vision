from views.base import AdminRequiredView
from flask import request, jsonify

class UserManagementView(AdminRequiredView):
    """User management view"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/tbCustom.html'
        self.title = 'Quản Lý - VisionMate'
    
    def get(self):
        """Show user management page"""
        users = self.get_users_data()
        return self.render_template(users=users)
    
    def get_users_data(self):
        """Get users data"""
        return [
            {
                'id': 1,
                'name': 'John Michael',
                'email': 'john@creative-tim.com',
                'relation': 'Ba',
                'date': '23/04/18',
                'avatar': 'team-2.jpg'
            },
            {
                'id': 2,
                'name': 'Alex Smith',
                'email': 'alex@creative-tim.com',
                'relation': 'Mẹ', 
                'date': '15/03/18',
                'avatar': 'team-3.jpg'
            },
            {
                'id': 3,
                'name': 'Sarah Connor',
                'email': 'sarah@creative-tim.com',
                'relation': 'Con',
                'date': '10/02/18', 
                'avatar': 'team-4.jpg'
            }
        ]

class CustomView(AdminRequiredView):
    """Custom page view"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/custom.html'
        self.title = 'Custom - VisionMate'
    
    def get(self):
        """Show custom page"""
        return self.render_template()
