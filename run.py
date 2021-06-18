from flask import Flask, request

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def cut_string():
    return 'input string: {}'.format(request.form['string_to_cut'])
