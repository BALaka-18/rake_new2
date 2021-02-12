from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'welcome to RAKE'

if __name__ == "__main__":
    app.run()

