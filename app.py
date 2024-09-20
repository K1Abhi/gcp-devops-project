from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi, BHushan today is your last working day !!!'
