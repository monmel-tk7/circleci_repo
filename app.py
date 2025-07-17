from flask import Flask, render_template
import logging

# Create a Flask application instance
app = Flask(__name__)

# Set up basic logger to log messages to console
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    """
    Route for the homepage.
    Logs when the home page is accessed and renders index.html.
    """
    app.logger.info("Home page accessed")
    return render_template("index.html")

@app.route("/log/show")
def log_show():
    """
    Route triggered by the 'Show Text' button.
    Logs that the Show button was clicked.
    """
    app.logger.info("Show button clicked")
    return "", 204  # Return HTTP 204 No Content

@app.route("/log/clear")
def log_clear():
    """
    Route triggered by the 'Clear Text' button.
    Logs that the Clear button was clicked.
    """
    app.logger.info("Clear button clicked")
    return "", 204  # Return HTTP 204 No Content

if __name__ == "__main__":
    # Log when the Flask server starts
    app.logger.info("Starting Flask app...")
    app.run(debug=True)