from flask import Flask, render_template, request
import numpy as np
import model as model






app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict_salary():
    
    value1= int(request.form.get("store_value"))
    value2= int(request.form.get("items"))
    value3= int(request.form.get("Quantity"))
    value4= int(request.form.get("pending_order"))
   
    output = model.voting.predict(np.array([[value1,value2,value3,value4]]))
    if output[0] == 0:
        return render_template("index.html", prediction="Very Bad")
    elif output[0] == 1:
        return render_template("index.html", prediction="Very Fair")
    elif output[0] == 2:
        return render_template("index.html", prediction="Very Good")
    elif output[0] == 3:
        return render_template("index.html", prediction="Normal")
    
        
    

if __name__ == "__main__":
    app.run(debug=True)
