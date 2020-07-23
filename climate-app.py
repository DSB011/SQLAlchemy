import numpy as np
import pandas as pd
import datetime as dt


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session= Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################


@app.route("/")
def home_page():
    
    return (
        
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"-------------------------------------------<br/>"
        f"-----data_search (yyyy-mm-dd)<br/>"
        f"/api/v1.0/start_date <br/>"
        f"/api/v1.0/start_date/end_date <br/>"
        
    )

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.name).all()
 # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/precipitation")
def precipitation():
    recent_date = (session.query(Measurement.date).order_by(Measurement.date.desc()).first())
    recent_date = list(np.ravel(recent_date))[0]

    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    recent_year = int(dt.datetime.strftime(recent_date, '%Y'))
    recent_month = int(dt.datetime.strftime(recent_date,'%m'))
    recent_day = int(dt.datetime.strftime(recent_date,'%d'))

    previous_year = dt.date(recent_year,recent_month,recent_day) - dt.timedelta(days=365)
    previous_year = dt.datetime.strftime(previous_year, '%Y-%m-%d')
    
    results = session.query(Measurement.date, Measurement.prcp, Measurement.station).filter(Measurement.date > previous_year).order_by(Measurement.date).all()
                    

    precipitation_data = []
    for result in results:
            precipitation_dict = {result.date : result.prcp}
            precipitation_data.append(precipitation_dict)
    return jsonify(precipitation_data)

@app.route("/api/v1.0/tobs")
def tobs():
    
    recent_date = (session.query(Measurement.date).order_by(Measurement.date.desc()).first())
    recent_date = list(np.ravel(recent_date))[0]

    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    recent_year = int(dt.datetime.strftime(recent_date, '%Y'))
    recent_month = int(dt.datetime.strftime(recent_date,'%m'))
    recent_day = int(dt.datetime.strftime(recent_date,'%d'))

    previous_year = dt.date(recent_year,recent_month,recent_day) - dt.timedelta(days=365)
    previous_year = dt.datetime.strftime(previous_year, '%Y-%m-%d')
    results = (session.query(Measurement.date, Measurement.tobs, Measurement.station).\
                   filter(Measurement.date > previous_year).order_by(Measurement.date).all())

    return jsonify(results)

@app.route("/api/v1.0/<start>")
def start_temp(start):
    
    Start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= Start_date).all()
    session.close()
    # Convert list of tuples into normal list
    result = list(np.ravel(temp_data))

    return jsonify(temp_data)
 
@app.route("/api/v1.0/<start>/<end>")
def trip_date(start, end):
    
    sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    start = dt.datetime.strptime(start, "%Y-%m-%d")
    end = dt.datetime.strptime(end, "%Y-%m-%d")

    results = (session.query(*sel).\
        filter(func.strftime("%Y-%m-%d", Measurement.date) >= start).\
        filter(func.strftime("%Y-%m-%d", Measurement.date) <= end).group_by(Measurement.date).all())
        
    dates =[]
    for result in results:
        start_end_dict = {}
        start_end_dict['Date'] = result[0]
        start_end_dict["Min Temp"] = result[1]
        start_end_dict["Avg Temp"] = result[2]
        start_end_dict["Min Temp"] = result[3]
        dates.append(start_end_dict)

    return jsonify(dates)



    





if __name__ == '__main__':
    app.run(debug=True)
    





    

