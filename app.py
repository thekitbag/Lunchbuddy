from flask import Flask, render_template, request, json
import time
import sqlite3
app = Flask(__name__)

db = 'H:\Coding\LunchBuddy\lunchbuddy.sqlite' 


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showEnterDetails')
def showEnterDetails():
    return render_template('recordvisit.html')

@app.route('/enterDetails',methods=['POST'])
def enterDetails():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('UPDATE restaurants SET Name = "Katiii roll" WHERE Name = "Katiii roll"');
    conn.commit()
    conn.close() 	

if __name__ == "__main__":
  app.run()

