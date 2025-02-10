# swlag: Calculate lag time constants in shipboard seawater lines

[![Tests](https://github.com/paul-covert/swlag/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/paul-covert/swlag/actions)
[![pypi badge](https://img.shields.io/pypi/v/swlag.svg?style=popout)](https://pypi.org/project/swlag/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<!-- TOC -->

- [swlag](#swlag)
    - [Introduction](#introduction)
    - [Installation](#installation)
    - [Documentation](#documentation)
    - [Basic use](#basic-use)
    - [About](#about)
    - [License](#license)

<!-- /TOC -->

## Introduction

**swlag** is numerical package, written in Python, to calculate the travel time of water from the inlet of a research vessel's underway seawater line to the lab.  

Seawater underway lines are commonly installed on oceanographic research vessels to enable sampling and analyis of surface seawater while the vessel is in transit.  The core measurements are temperature (*T*) and salinity (*S*).  Instruments to measure additional properties, such as chlorophyll-*a* fluorescence and CO<sub>2</sub> partial pressure, are also commonly attached to the seawater line.  When paired with ship's GPS data, maps of these surface seawater properties can be made.

It is important to recognize that it takes a finite amount of time for the seawater to flow from the inlet in the ship's hull to the outlet in the lab.  As a result, the time at which an analysis was made in the lab was made is not the same as the time at which the analyzed water entered the seawater line.  Without correcting for the travel time, a spatial and temporal bias in imparted to the analytical data.  There is also mixing along the seawater line.  Flow rate and total volume of the seawater line impact the extent of mixing.  Knowledge of these parameters can be used to accurately place measurements from the Loop in both geographic and temperature-salinity space.

Originally implemented for use with data collected from "The Loop" aboard the Canadian Coast Guard Vessel *John P. Tully*, this code can be used for any underway seawater line that has temperature sensors at both the inlet and outlet (laboratory) ends of the line.

## Installation

Install from the [Python Package Index](https://pypi.org/project/swlag/):

    pip install swlag

Update an existing installation:

    pip install swlag --upgrade --no-cache-dir

## Documentation

The top-level API is loaded upon importing the swlag package.

```python
    import swlag as lag
```

swlag expects the inlet and lab temperatures to be in a pandas Dataframe with a corresponding time index.  A convenience function is included for loading underway data from Fisheries and Oceans Canada's Institute of Ocean Sciences data archive.

    lag.read_tob(*fname*)

Gaps in data.  Time lag calculations rely on data with a monotonically increasing time coordinate.  There is no functionality built in to the package to adapt to data that aren't monotically increasing.  This will need to be taken care of by the user.  Strategies could include interpolation of the temperature data in cases of short gaps, or splitting the time-series into segments that are continuous in cases of long gaps.

## Basic use

## About

swlag is maintained by [Dr. Paul Covert](https://scholar.google.ca/citations?user=c7BaZ58AAAAJ&hl=en) at Fisheries and Oceans Canada's [Institute of Ocean Sciences](https://science.gc.ca/site/science/en/educational-resources/marine-and-freshwater-sciences/institute-ocean-sciences).

## License

swlag is licensed under the [GNU General Public License version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html).
