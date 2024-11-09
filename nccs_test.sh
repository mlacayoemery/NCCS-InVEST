#!/usr/bin/env bash

git checkout main

#conda env remove -n natcap -y
if ! conda env list | grep "natcap" >/dev/null 2>&1; then
   conda create -n natcap -c conda-forge "python=3.11" git gdal "numpy<2" abseil-cpp -y
   conda run -n natcap --live-stream python -m pip install natcap.invest==3.14.2
fi
conda run -n natcap --live-stream python execute_invest_pollination.py output/env_natcap

mkdir -p data/sample/pollination/pollinator_abundance
cp --update=none output/env_natcap/pollinator_abundance_apis_spring.tif data/sample/pollination/pollinator_abundance/pollinator_abundance_apis.tif
cp --update=none output/env_natcap/pollinator_abundance_apis2_spring.tif data/sample/pollination/pollinator_abundance/pollinator_abundance_apis2.tif
cp --update=none output/env_natcap/pollinator_abundance_bombus_spring.tif data/sample/pollination/pollinator_abundance/pollinator_abundance_bombus.tif
cp --update=none output/env_natcap/pollinator_abundance_bombus2_spring.tif data/sample/pollination/pollinator_abundance/pollinator_abundance_bombus2.tif

#conda env remove -n v1 -y
if ! conda env list | grep "v1" >/dev/null 2>&1; then
   git checkout v1
   
   conda create -n v1 -c conda-forge "python=3.11" git gdal "numpy<2" abseil-cpp -y
   conda run -n v1 --live-stream python -m pip install --upgrade pip setuptools wheel
   conda run -n v1 --live-stream pip install -r requirements-dev.txt
   conda run -n v1 --live-stream pip install .

   git checkout main
fi
conda run -n v1 --live-stream python execute_invest_pollination.py output/env_v1
