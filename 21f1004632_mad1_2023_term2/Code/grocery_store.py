# Main application file which is responsible for running the application

from flaskr import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        debug=False
    )