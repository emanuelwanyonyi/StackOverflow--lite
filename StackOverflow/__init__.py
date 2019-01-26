from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

from StackOverflow.site.routes import blueprint
#from StackOverflow.api.routes import blueprint
from StackOverflow.api.views import blueprint

app.register_blueprint(site.routes.blueprint)
#app.register_blueprint(api.routes.blueprint, url_prefix='/api/v1')
app.register_blueprint(api.views.auth_api_blueprint, url_prefix='/api/v1')

BCRYPT_LOG_ROUNDS = 13

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))