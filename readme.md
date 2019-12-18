# OpenWeatherMap CLI client
Simple lightweight client for weather using OpenWeathewMap API

## Implementation
Because we want client to be lightweight as possible, we are using only few libraries, `json` for parsing API response, `sys` for argument handling and `socket` for creating http request and respond.

## Install
Before running, you are going to need verification API key from [OpenWeatherApp](https://openweathermap.org/appid). 

## How to run
In case of multi-word city name, you need to put city into quotation marks `city="Salt Lake City"` 
### Makefile
`make run api_key=<API_KEY> city=<CITY>`

### As python3 script
`python3 weather.py <API_KEY> <CITY>`
