# app.py
from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    name = request.form.get('name')
    print(name)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if name:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return '<h1>Welcome to our server !!</h1><p>There is a map <a href="/map">here</a> and a Facebook test <a href="/fb_test">here</a></p>'

@app.route('/js/<path:path>')
def serveJavascript(path):
    return send_from_directory('js', path)

@app.route('/map/')
def map():
    return send_from_directory('map', 'map_test.html')

@app.route('/fb_test/')
def fb_test():
    return send_from_directory('fb', 'fb_test.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)