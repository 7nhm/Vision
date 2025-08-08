from functools import wraps
from flask import session, redirect, url_for, jsonify, request
from datetime import datetime, timedelta

def login_required(f):
    """Decorator yêu cầu user phải đăng nhập"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            if request.is_json:
                return jsonify({'error': 'Authentication required'}), 401
            return redirect(url_for('auth.sign_in'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator yêu cầu quyền admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin', False):
            if request.is_json:
                return jsonify({'error': 'Admin access required'}), 403
            return redirect(url_for('dashboard.index'))
        return f(*args, **kwargs)
    return decorated_function

def api_key_required(f):
    """Decorator cho API authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key or not validate_api_key(api_key):
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated_function

def rate_limit(max_requests=100, per_seconds=3600):
    """Decorator để giới hạn số lượng requests"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Implement rate limiting logic here
            # For now, just pass through
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_json(required_fields=None):
    """Decorator để validate JSON input"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not request.is_json:
                return jsonify({'error': 'JSON data required'}), 400
            
            data = request.get_json()
            if required_fields:
                missing_fields = [field for field in required_fields if field not in data]
                if missing_fields:
                    return jsonify({'error': f'Missing fields: {missing_fields}'}), 400
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_api_key(api_key):
    """Validate API key (implement your logic)"""
    # Implement your API key validation logic
    # For now, return True for demo purposes
    return api_key == "demo-api-key"
