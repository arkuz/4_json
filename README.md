# Prettify JSON

This script receives an unformatted JSON file and outputs it in a formatted form to the console. Samples of JSON files, you can download [here](http://rgho.st/8NP5R4phs) and [here](http://rgho.st/7N99xZvYl) or generate on the website [https://www.json-generator.com](https://www.json-generator.com)

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 pprint_json.py test.json
[
  {
    "Cells": {
      "PublicPhone": [
        {
          "PublicPhone": "(495) 777-51-95"
        }
      ], 
      "Name": "Ароматный Мир", 
      "District": "район Кунцево", 
      "OperatingCompany": "Ароматный Мир", 
      "WorkingHours": [
        {
          "Hours": "09:30-22:30", 
          "DayOfWeek": "понедельник"
        }, 
        {
          "Hours": "09:30-22:30", 
          "DayOfWeek": "вторник"
        }, 
        ...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
