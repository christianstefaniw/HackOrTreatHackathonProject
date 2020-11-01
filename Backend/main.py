import flask
from flask import request
from Predictor import Test
from flask import send_from_directory

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return send_from_directory("../", "index.html")

@app.route('/upload')
def upload():
	return send_from_directory('../', 'main.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return Test.run_test(request.files['avatar'])


app.run()
