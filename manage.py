#!/usr/bin/env python
"""
Project Management Script - Quản lý dự án VisionMate
"""

import os
import sys
import subprocess
import json

def show_project_info():
    """Hiển thị thông tin dự án"""
    print("📋 VisionMate Project Information")
    print("=" * 50)
    
    # Project structure
    structure = {
        "config/": ["app_config.py", "routes.json"],
        "core/": ["route_loader.py"],
        "views/": ["base.py", "dashboard.py", "auth.py", "management.py", "api.py"],
        "utils/": ["decorators.py"],
        "templates/": ["base.html", "errors/", "pages/", "partials/"],
        "static/": ["css/", "js/", "img/", "fonts/"]
    }
    
    print("📁 Project Structure:")
    for folder, files in structure.items():
        print(f"   {folder}")
        for file in files:
            if file.endswith('/'):
                print(f"     📁 {file}")
            else:
                status = "✅" if os.path.exists(file) else "❌"
                print(f"     {status} {file}")
    
    # Routes info
    try:
        with open('config/routes.json', 'r', encoding='utf-8') as f:
            routes = json.load(f)
        
        print(f"\n🛣️  Routes Configuration:")
        for blueprint, config in routes.items():
            route_count = len(config['routes'])
            prefix = config.get('url_prefix', '')
            print(f"   • {blueprint}: {route_count} routes {prefix}")
    except:
        print("\n❌ Could not load routes configuration")

def run_tests():
    """Chạy tests"""
    print("🧪 Running Tests...")
    
    try:
        result = subprocess.run([sys.executable, "test_architecture.py"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def start_server():
    """Khởi động server"""
    print("🚀 Starting VisionMate Server...")
    print("Server will run on http://localhost:5000")
    print("Press Ctrl+C to stop")
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")

def install_dependencies():
    """Cài đặt dependencies"""
    print("📦 Installing Dependencies...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except Exception as e:
        print(f"❌ Failed to install dependencies: {e}")

def create_new_view():
    """Tạo view mới"""
    print("🆕 Create New View")
    
    view_name = input("Enter view name (e.g., BlogView): ")
    module_name = input("Enter module name (e.g., blog): ")
    template_name = input("Enter template name (e.g., blog.html): ")
    
    # Create view file
    view_content = f'''from views.base import BaseView

class {view_name}(BaseView):
    """Generated view class for {module_name}"""
    
    def __init__(self):
        super().__init__()
        self.template = 'pages/{template_name}'
        self.title = '{view_name.replace("View", "")} - VisionMate'
    
    def get(self):
        """Handle GET request"""
        return self.render_template()
'''
    
    view_file = f"views/{module_name}.py"
    with open(view_file, 'w', encoding='utf-8') as f:
        f.write(view_content)
    
    print(f"✅ Created {view_file}")
    print(f"📝 Don't forget to:")
    print(f"   1. Add route to config/routes.json")
    print(f"   2. Add view mapping in core/route_loader.py")
    print(f"   3. Create template: templates/pages/{template_name}")

def show_menu():
    """Hiển thị menu chính"""
    print("\n🎯 VisionMate Project Manager")
    print("=" * 40)
    print("1. 📋 Show Project Info")
    print("2. 🧪 Run Tests")
    print("3. 🚀 Start Server")
    print("4. 📦 Install Dependencies")
    print("5. 🆕 Create New View")
    print("6. ❌ Exit")
    print("=" * 40)

def main():
    """Main function"""
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            show_project_info()
        elif choice == '2':
            run_tests()
        elif choice == '3':
            start_server()
        elif choice == '4':
            install_dependencies()
        elif choice == '5':
            create_new_view()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    main()
