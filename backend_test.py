#!/usr/bin/env python3
"""
Comprehensive Backend Testing for Уроки Ислама (Islamic Lessons) Application
Tests Supabase integration and all API endpoints
"""

import requests
import json
import sys
import time
from datetime import datetime
import uuid

# Configuration
BASE_URL = "https://data-bridge-15.preview.emergentagent.com/api"
ADMIN_CREDENTIALS = [
    {"username": "admin", "password": "admin123"},
    {"username": "miftahulum", "password": "197724"}
]

class IslamicLessonsAPITester:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.admin_token = None
        self.test_results = []
        
    def log_test(self, test_name, success, message="", details=None):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        result = {
            "test": test_name,
            "status": status,
            "message": message,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)
        print(f"{status} {test_name}: {message}")
        if details and not success:
            print(f"   Details: {details}")
    
    def test_basic_connection(self):
        """Test basic API connection"""
        try:
            response = self.session.get(f"{self.base_url}/")
            if response.status_code == 200:
                data = response.json()
                expected_message = "Hello World with Supabase"
                if data.get("message") == expected_message:
                    self.log_test("Basic Connection", True, f"API responding correctly: {data['message']}")
                    return True
                else:
                    self.log_test("Basic Connection", False, f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("Basic Connection", False, f"HTTP {response.status_code}: {response.text}")
                return False
        except Exception as e:
            self.log_test("Basic Connection", False, f"Connection failed: {str(e)}")
            return False
    
    def test_admin_authentication(self):
        """Test admin authentication with both credential sets"""
        for i, creds in enumerate(ADMIN_CREDENTIALS):
            try:
                response = self.session.post(
                    f"{self.base_url}/admin/login",
                    json=creds
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if "access_token" in data and "token_type" in data:
                        if i == 0:  # Store token from first successful login
                            self.admin_token = data["access_token"]
                        self.log_test(
                            f"Admin Auth ({creds['username']})", 
                            True, 
                            f"Login successful, token received"
                        )
                    else:
                        self.log_test(
                            f"Admin Auth ({creds['username']})", 
                            False, 
                            f"Invalid response format: {data}"
                        )
                else:
                    self.log_test(
                        f"Admin Auth ({creds['username']})", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test(
                    f"Admin Auth ({creds['username']})", 
                    False, 
                    f"Authentication failed: {str(e)}"
                )
        
        return self.admin_token is not None
    
    def get_auth_headers(self):
        """Get authorization headers"""
        if not self.admin_token:
            return {}
        return {"Authorization": f"Bearer {self.admin_token}"}
    
    def test_team_management(self):
        """Test team management endpoints"""
        # Test public team endpoint
        try:
            response = self.session.get(f"{self.base_url}/team")
            if response.status_code == 200:
                team_data = response.json()
                team_count = len(team_data)
                if team_count == 4:
                    self.log_test(
                        "Public Team API", 
                        True, 
                        f"Retrieved {team_count} team members as expected"
                    )
                    
                    # Log team member names for verification
                    member_names = [member.get('name', 'Unknown') for member in team_data]
                    print(f"   Team members: {', '.join(member_names)}")
                else:
                    self.log_test(
                        "Public Team API", 
                        False, 
                        f"Expected 4 team members, got {team_count}",
                        team_data
                    )
            else:
                self.log_test(
                    "Public Team API", 
                    False, 
                    f"HTTP {response.status_code}: {response.text}"
                )
        except Exception as e:
            self.log_test("Public Team API", False, f"Request failed: {str(e)}")
        
        # Test admin team endpoint
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/team",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    admin_team_data = response.json()
                    self.log_test(
                        "Admin Team API", 
                        True, 
                        f"Retrieved {len(admin_team_data)} team members for admin"
                    )
                else:
                    self.log_test(
                        "Admin Team API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Admin Team API", False, f"Request failed: {str(e)}")
    
    def test_course_management(self):
        """Test course management endpoints"""
        # Test public courses
        try:
            response = self.session.get(f"{self.base_url}/courses")
            if response.status_code == 200:
                courses_data = response.json()
                self.log_test(
                    "Public Courses API", 
                    True, 
                    f"Retrieved {len(courses_data)} published courses"
                )
            else:
                self.log_test(
                    "Public Courses API", 
                    False, 
                    f"HTTP {response.status_code}: {response.text}"
                )
        except Exception as e:
            self.log_test("Public Courses API", False, f"Request failed: {str(e)}")
        
        # Test admin courses
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/courses",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    admin_courses_data = response.json()
                    self.log_test(
                        "Admin Courses API", 
                        True, 
                        f"Retrieved {len(admin_courses_data)} courses for admin"
                    )
                else:
                    self.log_test(
                        "Admin Courses API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Admin Courses API", False, f"Request failed: {str(e)}")
    
    def test_lesson_management(self):
        """Test lesson management endpoints"""
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/lessons",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    lessons_data = response.json()
                    self.log_test(
                        "Admin Lessons API", 
                        True, 
                        f"Retrieved {len(lessons_data)} lessons for admin"
                    )
                else:
                    self.log_test(
                        "Admin Lessons API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Admin Lessons API", False, f"Request failed: {str(e)}")
    
    def test_testing_system(self):
        """Test the testing system endpoints"""
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/tests",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    tests_data = response.json()
                    self.log_test(
                        "Admin Tests API", 
                        True, 
                        f"Retrieved {len(tests_data)} tests for admin"
                    )
                else:
                    self.log_test(
                        "Admin Tests API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Admin Tests API", False, f"Request failed: {str(e)}")
    
    def test_universal_table_manager(self):
        """Test Universal Table Manager endpoints"""
        if self.admin_token:
            # Test table list
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/tables/list",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    tables_data = response.json()
                    if tables_data.get("success"):
                        tables = tables_data.get("tables", [])
                        table_count = len(tables)
                        self.log_test(
                            "Table List API", 
                            True, 
                            f"Retrieved {table_count} tables from database"
                        )
                        
                        # Expected tables based on test_result.md
                        expected_tables = [
                            'courses', 'lessons', 'tests', 'questions', 'admin_users', 
                            'team_members', 'qa_questions', 'users', 'test_results', 
                            'promocodes'
                        ]
                        
                        found_tables = [table.get('table_name', table) for table in tables if isinstance(table, dict)]
                        if not found_tables:
                            found_tables = tables  # If tables is a simple list
                        
                        print(f"   Found tables: {', '.join(map(str, found_tables[:10]))}{'...' if len(found_tables) > 10 else ''}")
                        
                        # Test table structure for team_members
                        if 'team_members' in str(tables):
                            self.test_table_structure('team_members')
                        
                    else:
                        self.log_test(
                            "Table List API", 
                            False, 
                            f"API returned success=false: {tables_data}"
                        )
                else:
                    self.log_test(
                        "Table List API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Table List API", False, f"Request failed: {str(e)}")
    
    def test_table_structure(self, table_name):
        """Test table structure endpoint"""
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/tables/{table_name}/structure",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    structure_data = response.json()
                    if structure_data.get("success"):
                        self.log_test(
                            f"Table Structure ({table_name})", 
                            True, 
                            f"Retrieved structure for {table_name} table"
                        )
                    else:
                        self.log_test(
                            f"Table Structure ({table_name})", 
                            False, 
                            f"API returned success=false: {structure_data}"
                        )
                else:
                    self.log_test(
                        f"Table Structure ({table_name})", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test(f"Table Structure ({table_name})", False, f"Request failed: {str(e)}")
    
    def test_qa_system(self):
        """Test Q&A system endpoints"""
        # Test public Q&A questions
        try:
            response = self.session.get(f"{self.base_url}/qa/questions")
            if response.status_code == 200:
                qa_data = response.json()
                self.log_test(
                    "Q&A Questions API", 
                    True, 
                    f"Retrieved {len(qa_data)} Q&A questions"
                )
            else:
                self.log_test(
                    "Q&A Questions API", 
                    False, 
                    f"HTTP {response.status_code}: {response.text}"
                )
        except Exception as e:
            self.log_test("Q&A Questions API", False, f"Request failed: {str(e)}")
        
        # Test Q&A categories
        try:
            response = self.session.get(f"{self.base_url}/qa/categories")
            if response.status_code == 200:
                categories_data = response.json()
                self.log_test(
                    "Q&A Categories API", 
                    True, 
                    f"Retrieved {len(categories_data)} Q&A categories"
                )
            else:
                self.log_test(
                    "Q&A Categories API", 
                    False, 
                    f"HTTP {response.status_code}: {response.text}"
                )
        except Exception as e:
            self.log_test("Q&A Categories API", False, f"Request failed: {str(e)}")
        
        # Test admin Q&A
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/qa/questions",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    admin_qa_data = response.json()
                    self.log_test(
                        "Admin Q&A API", 
                        True, 
                        f"Retrieved {len(admin_qa_data)} Q&A questions for admin"
                    )
                else:
                    self.log_test(
                        "Admin Q&A API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Admin Q&A API", False, f"Request failed: {str(e)}")
    
    def test_promocode_system(self):
        """Test promocode validation system"""
        # Test with a sample promocode validation
        test_promocode_data = {
            "code": "TEST2024",
            "student_email": "test@example.com"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/validate-promocode",
                json=test_promocode_data
            )
            
            # We expect either 200 (valid) or 404 (not found) - both are acceptable
            if response.status_code in [200, 404]:
                if response.status_code == 200:
                    promocode_data = response.json()
                    self.log_test(
                        "Promocode Validation API", 
                        True, 
                        f"Promocode validation working - found valid code"
                    )
                else:
                    self.log_test(
                        "Promocode Validation API", 
                        True, 
                        f"Promocode validation working - test code not found (expected)"
                    )
            else:
                self.log_test(
                    "Promocode Validation API", 
                    False, 
                    f"HTTP {response.status_code}: {response.text}"
                )
        except Exception as e:
            self.log_test("Promocode Validation API", False, f"Request failed: {str(e)}")
    
    def test_supabase_connection_stability(self):
        """Test Supabase connection stability by making multiple requests"""
        success_count = 0
        total_requests = 5
        
        for i in range(total_requests):
            try:
                response = self.session.get(f"{self.base_url}/")
                if response.status_code == 200:
                    success_count += 1
                time.sleep(0.5)  # Small delay between requests
            except:
                pass
        
        stability_percentage = (success_count / total_requests) * 100
        if stability_percentage >= 80:
            self.log_test(
                "Supabase Connection Stability", 
                True, 
                f"{success_count}/{total_requests} requests successful ({stability_percentage}%)"
            )
        else:
            self.log_test(
                "Supabase Connection Stability", 
                False, 
                f"Only {success_count}/{total_requests} requests successful ({stability_percentage}%)"
            )
    
    def test_dashboard_stats(self):
        """Test dashboard statistics endpoint"""
        if self.admin_token:
            try:
                response = self.session.get(
                    f"{self.base_url}/admin/dashboard",
                    headers=self.get_auth_headers()
                )
                if response.status_code == 200:
                    dashboard_data = response.json()
                    stats = [
                        f"Students: {dashboard_data.get('total_students', 0)}",
                        f"Courses: {dashboard_data.get('total_courses', 0)}",
                        f"Lessons: {dashboard_data.get('total_lessons', 0)}",
                        f"Tests: {dashboard_data.get('total_tests', 0)}",
                        f"Teachers: {dashboard_data.get('total_teachers', 0)}"
                    ]
                    self.log_test(
                        "Dashboard Stats API", 
                        True, 
                        f"Retrieved dashboard statistics: {', '.join(stats)}"
                    )
                else:
                    self.log_test(
                        "Dashboard Stats API", 
                        False, 
                        f"HTTP {response.status_code}: {response.text}"
                    )
            except Exception as e:
                self.log_test("Dashboard Stats API", False, f"Request failed: {str(e)}")
    
    def run_all_tests(self):
        """Run all tests in sequence"""
        print("🚀 Starting comprehensive backend testing for Уроки Ислама")
        print(f"🔗 Testing against: {self.base_url}")
        print("=" * 80)
        
        # Core connectivity tests
        if not self.test_basic_connection():
            print("❌ Basic connection failed - aborting further tests")
            return False
        
        # Authentication tests
        if not self.test_admin_authentication():
            print("⚠️  Admin authentication failed - some tests will be skipped")
        
        # API endpoint tests
        self.test_team_management()
        self.test_course_management()
        self.test_lesson_management()
        self.test_testing_system()
        self.test_universal_table_manager()
        self.test_qa_system()
        self.test_promocode_system()
        self.test_dashboard_stats()
        
        # Stability tests
        self.test_supabase_connection_stability()
        
        return True
    
    def generate_report(self):
        """Generate test report"""
        print("\n" + "=" * 80)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 80)
        
        passed = sum(1 for result in self.test_results if "✅ PASS" in result["status"])
        failed = sum(1 for result in self.test_results if "❌ FAIL" in result["status"])
        total = len(self.test_results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed} ✅")
        print(f"Failed: {failed} ❌")
        print(f"Success Rate: {(passed/total*100):.1f}%")
        
        if failed > 0:
            print("\n❌ FAILED TESTS:")
            for result in self.test_results:
                if "❌ FAIL" in result["status"]:
                    print(f"  - {result['test']}: {result['message']}")
        
        print("\n✅ PASSED TESTS:")
        for result in self.test_results:
            if "✅ PASS" in result["status"]:
                print(f"  - {result['test']}: {result['message']}")
        
        return passed, failed, total

def main():
    """Main test execution"""
    tester = IslamicLessonsAPITester()
    
    try:
        success = tester.run_all_tests()
        passed, failed, total = tester.generate_report()
        
        # Return appropriate exit code
        if failed == 0:
            print("\n🎉 All tests passed! Backend is working correctly.")
            return 0
        else:
            print(f"\n⚠️  {failed} test(s) failed. Please check the issues above.")
            return 1
            
    except KeyboardInterrupt:
        print("\n⏹️  Testing interrupted by user")
        return 1
    except Exception as e:
        print(f"\n💥 Testing failed with error: {str(e)}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)