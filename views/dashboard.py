from views.base import BaseView
from flask import session

class DashboardView(BaseView):
    """Dashboard main view"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/UserDashboard.html'
        self.title = 'Dashboard - VisionMate'
    
    def get_context(self):
        """Thêm context data cho dashboard"""
        context = super().get_context()
        context.update({
            'user_name': session.get('user_name', 'Guest'),
            'stats': self.get_dashboard_stats(),
            'recent_activities': self.get_recent_activities()
        })
        return context
    
    def get_dashboard_stats(self):
        """Lấy thống kê cho dashboard"""
        return {
            'total_users': 150,
            'total_projects': 25,
            'completion_rate': 85.5,
            'active_sessions': 12
        }
    
    def get_recent_activities(self):
        """Lấy hoạt động gần đây"""
        return [
            {
                'user': 'John Doe',
                'action': 'Logged in',
                'time': '2 minutes ago'
            },
            {
                'user': 'Jane Smith', 
                'action': 'Updated profile',
                'time': '15 minutes ago'
            }
        ]
    
    def get(self):
        """Handle GET request"""
        return self.render_template()
