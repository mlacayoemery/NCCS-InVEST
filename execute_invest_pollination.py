import os
base_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(base_path, "data", "sample", "pollination")

import logging
import sys

import natcap.invest.pollination
import natcap.invest.utils

LOGGER = logging.getLogger(__name__)
root_logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt=natcap.invest.utils.LOG_FMT,
    datefmt='%m/%d/%Y %H:%M:%S ')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])

args = {
    'farm_vector_path': os.path.join(input_path, 'farms.shp'),
    'guild_table_path': os.path.join(input_path, 'guild_table.csv'),
    'landcover_biophysical_table_path': os.path.join(input_path, 'landcover_biophysical_table.csv'),
    'landcover_raster_path': os.path.join(input_path, 'landcover.tif'),
    'results_suffix': '',
    'pollinator_abundance_dir': os.path.join(input_path, 'pollinator_abundance'),
    'workspace_dir': os.path.join(base_path, 'output'),
}

if __name__ == '__main__':
    try:
        #output dir passed
        args["workspace_dir"] = os.path.join(base_path,sys.argv[1])
    except IndexError:
        #sticking with default output
        pass
    
    natcap.invest.pollination.execute(args)
