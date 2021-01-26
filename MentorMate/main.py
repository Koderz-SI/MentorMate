from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

local_server = True
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


app.run(debug=True)