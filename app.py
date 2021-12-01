from logging import debug
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import testemail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Login(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}: {self.email}"

@app.route("/",methods=['GET','POST'])
def main():
    
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        present = Login.query.filter_by(email=email).first()
        if present == None:
            password = request.form['password']
            info = Login(name=name,email=email,password=password)
            db.session.add(info)
            db.session.commit()
            testemail.sendto(email,name)

        else:
            return render_template("index.html",flag=-1)
    allmail = Login.query.all()
    
    num = 0
    return render_template("index.html",allLogins=allmail,flag=num)

@app.route("/login")
def login():
    return render_template('login.html')
    
@app.route("/login/alert",methods=['GET','POST'])
def check():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        try:
            actual_mail = Login.query.filter_by(email=email).first()
            if actual_mail.email==email and password==actual_mail.password:
                num = 1
        
                return render_template('index.html',flag=num,name=actual_mail.name)
            else:
                num = 2
                return render_template('index.html',flag=num)
        except:
            
            num = 3
            
            return render_template('index.html',flag=num)

    redirect("/login")




if __name__=='__main__':
    app.run(debug=False)
