import flask
from flask import request
from Predictor import Test

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "API"


@app.route('/test', methods=['GET', 'POST'])
def test():
    return Test.run_test(request.files['file'])


app.run()
