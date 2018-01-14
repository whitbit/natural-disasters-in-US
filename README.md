#US Natural Disasters Data (1950-2017)

This project is a simple REST API sharing US environmental disaster data from [FEMA](https://FEMA.gov/). For the purpose of only displaying data, the project only supports GET requests at the moment.

## Table of Contents
* [GET Requests](#getrequest)
* [Run locally on machine](#run)


### <a name="getrequests"></a>GET Requests
*/api/events*
Returns events between two dates of specified event types.

**Required Arguments**
from - The start date (YYYY-MM-DD)
to - The end date (YYYY-MM-DD)
event_type


### <a name="run"></a>Run Locally On Machine

* Set up and activate a python virtualenv
    * `pip install -r requirements.text`
* Run PostgreSQL and create a new database named 'disaster_events':
    * `psql`
    * `createdb disaster_events`
* Seed database
    * `python seed.py`
* Start up the flask server
    * `python server.py`
* Go to [localhost:3000](http://localhost:3000/) to see the home page


