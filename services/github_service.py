import requests
import base64
import re

def fetch_github_repo(repo_url, token):
    """
    Fetch the contents of a GitHub repository using the GitHub API with authentication.

    Args:
    - repo_url (str): The full URL of the GitHub repository (e.g., https://github.com/username/repo)
    - token (str): The GitHub API token for authentication

    Returns:
    - list: A list of files in the repository, or None if the request failed.
    """
    parts = repo_url.strip('/').split('/')
    if len(parts) < 2:
        return None
    
    owner, repo = parts[-2], parts[-1]
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        files = response.json()
        return files
    else:
        return None

def fetch_file_content(owner, repo, file_path, token):
    """
    Fetch the content of a specific file from a GitHub repository, including files in subfolders.
    
    Args:
    - owner (str): The GitHub repository owner.
    - repo (str): The GitHub repository name.
    - file_path (str): The path to the file in the repository, including subfolders.

    Returns:
    - str: The content of the file, or None if the request failed.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        try:
            content = response.json()
            
            if isinstance(content, list):  # If it's a directory
                files = []
                for item in content:
                    if item['type'] == 'file':
                        files.append(fetch_file_content(owner, repo, item['path']))
                    elif item['type'] == 'dir':
                        files.extend(fetch_file_content(owner, repo, item['path']))
                return files  # Return all files found in the directory and subdirectories

            elif isinstance(content, dict) and 'content' in content:  # If it's a file
                file_content = content.get('content')
                file_content = base64.b64decode(file_content).decode('utf-8')
                return file_content
            else:
                return None
        except Exception as e:
            print(f"Error while fetching file content: {e}")
            return None
    else:
        print(f"Failed to fetch content for {file_path}. Status code: {response.status_code}")
        return None


def analyze_code_quality(file_content, filename):
    """
    Analyze the code quality of a given file based on predefined rules, excluding config files.

    Args:
    - file_content (str): The content of the file to analyze.
    - filename (str): The name of the file being analyzed.

    Returns:
    - dict: A dictionary containing feedback and a score.
    """
    feedback = []
    score = 100
    
    # Exclude config files from analysis
    if filename.endswith(('.config', '.ini', '.json', 'config.js', 'config.ts', 'md', '.gitignore', '.mjs', '.lock', 'prettierignore')):
        return {"feedback": feedback, "score": score}
    
    if len(file_content.splitlines()) > 50:
        feedback.append("Warning: File has more than 50 lines, consider breaking it into smaller functions.")
        score -= 10
    
    if re.search(r'["\'](API_KEY|SECRET_KEY|PASSWORD)["\']', file_content):
        feedback.append("Warning: Sensitive data (API keys or passwords) found in the code.")
        score -= 20

    if re.search(r'\bvar\s+\w+\s*=\s*\w+\s*;', file_content):
        feedback.append(f"Warning: Unused variable detected in {filename}.")
        score -= 10
    
    if filename.endswith(('.jsx', '.js')) and "function " not in file_content:
        feedback.append(f"Warning: React component in {filename} should be a function component.")
        score -= 15

    if re.search(r'\(.*\)\s*=>\s*{.*}', file_content):
        feedback.append(f"Warning: Avoid inline functions in JSX in {filename}. This can cause performance issues.")
        score -= 10

    if not re.search(r'\b(let|const)\b', file_content):
        feedback.append(f"Warning: Use `let` or `const` for variable declaration in {filename}.")
        score -= 5
    
    return {"feedback": feedback, "score": score}

def categorize_feedback(all_feedback):
    """
    Categorize feedback into sections for better organization.
    
    Args:
    - all_feedback (list): A list of all feedback strings.
    
    Returns:
    - dict: A dictionary containing feedback categorized by section.
    """
    categorized_feedback = {
        "Code Quality": [],
        "Security": [],
        "React Best Practices": [],
    }
    
    for feedback in all_feedback:
        if "Warning" in feedback:
            if "API keys" in feedback:
                categorized_feedback["Security"].append(feedback)
            elif "React component" in feedback or "inline function" in feedback:
                categorized_feedback["React Best Practices"].append(feedback)
            else:
                categorized_feedback["Code Quality"].append(feedback)
    
    return categorized_feedback
