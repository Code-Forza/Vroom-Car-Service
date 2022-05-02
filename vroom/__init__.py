from flask import Flask

app = Flask(__name__)

# app.config.from_envvar('ENV_VAR')

from vroom import routes