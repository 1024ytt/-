from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])#登陆页面，用户名密码已经写死：root,12345
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username=='root' and password=='12345':
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/index')#首页页面
def index():
    return render_template("index.html")
@app.route('/index')
def home():
    return index();

@app.route('/1')#明文离线检测
def movie():
    datalist=[];
    conn=sqlite3.connect("movie.db")
    cur=conn.cursor()
    sql='''select * from movie250'''
    data=cur.execute(sql)
    for item in data:
        datalist.append(item);
    cur.close()
    conn.close()
    return render_template("/1.html",movies=datalist);
@app.route('/2')#明文在线页面解析
def score():
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = '''select score,count(score) from movie250 group by score'''#从数据库里面查找score，以及score的个数
    data = cur.execute(sql)
    score=[] #表示评分的列表
    number=[] #表示评分种类的数量
    for item in data:
        score.append(str(item[0]))
        number.append(item[1])
    cur.close()
    conn.close()
    return render_template("/2.html",score=score,number=number);

@app.route('/3')#密文离线解析
def team():
    return render_template("/3.html");

@app.route('/4')#密文在线解析
def word():
    return render_template("/4.html");

@app.route('/5')#阻断 IP 列表
def five():
    return render_template("/5.html");

if __name__ == '__main__':
    app.run(debug=True)
