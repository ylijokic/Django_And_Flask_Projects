from flask import Flask, render_template, url_for, request, redirect
from tracker import AmazonAPI, GenerateReport
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import json

DIRECTORY = 'reports'
CURRENCY = '€'
BASE_URL = "http://www.amazon.de/"

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        req = request.form

        name = req['name']
        min_price = req['min']
        max_price = req["max"]
        filters = {'min': min_price, 'max': max_price}
        print(name, min_price, max_price)

        amazon = AmazonAPI(name, filters, BASE_URL, CURRENCY)
        data = amazon.run()
        obj = GenerateReport(name, filters, BASE_URL, CURRENCY, data)
        report = GenerateReport.get_report(obj)
        print(report)

        return render_template('report.html', dictionary=report, name=name)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(port=4444, debug=True)