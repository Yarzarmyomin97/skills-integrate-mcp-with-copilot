import unittest

from fastapi.testclient import TestClient

from src.app import app


class ActivityCatalogTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_github_skills_activity_is_listed_and_registerable(self):
        response = self.client.get("/activities")
        self.assertEqual(response.status_code, 200)

        activities = response.json()
        self.assertIn("GitHub Skills", activities)

        signup_response = self.client.post(
            "/activities/GitHub%20Skills/signup?email=student@mergington.edu"
        )
        self.assertEqual(signup_response.status_code, 200)

        updated_activities = self.client.get("/activities").json()
        self.assertIn("student@mergington.edu", updated_activities["GitHub Skills"]["participants"])


if __name__ == "__main__":
    unittest.main()
