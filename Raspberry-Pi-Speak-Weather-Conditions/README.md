Have your Raspberry Pi speak the weather forecast
========================================

This is a simple parser for the JSON output returned by the Weather Underground API to create a string that can be used by a TTS engine to speak the current weather conditions and forecast for the day.


## Requirements:

* **A Raspberry Pi** - Actually this code should run fine on any Linux or Mac OS X system
* **Weather Underground API credentials** - http://www.wunderground.com/weather/api/
* **A TTS solution such as the one described in** - 
  https://github.com/VidereResearch/Python/tree/master/Pyvona-Example-Raspberry-Pi-Text-to-Speech-TTS

## Using the Weather Underground API

The `pi-weather-underground-speak.py` script that will make a request to the Weather Underground API for the nearest location around you and create a human understandable string that can be passed to a TTS engine.

    Obviously, enter your own API key, and also set the location variable to the correct location:
    my_location = 'HI/Kihei'

    The example comes with TTS disabled, uncomment the TTS lines and the import statement to enable!
