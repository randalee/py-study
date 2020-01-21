from flask import Flask, url_for

app = Flask(__name__)

@app.route("/hello")
def main():
    return 'hello'

@app.route("/user/<user>")
def get_user(user):
    return 'user : ' + user

if __name__ == "__main__":
    with app.test_request_context():
        print (url_for('main'))
        print (url_for('get_user', user='randa'))