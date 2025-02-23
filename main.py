from flask import Flask,render_template

app=Flask("Vikash_website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temperature = 26
    return {"date":date,
            "station":station,"temperature":temperature}

app.run(debug=True)
