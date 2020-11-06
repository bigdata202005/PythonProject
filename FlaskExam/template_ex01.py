from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 주소 복수개 지정 가능
@app.route('/template')
@app.route('/template/<userid>')
def template_test(userid=None):
    sports = ['야구', '축구', '농구']
    # 템플릿으로 값 전달!!!
    return render_template('template2.html', tempid=userid, sports=sports)


if __name__ == '__main__':
    app.run()  # 서버 실행
