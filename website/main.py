import flask
from flask import request
from Predictor import Test
from flask import send_from_directory, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/upload')
def upload():
	return render_template('main.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return '''
    <html>
    	<head>
        	<title>Score</title>
        	<link rel="stylesheet" href="static/score.css">
    	</head>
    	<body>
        	<h1>Your costume is, ''' + Test.run_test(request.files['avatar']) + '''!</h1>
    	</body>
	</html>  '''

app.run()
