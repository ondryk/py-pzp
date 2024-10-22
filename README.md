# PyPZP

Simple cmd line client for great Czech [PZP](https://www.pzp.cz/) heat pumps that allows to read some values. I wrote it just for me to display some graphs related to heating in my house using Prometheus and Grafana (and little piece of PHP that allows Prometheus to scrape data from this tool). It is highly unlikely it would support some other heat pump as I have access to only one. But feel free to use this as base for yourself and your PZP heat pump.

At the moment it is tested with [AWX Economy](https://www.pzpheating.cz/en/economic-air-water-heat-pump/) model with 5.x firmware and software only as it is the only available for me. It displays values in form of CSV line.

Just run it from command line using python3 to get some help.

## Usage
    python3 main.py -h

or get values directly from your pump

    python3 main.py https://10.0.0.2/

## Features
- Read various temperatures from different sensors on PAGE73.XML - outside temperature, heating medium, hot water, water returning from heating system and some others. 

## ToDo
- Support reading of operating states from PAGE15.XML (running compressor, pumps, heating of water, heating etc.)
- Refactor to support multiple pump models via abstracting features and their implementations