# 🚀 GitHub Code Quality Scanner 🚀

This project is a Flask-based web application that scans a GitHub repository for code quality issues and provides feedback on best practices and security concerns. It utilizes the GitHub API to fetch repository contents and analyze individual files.

[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Flask Version](https://img.shields.io/badge/Flask-3.1.0-green.svg)](https://flask.palletsprojects.com/en/3.1.x/)
[![GitHub API](https://img.shields.io/badge/GitHub%20API-v3-yellow.svg)](https://docs.github.com/en/rest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📚 Setup

1. **Clone the repository**: `git clone https://github.com/your-username/github-code-quality-scanner.git` 📁
2. **Create a virtual environment**: `python -m venv venv` 🔄
3. **Activate the virtual environment**: 
   - On Windows: `venv\Scripts\activate` 💻
   - On Unix/Linux/MacOS: `source venv/bin/activate` 🐧
4. **Install dependencies**: `pip install -r requirements.txt` 📦
5. **Set environment variables**: `export GITHUB_API_TOKEN=your-github-api-token` 🔒
6. **Run the application**: `python app.py` 🚀

## 🏃‍♂️ Running the Project

1. Open a web browser and navigate to `http://localhost:5000/` 🌐
2. Enter the GitHub repository URL you want to scan in the input field and click the "Scan" button. 🔍
3. The application will fetch the repository contents, analyze each file, and display categorized feedback and a score based on the analysis. 📊

**Note:** Ensure you have a valid GitHub API token set in your environment variables. This token is used for authentication when fetching repository contents from the GitHub API. 🔑

**Features:**

* Scans a GitHub repository for code quality issues 🚨
* Analyzes individual files for best practices and security concerns 📝
* Provides categorized feedback on code quality, security, and React best practices 📊
* Calculates a score based on the analysis 📈

**Technologies Used:**

* Flask for web application framework 🌟
* GitHub API for fetching repository contents 📁
* Python for backend logic and analysis 🐍
* JavaScript and HTML/CSS for frontend user interface 📊

