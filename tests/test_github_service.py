import unittest
from services.github_service import fetch_github_repo, fetch_file_content, analyze_code_quality, categorize_feedback

class TestGitHubService(unittest.TestCase):

    def test_fetch_github_repo_valid(self):
        repo_url = "https://github.com/username/repo"
        token = "valid_token"
        result = fetch_github_repo(repo_url, token)
        self.assertIsInstance(result, list)

    def test_fetch_github_repo_invalid(self):
        repo_url = "https://github.com/invalid/repo"
        token = "valid_token"
        result = fetch_github_repo(repo_url, token)
        self.assertIsNone(result)

    def test_fetch_file_content_valid(self):
        owner = "username"
        repo = "repo"
        file_path = "path/to/file.py"
        token = "valid_token"
        result = fetch_file_content(owner, repo, file_path, token)
        self.assertIsInstance(result, str)

    def test_fetch_file_content_invalid(self):
        owner = "username"
        repo = "repo"
        file_path = "invalid/path/to/file.py"
        token = "valid_token"
        result = fetch_file_content(owner, repo, file_path, token)
        self.assertIsNone(result)

    def test_analyze_code_quality(self):
        file_content = "def example_function():\n    pass"
        filename = "example.py"
        result = analyze_code_quality(file_content, filename)
        self.assertIn("feedback", result)
        self.assertIn("score", result)

    def test_categorize_feedback(self):
        all_feedback = [
            "Warning: Sensitive data (API keys or passwords) found in the code.",
            "Warning: Unused variable detected in example.py."
        ]
        result = categorize_feedback(all_feedback)
        self.assertIn("Security", result)
        self.assertIn("Code Quality", result)

if __name__ == '__main__':
    unittest.main() 