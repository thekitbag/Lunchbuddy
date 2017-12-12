from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/recordvisit')
def showSignUp():
    return render_template('recordvisit.html')


@app.route('/enterLunchDetails',methods=['POST'])
def enterLunchDetails():
 
    # read the posted values from the UI
    _restaurant = request.form['inputRestaurant']    
 
    # validate the received values
    if _restaurant:
        return json.dumps({'html':'<span>All fields are good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
  app.run()

