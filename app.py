from flask import Flask, render_template, request, json
import time
import sqlite3
app = Flask(__name__)

db = 'lunchbuddy.sqlite' 


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showAddDestination')
def showAddDestination():
    return render_template('adddestination.html')

@app.route('/enterDetails',methods=['POST','GET'])
def enterDetails():
	#get details from form
	_name = request.form['inputName']
	_price = request.form['inputPrice']
	_distance = request.form['inputDistance']
	_takeaway = request.form['inputTakeaway']
	_eatin = request.form['inputEatIn']
	_healthiness = request.form['inputHealthiness']
	_gluten = request.form['inputGluten']

	#send details from the form to the db
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("INSERT INTO restaurants (Name, Price, Distance, Takeaway, 'Eat in', Healthiness, Gluten) VALUES (?,?,?,?,?,?,?);", (_name, _price, _distance, _takeaway, _eatin, _healthiness, _gluten))
	conn.commit()
	conn.close()
	return json.dumps({'message':'column added successfully !'})		

if __name__ == "__main__":
  app.run()



