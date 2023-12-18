from flask import Flask, render_template, request
import numpy as np
import model as model







app = Flask(__name__)

@app.route("/")
def index():
    return render_template("new_index.html", prediction="")

@app.route("/predict", methods=["POST"])
def predict_salary():
    
    value1= int(request.form.get("Model"))
    value2= int(request.form.get("Manufacturing year"))
    value3= int(request.form.get("Car Kilometers"))
    value4= int(request.form.get("fuelType"))
    value5= int(request.form.get("sellerType"))
    value6= int(request.form.get("transmission"))
    value7= int(request.form.get("owner"))
   
    output = model.rfr.predict(np.array([[value1,value2,value3,value4,value5,value6,value7]]))
    
    
    return render_template("new_index.html", prediction=output[0])
    
    # if output[0] == 0:
    #     return render_template("index.html", prediction="Very Bad")
    # elif output[0] == 1:
    #     return render_template("index.html", prediction="Very Fair")
    # elif output[0] == 2:
    #     return render_template("index.html", prediction="Very Good")
    # elif output[0] == 3:
    #     return render_template("index.html", prediction="Normal")
    
        
    

if __name__ == "__main__":
    app.run(debug=True)
