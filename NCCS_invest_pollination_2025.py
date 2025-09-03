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
    'farm_vector_path': '',
    'guild_table_path': os.path.join(base_path, 'InVEST_2025_apple_pesenc', 'guild_CH_presence_apple.csv'),
    'landcover_biophysical_table_path': os.path.join(base_path, 'InVEST_2025_apple_pesenc', 'pollination_bptable_ds25.csv'),
    'landcover_raster_path': os.path.join(base_path,'InVEST_2025_apple_pesenc', 'LU-CH_2018all.tif'),
    'results_suffix': '',
    'workspace_dir': os.path.join(base_path, 'output'),
    'pollinator_abundance_dir': os.path.join(base_path,'InVEST_2025_apple_pesenc', 'pollinator_abundance')
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)
