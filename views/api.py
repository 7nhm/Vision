from views.base import BaseAPIView
from flask import request
from utils.decorators import login_required, validate_json, rate_limit

class UserAPIView(BaseAPIView):
    """User API endpoints"""
    decorators = [login_required, rate_limit(max_requests=100)]
    
    def get(self):
        """Get all users"""
        users = self.get_users_data()
        return self.get_success_response(data=users)
    
    @validate_json(required_fields=['name', 'email'])
    def post(self):
        """Create new user"""
        data = request.get_json()
        
        # Validate and create user
        if self.create_user(data):
            return self.get_success_response(
                message="User created successfully",
                status_code=201
            )
        else:
            return self.get_error_response(
                message="Failed to create user",
                status_code=400
            )
    
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
    
    def create_user(self, data):
        """Create user in database"""
        # Implement user creation logic
        return True

class UserDetailAPIView(BaseAPIView):
    """User detail API endpoints"""
    decorators = [login_required]
    
    def get(self, user_id):
        """Get specific user"""
        user = self.get_user_by_id(user_id)
        if user:
            return self.get_success_response(data=user)
        return self.get_error_response(
            message="User not found",
            status_code=404
        )
    
    @validate_json()
    def put(self, user_id):
        """Update user"""
        data = request.get_json()
        
        if self.update_user(user_id, data):
            return self.get_success_response(
                message="User updated successfully"
            )
        return self.get_error_response(
            message="Failed to update user"
        )
    
    def delete(self, user_id):
        """Delete user"""
        if self.delete_user(user_id):
            return self.get_success_response(
                message="User deleted successfully"
            )
        return self.get_error_response(
            message="Failed to delete user"
        )
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        # Implement user lookup
        users_data = [
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
        return next((user for user in users_data if user['id'] == user_id), None)
    
    def update_user(self, user_id, data):
        """Update user in database"""
        # Implement user update logic
        return True
    
    def delete_user(self, user_id):
        """Delete user from database"""
        # Implement user deletion logic
        return True
