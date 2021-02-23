from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def test():
    account = request.form['account']
    return render_template('index.html', mesg=account)


if __name__ == '__main__':
    app.run()
