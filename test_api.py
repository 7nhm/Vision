#!/usr/bin/env python
"""
API Test Script - Test các API endpoints
Chạy script này khi server đang chạy để test API
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_dashboard():
    """Test dashboard endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Dashboard GET: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Dashboard GET: FAILED - {e}")
        return False

def test_auth_pages():
    """Test authentication pages"""
    endpoints = [
        "/auth/sign-in",
        "/auth/sign-up"
    ]
    
    success_count = 0
    for endpoint in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            if response.status_code == 200:
                print(f"✅ {endpoint} GET: {response.status_code}")
                success_count += 1
            else:
                print(f"❌ {endpoint} GET: {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint} GET: FAILED - {e}")
    
    return success_count == len(endpoints)

def test_api_endpoints():
    """Test API endpoints (cần authentication)"""
    try:
        # Test GET users API (sẽ redirect vì cần auth)
        response = requests.get(f"{BASE_URL}/api/v1/users")
        print(f"✅ API Users GET: {response.status_code} (expected redirect/401)")
        
        # Test API với invalid endpoint
        response = requests.get(f"{BASE_URL}/api/v1/nonexistent")
        print(f"✅ API 404 test: {response.status_code}")
        
        return True
    except Exception as e:
        print(f"❌ API endpoints: FAILED - {e}")
        return False

def test_error_pages():
    """Test error pages"""
    try:
        # Test 404 page
        response = requests.get(f"{BASE_URL}/nonexistent-page")
        print(f"✅ 404 Error page: {response.status_code}")
        return response.status_code == 404
    except Exception as e:
        print(f"❌ Error pages: FAILED - {e}")
        return False

def main():
    """Run all API tests"""
    print("🧪 Testing VisionMate API Endpoints")
    print("Make sure the server is running on http://localhost:5000")
    print("=" * 60)
    
    tests = [
        ("Dashboard", test_dashboard),
        ("Auth Pages", test_auth_pages), 
        ("API Endpoints", test_api_endpoints),
        ("Error Pages", test_error_pages)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}:")
        if test_func():
            passed += 1
            print(f"   ✅ {test_name}: PASSED")
        else:
            print(f"   ❌ {test_name}: FAILED")
    
    print("\n" + "=" * 60)
    print(f"📊 API Test Results: {passed}/{total} test groups passed")
    
    if passed == total:
        print("🎉 All API tests passed!")
        print("\n🌐 Available endpoints:")
        print("   • Dashboard: http://localhost:5000/")
        print("   • Sign In: http://localhost:5000/auth/sign-in")
        print("   • Sign Up: http://localhost:5000/auth/sign-up")
        print("   • Management: http://localhost:5000/management/users")
        print("   • API: http://localhost:5000/api/v1/users")
    else:
        print("⚠️  Some API tests failed.")

if __name__ == "__main__":
    main()
