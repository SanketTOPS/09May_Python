from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__) #app initlization

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///newdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dbapp=SQLAlchemy(app) #database initlization

#Db Model
class studinfo(dbapp.Model):
    id=dbapp.Column(dbapp.Integer, primary_key=True)
    name=dbapp.Column(dbapp.String)
    city=dbapp.Column(dbapp.String)


def db_create():
    dbapp.create_all()


@app.route('/',methods=['GET','POST'])
def index():
    db_create()
    if request.method=='POST':
        nm=request.form['name']
        ct=request.form['city']

        newData=studinfo(name=nm,city=ct)
        dbapp.session.add(newData)
        dbapp.session.commit()
        print("Record inserted!")
    else:
        print("Error!")
    return render_template('index.html')

@app.route('/showdata')
def showdata():
    data=studinfo.query.all()
    return render_template('showdata.html',data=data)

if __name__=='__main__':
    app.run(debug=True)