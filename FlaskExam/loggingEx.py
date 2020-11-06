import flask

# 어플리케이션 생성
app = flask.Flask(__name__)


# 웹상의 주소 1개를 만들고
@app.route('/')
def hello_world():
    return 'Hello World!'


# 로그를 출력 가능하다!!!
@app.route('/logging')
def logging_test():
    test = 1
    app.logger.debug('디버깅 필요')  # 로그 출력
    app.logger.warning(str(test) + " 라인")
    app.logger.error('에러발생')
    return "로깅 끝"


if __name__ == '__main__':
    app.debug = True
    # 서버와 포트번호 지정해서 실행
    app.run(host='localhost', port=1004)  # 서버 실행
