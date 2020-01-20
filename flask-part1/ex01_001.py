from flask import Flask

app = Flask(__name__)

@app.route("/") # app.route를 이용하여 받아올 데이터를 체크한다.
def hello():
    return "Hello World!!" # 리턴되는 데이터가 html로 처리된다.

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # 외부접속을 허용하기 위하여 host를 지정, 기본포트는 5000을 이용하는데 8080으로 임의 지정한다.