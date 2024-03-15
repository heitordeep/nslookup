from decouple import config
from flask import Flask
from flask_wtf.csrf import CSRFProtect

from app.main import app

application_whois = Flask('app')
application_whois.register_blueprint(app)
application_whois.secret_key = config('SECRET_KEY', cast=str)
csrf = CSRFProtect(application_whois)

if __name__ == "__main__":
    application_whois.run(debug=config('DEBUG', cast=bool))
