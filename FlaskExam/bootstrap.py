from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('bootstrap_index.html', title="Bootstrap & Flask")


if __name__ == '__main__':
    app.run()  # 서버 실행
