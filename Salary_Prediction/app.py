from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open("salary_model", "rb"))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict_salary():
    new = int(request.form.get("year"))
    print(new)

    # prediction
    output = model.predict(np.array([[new]]))

    return render_template("index.html", prediction=np.round(output[0][0],2))

if __name__ == "__main__":
    app.run(debug=True)
