from flask import Flask, render_template
import random

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',nm="Sanket")

@app.route('/about')
def about():
    num=random.randint(1111,9999)
    return render_template('about.html',num=num)





if __name__=='__main__':
    app.run(debug=True)