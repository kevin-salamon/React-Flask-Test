from flask import Flask, request

app = Flask(__name__)

@app.route('/jobs')
def jobs():
    return 'dey took er jerbs!'