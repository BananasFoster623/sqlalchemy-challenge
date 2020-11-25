# Import all dependencies

from flask import Flask, jsonify
# Leaving out matplotlib dependencies since we don't need them
# %matplotlib inline
# from matplotlib import style
# style.use('fivethirtyeight')
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Create the database instance

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
# Base.classes.keys() ----- don't need this since we verified it works in the jupyter notebook
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    return ("Hawaii Weather Data API<br/><br/>"
            "Available Routes:<br/><br/>"
            "/api/v1.0/precipitation<br/>"
            "/api/v1.0/stations<br/>"
            "/api/v1.0/tobs<br/>"
            "/api/v1.0/start<br/>"
            "/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return

@app.route("/api/v1.0/stations")
def stations():
    return

@app.route("/api/v1.0/tobs")
def temp_observations():
    return

@app.route("/api/v1.0/<start>")
def temp_query1():
    return

@app.route("/api/v1.0/<start>/<end>")
def temp_query2():
    return

if __name__ == "__main__":
    app.run(debug=True)
