from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run the Flask application using a production-grade WSGI server like gunicorn
    # gunicorn is recommended for production deployments
    # Example command to start gunicorn: gunicorn -w 4 -b 0.0.0.0:5000 run:app
    app.run()