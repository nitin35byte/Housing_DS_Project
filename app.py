
from logging import raiseExceptions
import sys
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():

    try:
        raiseExceptions("we are testing custom exception")
    except Exception as e:
       housing= HousingException(e,sys)
       logging.info(housing.error_message)
       logging.info("we are testing logging module")
       
    return "Starting machine learning project"

if __name__== "__main__":
    app.run(debug=True)

