from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route cho trang chủ/dashboard
@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('pages/UserDashboard.html', title='Dashboard - VisionMate')

# Route cho trang Custom
@app.route('/custom')
def custom():
    return render_template('pages/custom.html', title='Custom - VisionMate')

# Route cho trang Quản lý
@app.route('/quan-ly')
def quan_ly():
    # Dữ liệu mẫu cho bảng
    users = [
        {
            'name': 'John Michael',
            'email': 'john@creative-tim.com',
            'relation': 'Ba',
            'date': '23/04/18',
            'avatar': 'team-2.jpg'
        },
        {
            'name': 'Alex Smith',
            'email': 'alex@creative-tim.com',
            'relation': 'Mẹ', 
            'date': '15/03/18',
            'avatar': 'team-3.jpg'
        },
        {
            'name': 'Sarah Connor',
            'email': 'sarah@creative-tim.com',
            'relation': 'Con',
            'date': '10/02/18', 
            'avatar': 'team-4.jpg'
        }
    ]
    return render_template('pages/tbCustom.html', users=users, title='Quản Lý - VisionMate')

# Route cho trang Tables
@app.route('/tables')
def tables():
    return render_template('pages/tables.html', title='Tables - VisionMate')

# Route cho trang Billing
@app.route('/billing')
def billing():
    return render_template('pages/billing.html', title='Billing - VisionMate')

# Route cho trang Virtual Reality
@app.route('/virtual-reality')
def virtual_reality():
    return render_template('pages/virtual-reality.html', title='Virtual Reality - VisionMate')

# Route cho trang RTL
@app.route('/rtl')
def rtl():
    return render_template('pages/rtl.html', title='RTL - VisionMate')

# Route cho trang Profile
@app.route('/profile')
def profile():
    return render_template('pages/profile.html', title='Profile - VisionMate')

# Route cho trang Sign In
@app.route('/sign-in')
def sign_in():
    return render_template('pages/signin.html', title='Sign In - VisionMate')

# Route cho trang Sign Up
@app.route('/sign-up')
def sign_up():
    return render_template('pages/signup.html', title='Sign Up - VisionMate')

# API endpoints cho AJAX calls
@app.route('/api/users')
def get_users():
    # Trả về dữ liệu JSON
    users = [
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
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Xử lý cập nhật user
    data = request.get_json()
    # Logic cập nhật...
    return jsonify({'status': 'success', 'message': 'User updated successfully'})

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Xử lý xóa user
    # Logic xóa...
    return jsonify({'status': 'success', 'message': 'User deleted successfully'})

@app.route('/api/users', methods=['POST'])
def create_user():
    # Xử lý tạo user mới
    data = request.get_json()
    # Logic tạo user...
    return jsonify({'status': 'success', 'message': 'User created successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
