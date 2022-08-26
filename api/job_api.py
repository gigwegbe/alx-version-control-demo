import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Job APIs</h1><p>This site is a prototype API for job apis.</p>"

app.run()
