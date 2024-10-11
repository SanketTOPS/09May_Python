from flask import Flask, render_template,request,redirect
import sqlite3

app=Flask(__name__)


#Database Connection
def dbcon():
    try:
        db=sqlite3.connect('flaskdb.db')
        print("Database Connected/Created!")
        return db
    except Exception as e:
        print(e)


#Table Created
def tbl_create():
    db=dbcon()
    try:
        create_tbl="create table studinfo(id integer primary key autoincrement, name text, city text)"
        db.execute(create_tbl)
        print("Table created!")
    except Exception as e:
        print(e)

@app.route('/', methods=['GET','POST'])
def index():
    dbcon()
    tbl_create()
    if request.method=='POST':
        nm=request.form['name']
        ct=request.form['city']

        newdata=f"insert into studinfo(name,city)values('{nm}','{ct}')"
        db=dbcon()
        db.execute(newdata)
        db.commit()
        print("Record inserted!")
    else:
        print("Error!")

    return render_template('index.html')

@app.route('/showdata')
def showdata():
    db=dbcon()
    cr=db.cursor()
    try:
        showdt="select * from studinfo"
        cr.execute(showdt)
        data=cr.fetchall()
    except Exception as e:
        print(e)
    return render_template('showdata.html',data=data)



if __name__=='__main__':
    app.run(debug=True)