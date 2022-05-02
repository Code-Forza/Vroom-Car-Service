from flask import Flask

app = Flask(__name__)

app.config.from_envvar('ENV_VAR')

@app.route('/')
def home():
  return '<h1> Hello </h1>'


if __name__ == '__main__':
  app.run()