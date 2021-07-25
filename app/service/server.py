import flask

from flask import make_response, jsonify

app = flask.Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    response = make_response(jsonify(message="Running"), 200)
    return response


def main():
    app.run(host='0.0.0.0', debug=True, port=8000)


if __name__ == '__main__':
    main()
