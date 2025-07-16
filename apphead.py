from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/info', methods=['GET', 'HEAD', 'OPTIONS'])
def info():
    if request.method == 'HEAD':
        # Return only headers, no body
        response = make_response('', 200)
        response.headers['Custom-Header'] = 'HeadRequestTest'
        return response

    if request.method == 'OPTIONS':
        response = make_response('', 200)
        response.headers['Allow'] = 'GET,HEAD,OPTIONS'
        response.headers['Content-Type'] = 'application/json'
        return response

    # GET method fallback
    return jsonify({"message": "This is an info route."})

if __name__ == '__main__':
    app.run(debug=True)
