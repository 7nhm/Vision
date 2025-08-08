from views.base import BaseView, AuthRequiredView
from flask import request, redirect, url_for, session, flash
from utils.decorators import validate_json

class SignInView(BaseView):
    """Sign in view"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/signin.html'
        self.title = 'Sign In - VisionMate'
    
    def get(self):
        """Show sign in form"""
        if 'user_id' in session:
            return redirect(url_for('dashboard.index'))
        return self.render_template()
    
    def post(self):
        """Handle sign in"""
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Implement authentication logic
        if self.authenticate_user(email, password):
            user = self.get_user_by_email(email)
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['is_admin'] = user.get('is_admin', False)
            
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Email hoặc mật khẩu không đúng!', 'error')
            return self.render_template()
    
    def authenticate_user(self, email, password):
        """Authenticate user credentials"""
        # Implement your authentication logic
        return email == "admin@visionmate.com" and password == "admin123"
    
    def get_user_by_email(self, email):
        """Get user data by email"""
        # Implement user lookup
        return {
            'id': 1,
            'name': 'Admin User',
            'email': email,
            'is_admin': True
        }

class SignUpView(BaseView):
    """Sign up view"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/signup.html'
        self.title = 'Sign Up - VisionMate'
    
    def get(self):
        """Show sign up form"""
        return self.render_template()
    
    def post(self):
        """Handle sign up"""
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'confirm_password': request.form.get('confirm_password')
        }
        
        if self.validate_signup_data(data):
            if self.create_user(data):
                flash('Đăng ký thành công! Vui lòng đăng nhập.', 'success')
                return redirect(url_for('auth.sign_in'))
            else:
                flash('Có lỗi xảy ra khi tạo tài khoản!', 'error')
        
        return self.render_template()
    
    def validate_signup_data(self, data):
        """Validate sign up data"""
        if not all([data['name'], data['email'], data['password']]):
            flash('Vui lòng điền đầy đủ thông tin!', 'error')
            return False
        
        if data['password'] != data['confirm_password']:
            flash('Mật khẩu xác nhận không khớp!', 'error')
            return False
        
        return True
    
    def create_user(self, data):
        """Create new user"""
        # Implement user creation logic
        return True

class ProfileView(AuthRequiredView):
    """User profile view"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/profile.html'
        self.title = 'Profile - VisionMate'
    
    def get(self):
        """Show user profile"""
        user_data = self.get_user_data()
        return self.render_template(user=user_data)
    
    def post(self):
        """Update user profile"""
        # Handle profile update
        flash('Cập nhật thông tin thành công!', 'success')
        return redirect(url_for('auth.profile'))
    
    def get_user_data(self):
        """Get current user data"""
        return {
            'id': session['user_id'],
            'name': session['user_name'],
            'email': 'user@example.com'
        }

class LogoutView(AuthRequiredView):
    """Logout view"""
    
    def post(self):
        """Handle logout"""
        session.clear()
        flash('Đăng xuất thành công!', 'success')
        return redirect(url_for('auth.sign_in'))
