# 🚀 GitHub Code Quality Scanner 🚀

This project is a Flask-based web application that scans a GitHub repository for code quality issues and provides feedback on best practices and security concerns. It utilizes the GitHub API to fetch repository contents and analyze individual files.

[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg?logo=python)](https://www.python.org/downloads/release/python-390/)
[![Flask Version](https://img.shields.io/badge/Flask-3.1.0-green.svg?logo=flask)](https://flask.palletsprojects.com/en/3.1.x/)
[![GitHub API](https://img.shields.io/badge/GitHub%20API-v3-yellow.svg?logo=github)](https://docs.github.com/en/rest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?logo=opensourceinitiative)](https://opensource.org/licenses/MIT)
[![Blinker Version](https://img.shields.io/badge/Blinker-1.9.0-blue.svg?logo=python)](https://pypi.org/project/blinker/)
[![Certifi Version](https://img.shields.io/badge/Certifi-2024.8.30-green.svg?logo=python)](https://pypi.org/project/certifi/)
[![Charset-Normalizer Version](https://img.shields.io/badge/Charset--Normalizer-3.4.0-yellow.svg?logo=python)](https://pypi.org/project/charset-normalizer/)
[![Click Version](https://img.shields.io/badge/Click-8.1.7-blue.svg?logo=python)](https://pypi.org/project/click/)
[![Idna Version](https://img.shields.io/badge/Idna-3.10-green.svg?logo=python)](https://pypi.org/project/idna/)
[![Importlib-Metadata Version](https://img.shields.io/badge/Importlib--Metadata-8.5.0-yellow.svg?logo=python)](https://pypi.org/project/importlib-metadata/)
[![ItsDangerous Version](https://img.shields.io/badge/ItsDangerous-2.2.0-blue.svg?logo=python)](https://pypi.org/project/itsdangerous/)
[![Jinja2 Version](https://img.shields.io/badge/Jinja2-3.1.4-green.svg?logo=jinja)](https://pypi.org/project/Jinja2/)
[![MarkupSafe Version](https://img.shields.io/badge/MarkupSafe-3.0.2-yellow.svg?logo=python)](https://pypi.org/project/MarkupSafe/)
[![Requests Version](https://img.shields.io/badge/Requests-2.32.3-blue.svg?logo=requests)](https://pypi.org/project/requests/)
[![Urllib3 Version](https://img.shields.io/badge/Urllib3-2.2.3-green.svg?logo=python)](https://pypi.org/project/urllib3/)
[![Werkzeug Version](https://img.shields.io/badge/Werkzeug-3.1.3-yellow.svg?logo=python)](https://pypi.org/project/Werkzeug/)
[![Zipp Version](https://img.shields.io/badge/Zipp-3.21.0-blue.svg?logo=python)](https://pypi.org/project/zipp/)

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
* JavaScript and HTML/CSS for frontend user interface 📦

