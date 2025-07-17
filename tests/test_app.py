import sys
import os
# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
def test_homepage():
    """
    Test that the homepage loads successfully
    and contains the expected button.
    """
    tester = app.test_client()            # Create test client
    response = tester.get('/')            # Send GET request to "/"
    assert response.status_code == 200    # Check HTTP 200 OK
    assert b'Show Text' in response.data  # Check if 'Show Text' button is present
    assert b'Clear Text' in response.data # Check if 'Clear Text' button is present
