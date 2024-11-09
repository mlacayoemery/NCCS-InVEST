#!/usr/bin/env bash

#conda env remove -n natcap -y
if ! conda env list | grep "natcap" >/dev/null 2>&1; then
   git checkout natcap
   conda create -n natcap -c conda-forge "python=3.11" git gdal "numpy<2" abseil-cpp -y
   conda run -n natcap --live-stream python -m pip install --upgrade pip setuptools wheel
   conda run -n natcap --live-stream pip install -r requirements-dev.txt
   conda run -n natcap --live-stream pip install .
fi
conda run -n natcap --live-stream python execute_invest_pollination.py output/env_natcap

#conda env remove -n v1 -y
if ! conda env list | grep "v1" >/dev/null 2>&1; then
   git checkout v1
   conda create -n v1 -c conda-forge "python=3.11" git gdal "numpy<2" abseil-cpp -y
   conda run -n v1 --live-stream python -m pip install --upgrade pip setuptools wheel
   conda run -n v1 --live-stream pip install -r requirements-dev.txt
   conda run -n v1 --live-stream pip install .
fi
conda run -n v1 --live-stream python execute_invest_pollination.py output/env_v1
