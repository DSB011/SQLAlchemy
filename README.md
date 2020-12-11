# SQLAlchemy - Surfs Up!

## Overview:
Decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area.

<img src = "https://github.com/DSB011/SQLAlchemy/blob/master/Images/surfs-up%20(1).png"><br>

## Step 1 - Climate Analysis and Exploration:
Used Python and SQLAlchemy to do basic climate analysis and data exploration of climate database. All of the following analysis are done using SQLAlchemy ORM queries, Pandas, and Matplotlib.<br>
* Used the provided starter notebook and hawaii.sqlite files to complete the climate analysis and data exploration.
* Choose a start date and end date for the trip. The vacation range is approximately 3-15 days total.
* Used SQLAlchemy create_engine to connect to the sqlite database.
* Used SQLAlchemy automap_base() to reflect the tables into classes and saved a reference to those classes called Station and Measurement.

## Precipitation Analysis:

* Designed a query to retrieve the last 12 months of precipitation data.
* Selected only the date and prcp values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by date.
* Plotted the results using the DataFrame plot method.
* Used Pandas to print the summary statistics for the precipitation data.<br><br>
<img src = "https://github.com/DSB011/SQLAlchemy/blob/master/Images/download.png"> <br>

## Station Analysis:

* Designed a query to calculate the total number of stations.
* Designed a query to find the most active stations.
    * Listed the stations and observation counts in descending order.
    * Which station has the highest number of observations?
    * Hint: Used functions such as func.min, func.max, func.avg, and func.count in the queries.
* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
    * Filtered by the station with the highest number of observations.
    * Plotted the results as a histogram with bins=12.
<img src = "https://github.com/DSB011/SQLAlchemy/blob/master/Images/Station.png">

## Step 2 - Climate App:
Designed a Flask API based on the queries that was just developed.
  * Used Flask to create your routes.
  
## Routes:
* /
  * Home page.
  * Listed all routes that are available.

* /api/v1.0/precipitation
   * Converted the query results to a dictionary using date as the key and prcp as the value.
   * Returned the JSON representation of the dictionary.

* /api/v1.0/stations
    * Returned a JSON list of stations from the dataset.

* /api/v1.0/tobs
    * Query the dates and temperature observations of the most active station for the last year of data.
    * Returned a JSON list of temperature observations (TOBS) for the previous year.

* /api/v1.0/<start> and /api/v1.0/<start>/<end>
    * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    * When given the start only, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    * When given the start and the end date, calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Bonus: Other Recommended Analysis:

## Temperature Analysis I:
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
* Used pandas's read_csv() to perform this portion.
* Identified the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
* Used the t-test to determine whether the difference in the means. Will you use a paired t-test, or an unpaired t-test? Why?

## Temperature Analysis II:
* The starter notebook contained a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
* Used the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
* Plotted the min, avg, and max temperature from your previous query as a bar chart.
    * Used the average temperature as the bar height.
    * Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).<br><br>
<img src = "https://github.com/DSB011/SQLAlchemy/blob/master/Images/Bonus.png"> <br>

## Daily Rainfall Average:

* Calculated the rainfall per weather station using the previous year's matching dates.
* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.
* Created a list of dates for the trip in the format %m-%d. Used the daily_normals function to calculate the normals for each date string and appended the results to a list.
* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.
* Used Pandas to plot an area plot (stacked=False) for the daily normals.<br><br>
<img src = "https://github.com/DSB011/SQLAlchemy/blob/master/Images/Daily_rainfall.png"><br>

## Tech Environment Used:

SQLAlchemy ORM queries, Pandas, Juputer Notebook, Matplotlib.








