from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello CHANGE THIS MESSAGE TO TRIGGER BUILDS" :) "
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

