# GitHub Code Quality Scanner

This project is a Flask-based web application that scans a GitHub repository for code quality issues and provides feedback on best practices and security concerns. It utilizes the GitHub API to fetch repository contents and analyze individual files.

## Setup

1. **Clone the repository**: `git clone https://github.com/your-username/github-code-quality-scanner.git`
2. **Create a virtual environment**: `python -m venv venv`
3. **Activate the virtual environment**: 
   - On Windows: `venv\Scripts\activate`
   - On Unix/Linux/MacOS: `source venv/bin/activate`
4. **Install dependencies**: `pip install -r requirements.txt`
5. **Set environment variables**: `export GITHUB_API_TOKEN=your-github-api-token`
6. **Run the application**: `python app.py`

## Running the Project

1. Open a web browser and navigate to `http://localhost:5000/`
2. Enter the GitHub repository URL you want to scan in the input field and click the "Scan" button.
3. The application will fetch the repository contents, analyze each file, and display categorized feedback and a score based on the analysis.

**Note:** Ensure you have a valid GitHub API token set in your environment variables. This token is used for authentication when fetching repository contents from the GitHub API.

**Features:**

* Scans a GitHub repository for code quality issues
* Analyzes individual files for best practices and security concerns
* Provides categorized feedback on code quality, security, and React best practices
* Calculates a score based on the analysis

**Technologies Used:**

* Flask for web application framework
* GitHub API for fetching repository contents
* Python for backend logic and analysis
* JavaScript and HTML/CSS for frontend user interface

