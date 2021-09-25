#!flask/bin/python

import traceback

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from mongo import upsert

# init app
app = Flask(__name__)

# allow cross-origin requests
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


from pprint import pprint

@app.route("/upload", methods = ['POST'])
@cross_origin()
def upload():
    # extract data from request
    form = request.get_json(force=True) or None
    if form is None:
        return jsonify({"message": "Invalid JSON"}), 400

    try:
        upsert(form)
        response = jsonify({
            "message": f"Success!"
        })
        return response, 201
    except Exception as e:
        print(traceback.print_exc())
        return jsonify({"message": f"Unknown Error"}), 400

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
