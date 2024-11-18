import unittest
from app import app

class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Scan Your GitHub Codebase', response.data)

    def test_scan_codebase_valid(self):
        response = self.app.post('/scan', data={'repo_url': 'https://github.com/username/repo'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn("feedback", json_data)
        self.assertIn("score", json_data)

    def test_scan_codebase_invalid_url(self):
        response = self.app.post('/scan', data={'repo_url': 'invalid_url'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn("error", json_data)

if __name__ == '__main__':
    unittest.main() 