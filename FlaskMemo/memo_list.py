import socket
from flask import Flask, render_template, request
from werkzeug.utils import redirect

from Memo.memo_service import Memo_Service

app = Flask(__name__)  # 어플리케이션 생성


@app.route('/')
@app.route('/index')  # 웹상의 주소 1개를 만들고
def index():
    current_page = 1
    page_size = 10
    block_size = 10
    try:
        parameter_dict = request.args.to_dict()  # 파라메터를 dict로 받기
        current_page = int(parameter_dict['p'])
        page_size = int(parameter_dict['s'])
        block_size = int(parameter_dict['b'])
    except Exception as e:  # 키가 없으면 에러발생해서 기본값
        print("에러발생 :", e)
    print("받은 내용 :", current_page, page_size, block_size)
    service = Memo_Service()
    paging = service.select_list(current_page, page_size, block_size)
    print(paging)
    return render_template('index.html', paging=paging)


@app.route('/insert', methods=['GET'])  # 웹상의 주소 1개를 만들고
def insert_get():
    return redirect('/')


@app.route('/insert', methods=['POST'])  # 웹상의 주소 1개를 만들고
def insert_post():
    memo_dict = {}
    memo_dict['name'] = request.form['name']
    memo_dict['password'] = request.form['password']
    memo_dict['content'] = request.form['content']
    memo_dict['ip'] = socket.gethostbyname(socket.gethostname()) # ip알아내기
    memo_dict['p'] = request.form['p']
    memo_dict['s'] = request.form['s']
    memo_dict['b'] = request.form['b']
    service = Memo_Service()
    service.insert(memo_dict=memo_dict)
    # redirect(url_for(~))로 처리 할수 있고
    # 주의할점은 redirect할 method 명으로 처리 한다는것이다.
    # redirect(url_for('login2'))
    return redirect('/?p=' + memo_dict['p'] + '&s=' + memo_dict['s'] + '&b=' + memo_dict['b'])


@app.route('/edit', methods=['GET'])
def edit_get():
    return redirect('/')


@app.route('/edit', methods=['POST'])
def edit_post():
    memo_dict = {}
    memo_dict['idx'] = request.form['idx']
    memo_dict['password'] = request.form['password']
    memo_dict['content'] = request.form['content']
    memo_dict['ip'] = socket.gethostbyname(socket.gethostname())
    memo_dict['p'] = request.form['p']
    memo_dict['s'] = request.form['s']
    memo_dict['b'] = request.form['b']
    service = Memo_Service()
    service.update(memo_dict=memo_dict)
    return redirect('/?p=' + memo_dict['p'] + '&s=' + memo_dict['s'] + '&b=' + memo_dict['b'])


@app.route('/delete', methods=['GET'])
def delete_get():
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_post():
    memo_dict = {}
    memo_dict['idx'] = request.form['idx']
    memo_dict['password'] = request.form['password']
    memo_dict['p'] = request.form['p']
    memo_dict['s'] = request.form['s']
    memo_dict['b'] = request.form['b']
    service = Memo_Service()
    service.delete(memo_dict=memo_dict)
    return redirect('/?p=' + memo_dict['p'] + '&s=' + memo_dict['s'] + '&b=' + memo_dict['b'])


if __name__ == '__main__':
    app.run()  # 서버 실행
