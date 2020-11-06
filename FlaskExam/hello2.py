# 모듈 읽고
from flask import Flask

# 어플리케이션 생성
app = Flask(__name__)


# 웹상의 주소 1개를 만들고
@app.route('/')
def hello_world():
    return 'Hello World!'


# 경로를 인수로 받을때 <이름>을 사용한다. 기본으로 문자열
@app.route('/user/<username>')
def show_user_profile(username):
    return "사용자이름 : {}".format(username)


# 경로를 인수로 받을때 <타입:이름>을 사용하여 자료형 지정이 가능하다. 숫자만 유효!!!
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ID : {}'.format(post_id)


if __name__ == '__main__':
    app.debug = True
    # 서버와 포트번호 지정해서 실행
    app.run(host='localhost', port=1004)  # 서버 실행
