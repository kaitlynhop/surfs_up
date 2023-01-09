# import dependencies
# analysis
import datetime as dt
import numpy as np
import pandas as pd
# SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
# Flask
from flask import Flask, jsonify

# connection to SQLite 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect schema of tables into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Store class variables to reference table-data
Measurement = Base.classes.measurement
Station = Base.classes.station

# Session link to DB file
session = Session(engine)

# Instantiate flask app
app = Flask(__name__)

# Defining root route
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Get date 1 year from 8/23/17
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp) \
            .filter(Measurement.date >= prev_year).all()
    # create dictionary to hold percipitation and data
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Station Route
@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    # flatten array and convert to list
    stations = list(np.ravel(results))
    # set json object to stations: value
    return jsonify(stations=stations)

# Temperature Route
@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active = session.query(Measurement.station, func.count(Measurement.station)) \
            .group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()
    # query to get temp obs for the most active
    results = session.query(Measurement.tobs).filter(Measurement.station == most_active[0]) \
            .filter(Measurement.date >= prev_year).all()
    # flatten array
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Statistics Route - temp data by user inputed date
@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')
# set default to None - to remove filters
def stats(start=None, end=None):
    # list variable to hold query
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    # if no end date supplied
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# run as script from app
if __name__ == '__main__':
    app.run(debug=True)
