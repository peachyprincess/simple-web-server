import flask
from .string_utils import get_every_third_letter

app = flask.Flask(__name__)

@app.route('/test', methods=['POST'])
def cut_string():
    s = flask.request.form['string_to_cut']
    return flask.jsonify({"return_string": get_every_third_letter(s)})
