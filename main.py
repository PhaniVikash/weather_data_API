from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)

stations=pd.read_csv("data_small/stations.txt",skiprows=17)
stations=stations[["STAID",'STANAME                                 ']]


@app.route("/")
def home():
    return render_template("home.html",data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filepath="data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filepath,skiprows=20,parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    return {"date":date,
            "station":station,"temperature":temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    result=df.to_dict(orient='records')
    return result

@app.route("/annual/api/v1/<station>/<year>")
def yearly(station,year):
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    df['    DATE']=df['    DATE'].astype(str)
    result=df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == '__main__':
    app.run(debug=True,port=5001)
