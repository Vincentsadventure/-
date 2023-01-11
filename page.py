import sqlalchemy as db
from flask import Flask, render_template, request
import pandas as pd
import csv
import json

app = Flask(__name__)

# 原網頁
@app.route('/')
def index():
    return render_template('網頁.html')

# submit後的結果
@app.route('/result', methods=['POST']) 
def result():
    df_mrt = pd.read_csv("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_mrt.csv")
    station = request.form['mberAddressDist']
    lat = df_mrt.loc[df_mrt['name'] == station, ["latitude"]]
    lat = lat['latitude'].values[0]
    lng = df_mrt.loc[df_mrt['name'] == station, ["longitude"]]
    lng = lng['longitude'].values[0]
    print(lat)
    
    restaurant = pd.read_csv("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/restaurant.csv")
    # df = df.loc[df["大分類"] == "速食", ["latitude", "longitude"]]
    restaurant = restaurant[["latitude", "longitude"]]
    restaurant = restaurant.iloc[:8000, :]
    restaurant = restaurant.to_dict(orient="records")

    df_conv_s = pd.read_excel("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_conv_s.xlsx")
    df_conv_s = df_conv_s[["latitude", "longitude"]]
    # df_conv_s = df.iloc[:500, :]
    convenience_store = df_conv_s.to_dict(orient="records")

    df_hospital = pd.read_excel("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_hospital.xlsx")
    df_hospital = df_hospital[["latitude", "longitude"]]
    # df_hospital = df_hospital.iloc[:50, :]
    hospital = df_hospital.to_dict(orient="records")

    df_ng_market = pd.read_excel("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_ng_market.xlsx")
    df_ng_market = df_ng_market[["latitude", "longitude"]]
    ng_market = df_ng_market.to_dict(orient="records")

    df_office = pd.read_excel("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_office.xlsx")
    df_office = df_office[["latitude", "longitude"]]
    df_office = df_office.iloc[:4000, :]
    office = df_office.to_dict(orient="records")

    df_school = pd.read_excel("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_school.xlsx")
    df_school = df_school[["latitude", "longitude"]]
    school = df_school.to_dict(orient="records")

    df_td_market = pd.read_excel("C:/Users/student/Desktop/網頁模板/startbootstrap-agency-gh-pages/static/data/df_td_market.xlsx")
    df_td_market = df_td_market[["latitude", "longitude"]]
    market = df_td_market.to_dict(orient="records")
    
    return render_template("result.html", page_header="推薦結果", response=restaurant, response1=convenience_store, response2=hospital, response3=ng_market, response4=office, response5=school, response6=market,
    lat=lat, lng=lng)
   
if __name__=="__main__":
    app.run(debug=True)