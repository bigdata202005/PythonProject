from flask import Flask, render_template, request, session

# html로 표시하기 위해서 render_template을
# 정보를 받기 위해서 request를
# 세션에 저장하기 위해서 session을 임포트해야 함!!!
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login_form')
def login_form():
    return render_template('login_form.html')  # html을 표시해라!! templates폴더에 위치해야 함


@app.route('/login', methods=['POST'])  # 전송방식 지정
def login_post():
    # 아이디와 비번 비교
    if request.form['username'] == 'admin' and request.form['password'] == '1234':
        # 세션에 저장
        session['logged_in'] = True
        session['username'] = request.form['username']
        return redirect('/template')
    else:
        return '로그인 정보가 맞지 않습니다.'


@app.route('/login', methods=['GET'])  # 전송방식 지정
def login_get():
    return '잘못된 접근'


@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)  # 세션변수 제거
    return redirect('/')


# 주소 복수개 지정 가능
@app.route('/template')
@app.route('/template/<param>')
def template_test(param=None):
    sports = ['야구', '축구', '농구']
    # 템플릿으로 값 전달!!!
    return render_template('template.html', param=param, sports=sports)


app.secret_key = 'qwerty'

if __name__ == '__main__':
    app.run(host='localhost', port=1004)  # 서버 실행
