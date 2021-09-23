import flask

from flask import make_response, jsonify, request

app = flask.Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    response = make_response(jsonify(message="Running"), 200)
    return response


@app.route('/postendpoint', methods=['POST'])
def post_endpoint():
    data = request.get_json()
    response = make_response(jsonify(message="Received payload attached in the response", payload=data), 200)
    return response


def main():
    app.run(host='0.0.0.0', debug=False, port=8000)


if __name__ == '__main__':
    main()
