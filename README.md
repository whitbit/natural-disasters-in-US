# US Natural Disasters Data

This project is a simple REST API sharing US environmental disaster data between 1950-2017 from [FEMA](https://FEMA.gov/). For the purpose of displaying data, the project only supports GET requests at the moment. Please find the UI deployed at [https://naturaldisasters.herokuapp.com/](https://naturaldisasters.herokuapp.com/).

## Table of Contents
* [GET Requests](#getrequest)
* [Run locally on machine](#run)


### <a name="getrequests"></a>GET Requests
*/api/events*

Returns events between two dates of specified event types.

**Required Arguments**
* from (YYYY-MM-DD)
* to (YYYY-MM-DD)
* event_type


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
* Go to [localhost:5000](http://localhost:5000/) to see the home page


