# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
# Define a function to handle requests to the root URL
def hello_world():
    # Return the string 'Hello, World!' as the response
    return 'Hello, World!'

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the application on the local development server
    # Set debug=True to enable automatic reloading of the server on code changes
    app.run(debug=True)


