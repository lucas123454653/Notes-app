# Function: create_app
# Purpose: Factory function to create and configure the Flask application instance.
# Description: This function sets up the Flask application by configuring settings, 
#              initializing extensions, and registering blueprints. It ensures the 
#              application is created with all necessary components for running a web service.
# Returns: A Flask application instance configured and ready to be run.

from website import create_app

# Creating the Flask application instance using the factory function.
app = create_app()

# Main entry point of the application.
if __name__ == '__main__':
    # Running the application in debug mode. This is useful for development purposes 
    # as it provides detailed error pages and auto-reloads the server on code changes.
    app.run(debug=True)