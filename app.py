import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    test = os.environ.get('TEST')
    mystr = "Welcome " + test + "!" 
    return mystr

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
