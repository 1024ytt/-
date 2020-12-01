from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username=='root' and password=='12345':
        return render_template('index.html')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


