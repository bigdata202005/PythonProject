# 모듈 읽고
from flask import Flask

# 어플리케이션 생성
app = Flask(__name__)


# 웹상의 주소 1개를 만들고
@app.route('/')
def hello_world():
    return 'Hello World!'


# 웹상의 주소 1개를 만들고
@app.route('/hi')
def hello_world2():
    return '<h1>안녕</h1>'


if __name__ == '__main__':
    app.debug = True
    app.run()  # 서버 실행
