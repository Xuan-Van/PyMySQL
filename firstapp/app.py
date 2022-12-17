from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "hello world"

@app.route("/reg")
def reg():
    return render_template("form.html")

@app.route("/regin",methods=["POST","GET"])
def regin():
    db=pymysql.connect(host='localhost',user='root',password='123456',charset='utf8',db='reg')
    xh=request.args.get("学号")
    xm=request.args.get("姓名")
    mm=request.args.get("密码")
    cursor=db.cursor()
    sql=f"insert into xs values ('{xh}','{xm}','{mm}');"
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return "插入成功"

if __name__ == '__main__':
    app.run(debug = True)