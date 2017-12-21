from flask import Flask, jsonify, render_template, request, json
import time
import sqlite3
app = Flask(__name__)

db = 'lunchbuddy.sqlite' 

#routes for displaying pages

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showAddDestination')
def showAddDestination():
    return render_template('adddestination.html')

@app.route('/showRecordVisit')
def showRecordVisit():
    return render_template('recordvisit.html')

@app.route('/showFindLunch')
def showFindLunch():
    return render_template('findlunch.html')

#routes for button actions

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
	c.execute("INSERT INTO restaurants (Name, Price, Distance, Takeaway, 'Eat in', Healthiness, 'Gluten Free Option') VALUES (?,?,?,?,?,?,?);", (_name, _price, _distance, _takeaway, _eatin, _healthiness, _gluten))
	conn.commit()
	conn.close()
	return json.dumps({'message':'New Restaurant added successfully !'})		



@app.route('/recordVisit',methods=['POST','GET'])
def recordVisit():
	#get details from form
	_restaurant = request.form['inputRestaurant']
	_pricePaid = request.form['inputPricePaid']
	_dish = request.form['inputDish']
	_rating = request.form['inputRating']
	_date = "19/12/2017"

	#send details from the form to the db
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("INSERT INTO visits ('Date', Restaurant, Dish, 'Price Paid', Rating) VALUES (?,?,?,?,?);", (_date, _restaurant, _pricePaid, _dish, _rating))
	conn.commit()
	conn.close()
	return json.dumps({'message':'Visit Recorded successfully !'})



@app.route('/findLunch',methods=['POST','GET'])
def findLunch():	
	
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT * FROM restaurants")
	all_rows = c.fetchall()
	return jsonify(all_rows)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
	

if __name__ == "__main__":
  app.run()



