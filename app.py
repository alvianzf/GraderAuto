from flask import Flask, render_template, request, jsonify
from services.github_service import categorize_feedback, fetch_github_repo, fetch_file_content, analyze_code_quality
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
                           
@app.route('/scan', methods=['POST'])
def scan_codebase():
    repo_url = request.form.get('repo_url')
    
    parts = repo_url.strip('/').split('/')
    if len(parts) < 2:
        return jsonify({"message": "Invalid repository URL", "error": "Invalid URL format"})
    
    owner, repo = parts[-2], parts[-1]
    
    token = os.getenv('GITHUB_API_TOKEN')
    if not token:
        return jsonify({"message": "GitHub API token not found", "error": "Token not set in environment variables"})
    
    repo_data = fetch_github_repo(repo_url, token)

    if repo_data:
        all_feedback = []
        total_score = 100
        
        for file in repo_data:
            if isinstance(file, dict) and file.get('type') == 'file':
                file_content = fetch_file_content(owner, repo, file['path'], token)
                if file_content:
                    analysis = analyze_code_quality(file_content, file['name'])
                    all_feedback.extend(analysis['feedback'])
                    total_score -= (100 - analysis['score'])
                   
        categorized_feedback = categorize_feedback(all_feedback)
        
        # Return the feedback and score
        return jsonify({
            "message": "Repo analyzed successfully",
            "feedback": categorized_feedback,
            "score": total_score
        })

    else:
        return jsonify({"message": "Failed to fetch repo data", "error": "GitHub API issue or invalid repository URL"})


if __name__ == '__main__':
    app.run(debug=True)
