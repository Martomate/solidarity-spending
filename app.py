# app.py
from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return '''
    <html>
      <head>
        <title>Solidarity Spending</title>
        <link rel="stylesheet" href="/css/main.css" />
      </head>
      <body>
        <h1>Welcome to Solidarity Spendning!</h1>
        <p>This is a demo page, and not the final product.</p><p>There is a map <a href="/map">here</a> and a Facebook test <a href="/fb_test">here</a></p>
      </body>
    </html>
    '''

@app.route('/js/<path:path>')
def serveJavascript(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def serveCSS(path):
    return send_from_directory('css', path)

@app.route('/map/')
def map():
    return send_from_directory('map', 'map_test.html')

@app.route('/fb_test/')
def fb_test():
    return send_from_directory('fb', 'fb_test.html')

@app.route('/privacy/')
def privacy_policy():
    return '''
    <html>
      <head>
        <title>Privacy Policy - Solidarity Spending</title>
        <link rel="stylesheet" href="/css/main.css" />
      </head>
      <body>
        <h1>Privacy Policy for Solidarity Spending</h1>
        <p>
          We do not use your data at the moment, but in the future we would use it 
          to connect you with your data so that you can see what you have spent. 
          The data will not be sold to anyone at least.
        </p>
        <p>
          In the future there could be a feature where you can share your spendings on Facebook, 
          and in that case your data would be shared with your explicit permission.
        </p>
      </body>
    </html>
    '''

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)