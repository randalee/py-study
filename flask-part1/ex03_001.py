from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1>Hello World!!</H1>"

@app.route("/user/<username>")  # <> 를 이용하여 변수를 받을 수 있다.
def show_user(username):
    return "user : " + username

@app.route('/post/<int:post_id>')  # 타입을 지정할 수 있다. 다만 타입이 틀릴경우 에러 뿜뿜
def show_post(post_id):
    return "post : " + str(post_id)

@app.route('/circle/<float:pi>')
def show_pi(pi):
    return "post : " + str(pi)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)