from flask import Flask,render_template,request
from app.utils import Prediction
import CONFIG

app=Flask(__name__)
@app.route('/')
def start():
    return render_template("air_del.html")

@app.route('/predict',methods=["POST","GET"])
def predict_dep_del():
    data=request.form
    pred_obj = Prediction()
    predicted_depdel = pred_obj.predict_dep_del(data)
    print(predicted_depdel)
    
    return predicted_depdel


if __name__ == "__main__":
    app.run(CONFIG.HOST_NAME,CONFIG.PORT_NUMBER,debug=True)