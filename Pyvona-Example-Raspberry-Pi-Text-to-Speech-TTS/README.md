Raspberry Pi Text to Speech (TTS)
========================================

Google has one of the best sounding voices out there, but it routinely blocks API calls from users who are suspected to make calls from automated systems, which makes it impractical and unreliable.

Ivona is a very suitable replacement, and currently offers equaly (if not better) sounding voices and a clear and generous free usage tier. For more  details, see https://www.ivona.com/us/ to sign-up for your free account.


## Requirements:

* **A Raspberry Pi** - Actually this code should run fine on any Linux or Mac OS X system
* **Ivona (now an AWS company) credentials** - 
* **Pivona** - `pip install pivona` a Python library for using the Ivona API
  

## Using the Ivona API

The `tts.py` script is a small script that can be imported to easily speech-enable any of your Pithon scripts.

`tts_example.py` provides an example of how to use the `tts.py` script.


`tts2mp3.py` is a slight twist on the `tts.py` script that allows you to save the spoken text as an .mp3 file.