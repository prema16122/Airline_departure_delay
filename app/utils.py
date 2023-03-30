import pickle
import json
import numpy as np
import os 
from flask import Flask,request,render_template
import CONFIG

class Prediction():
    def __init__(self):
        print(os.getcwd())

    def load_raw(self):
        with open(CONFIG.MODEL_PATH,'rb') as model_file: 
            self.model = pickle.load(model_file)
    
        with open(CONFIG.ASSET_PATH,'r') as col_file: 
            self.column_names = json.load(col_file)   
            print(f"we are in load raw")

    def predict_dep_del(self,data):
        self.load_raw()
        self.data = data
        
        user_input = np.zeros(len(self.column_names['Column Names']))
        array = np.array(self.column_names['Column Names'])
        DepTime = self.data['html_dt']
        CRSDepTime = self.data['html_cdt']
        ArrTime = self.data['html_at']
        CRSArrTime = self.data['html_cat']
        FlightNum = self.data['html_flightno']
        ActualElapsedTime = self.data['html_aet']
        CRSElapsedTime = self.data['html_cet']
        AirTime = self.data['html_airtime']
        ArrDelay = self.data['html_arrd']
        Origin = self.data['html_org']
        Dest = self.data['html_dest']
        Distance = self.data['html_dist']
        Diverted = self.data['html_div']
        CarrierDelay = self.data['html_cd']
        WeatherDelay = self.data['html_wd']
        NASDelay = self.data['html_nasd']
        SecurityDelay = self.data['html_sd']
        LateAircraftDelay = self.data['html_lad']

        user_input[0] = int(DepTime)
        user_input[1] = int(CRSDepTime)
        user_input[2] = int(ArrTime)
        user_input[3] = int(CRSArrTime)
        user_input[4] = int(FlightNum)
        user_input[5] = int(ActualElapsedTime)
        user_input[6] = int(CRSElapsedTime)
        user_input[7] = int(AirTime)
        user_input[8] = int(ArrDelay)

        Origin_string = 'Origin_'+Origin
        Origin_index = np.where(array == Origin_string)[0][0]
        user_input[Origin_index] = 1

        dest_string = 'Dest_'+Dest
        dest_index = np.where(array == dest_string)[0][0]
        user_input[dest_index] = 1

        user_input[9] = int(Distance)
        user_input[10] = int(Diverted)
        user_input[11] = int(CarrierDelay)
        user_input[12] = int(WeatherDelay)
        user_input[13] = int(NASDelay)
        user_input[14] = int(SecurityDelay)
        user_input[15] = int(LateAircraftDelay)


        print(f"{user_input=}")
        print(len(user_input))

        dep_delay = self.model.predict([user_input])
        print(f"Predicted depature delay = {dep_delay}")

        return render_template("air_del.html",PREDICT_DELAYE=dep_delay)

if __name__ == "__main__":
     
    pred_obj = Prediction()
    pred_obj.load_raw()

