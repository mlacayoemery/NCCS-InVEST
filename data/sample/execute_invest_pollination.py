import os
base_path = os.path.dirname(os.path.realpath(__file__))

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
    'farm_vector_path': '', #os.path.join(base_path, 'pollination', 'farms.shp'),
    'guild_table_path': os.path.join(base_path, 'pollination', 'guild_table.csv'),
    'landcover_biophysical_table_path': os.path.join(base_path, 'pollination', 'landcover_biophysical_table.csv'),
    'landcover_raster_path': os.path.join(base_path,'pollination', 'landcover.tif'),
    'results_suffix': '',
    'workspace_dir': os.path.join(base_path, 'output'),
    'pollinator_abundance_dir': os.path.join(base_path,'pollination', 'pollinator_abundance')
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)
