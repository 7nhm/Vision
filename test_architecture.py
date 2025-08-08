#!/usr/bin/env python
"""
Test script để kiểm tra cấu trúc Flask mới
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
import json

def test_app_creation():
    """Test tạo app thành công"""
    try:
        app = create_app('testing')
        print("✅ App creation: SUCCESS")
        return True
    except Exception as e:
        print(f"❌ App creation: FAILED - {e}")
        return False

def test_routes_loading():
    """Test load routes từ JSON"""
    try:
        with open('config/routes.json', 'r', encoding='utf-8') as f:
            routes_config = json.load(f)
        
        print("✅ Routes JSON loading: SUCCESS")
        print(f"   - Found {len(routes_config)} blueprints")
        
        for bp_name, bp_config in routes_config.items():
            route_count = len(bp_config['routes'])
            print(f"   - {bp_name}: {route_count} routes")
        
        return True
    except Exception as e:
        print(f"❌ Routes JSON loading: FAILED - {e}")
        return False

def test_views_import():
    """Test import các view classes"""
    view_modules = [
        'views.base',
        'views.dashboard', 
        'views.auth',
        'views.management',
        'views.api'
    ]
    
    success_count = 0
    for module_name in view_modules:
        try:
            __import__(module_name)
            print(f"✅ Import {module_name}: SUCCESS")
            success_count += 1
        except Exception as e:
            print(f"❌ Import {module_name}: FAILED - {e}")
    
    return success_count == len(view_modules)

def test_decorators_import():
    """Test import decorators"""
    try:
        from utils.decorators import login_required, admin_required, validate_json
        print("✅ Decorators import: SUCCESS")
        return True
    except Exception as e:
        print(f"❌ Decorators import: FAILED - {e}")
        return False

def test_config_import():
    """Test import config"""
    try:
        from config.app_config import config
        print("✅ Config import: SUCCESS")
        print(f"   - Available configs: {list(config.keys())}")
        return True
    except Exception as e:
        print(f"❌ Config import: FAILED - {e}")
        return False

def test_route_loader():
    """Test RouteLoader"""
    try:
        from core.route_loader import RouteLoader
        loader = RouteLoader()
        routes_config = loader.load_routes_from_json()
        loader.create_blueprints(routes_config)
        
        print("✅ RouteLoader: SUCCESS")
        print(f"   - Created {len(loader.blueprints)} blueprints")
        return True
    except Exception as e:
        print(f"❌ RouteLoader: FAILED - {e}")
        return False

def main():
    """Chạy tất cả tests"""
    print("🚀 Testing VisionMate Flask Architecture")
    print("=" * 50)
    
    tests = [
        test_config_import,
        test_decorators_import,
        test_views_import,
        test_routes_loading,
        test_route_loader,
        test_app_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Architecture is working correctly.")
        print("\n🔥 Ready to start development!")
        print("\n📝 Next steps:")
        print("   1. Run: python app.py")
        print("   2. Visit: http://localhost:5000")
        print("   3. Login: admin@visionmate.com / admin123")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    main()
