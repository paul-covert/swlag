# swlag: Calculate lag time constants in shipboard seawater lines

[![Tests](https://github.com/paul-covert/swlag/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/paul-covert/swlag/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<!-- TOC -->

- [swlag](#swlag)
    - [Introduction](#introduction)
    - [Installation](#installation)
        - [With pip](#with-pip)
        - [With conda/mamba](#with-condamamba)
    - [Documentation](#documentation)
    - [Basic use](#basic-use)
    - [About](#about)
    - [License](#license)

<!-- /TOC -->

## Introduction

**swlag** is numerical package designed to calculate the travel time of water from the inlet of a research vessel's underwater seawater line to the lab.  Originally implemented for use with data collected from "The Loop" aboard the Canadian Coast Guard Vessel *John P. Tully*, this code can be used for any underway seawater line that has temperature sensors at both the inlet and outlet (laboratory) ends of the line.

Knowledge of these parameters can be used to accurately place measurements from the Loop in both geographic and temperature-salinity space.

## Installation

### With pip

Install from the [Python Package Index](https://pypi.org/project/swlag/):

    pip install swlag

Update an existing installation:

    pip install swlag --upgrade --no-cache-dir

### With conda/mamba

Install from the [conda-forge channel](https://anaconda.org/conda-forge/swlag):

    conda install swlag -c conda-forge

## Documentation
Gaps in data.  Time lag calculations rely on data with a monotonically increasing time coordinate.  There is no functionality built in to the package to adapt to data that aren't monotically increasing.  This will need to be taken care of by the user.  Strategies could include interpolation of the temperature data in cases of short gaps, or splitting the time-series into segments that are continuous in cases of long gaps.

## Basic use

## About

swlag is maintained by [Dr. Paul Covert](https://scholar.google.ca/citations?user=c7BaZ58AAAAJ&hl=en) at Fisheries and Oceans Canada's [Institute of Ocean Sciences](https://science.gc.ca/site/science/en/educational-resources/marine-and-freshwater-sciences/institute-ocean-sciences).

## License

swlag is licensed under the [GNU General Public License version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html).
