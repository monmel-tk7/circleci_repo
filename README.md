# Flask Web Application - CircleCI Assignment

This is a simple Flask web application created as part of an assignment.  
The app contains a single page with a button. When clicked, it displays new text.  
The project includes automated testing and is integrated with CircleCI.

---

## Features

- Single-page web application
- Button click reveals new text
- Automated tests using pytest
- Continuous Integration with CircleCI

---

## Getting Started

### Run Locally
1. Clone the repository:

2. Set up a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Start the app:
flask run

4. Open your browser at `http://127.0.0.1:5000`

---

### Run Tests
pytest

## CircleCI

The project is configured for CircleCI. Each commit runs tests automatically.  
Build status can be viewed here:  
[CircleCI Build URL](https://app.circleci.com/pipelines/circleci/6kTenxPMF9dLWun9Jvu4PH/A1PVbzzH45LPJ2s3KuU3Cr/3)

---