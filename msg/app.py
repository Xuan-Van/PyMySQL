from flask import Flask,render_template,request,redirect
import pymysql
import datetime

app = Flask(__name__)
@app.route('/',methods=['get','post'])
def msg():
    db=pymysql.connect(host='localhost',user='root',password='123456',database='msg')
    cursor=db.cursor()
    if request.method=='POST':
        msg=request.values.get('msg')
        now=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        cursor.execute(f'''INSERT INTO content VALUES('{now}','{msg}');''')
        db.commit()
        db.close()
        return redirect('/')
    else:
        cursor.execute('''SELECT 发表时间,发表内容 FROM content ORDER BY 发表时间 DESC LIMIT 10;''')
        data=cursor.fetchall()
        if len(data)==0:
            contents=False
        else:
            contents=[{'time':k.strftime('%y-%m-%d %H:%M:%S'),'content':v} for k,v in data]
        db.close()
        return render_template("index.html",contents=contents)

if __name__ == '__main__':
    app.run(debug = True)