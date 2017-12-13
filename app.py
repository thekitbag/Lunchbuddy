from flask import Flask, render_template, request, json
import time
import sqlite3
app = Flask(__name__)

db = 'lunchbuddy.sqlite' 


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showEnterDetails')
def showEnterDetails():
    return render_template('recordvisit.html')

@app.route('/enterDetails',methods=['POST','GET'])
def enterDetails():

	_name = request.form['inputName']
	_price = request.form['inputPrice']
	_distance = request.form['inputDistance']

	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("ALTER TABLE restaurants ADD {pr} string;"\
    	.format(pr=_price))
	conn.commit()
	conn.close()
	return json.dumps({'message':'column added successfully !'})		

if __name__ == "__main__":
  app.run()

