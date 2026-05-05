from flask import Flask
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
app.secret_key = "change-this"

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)