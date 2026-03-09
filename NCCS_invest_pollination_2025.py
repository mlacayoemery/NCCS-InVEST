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

# neuer Output-Ordner
output_path = r"O:\Data-Work\27_Natural_Resources-RE\271_KLIM_Work\CC_Impacts\NCCS\Data\M2b_Pollination\InVEST_2026\cherry"

args = {
    'farm_vector_path': '',

    # INPUT DATEN (bleiben im alten Ordner)
    'guild_table_path': os.path.join(base_path, 'InVEST_2026_cherry_present', 'guild_CH_present_cherry.csv'),
    'landcover_biophysical_table_path': os.path.join(base_path, 'InVEST_2026_cherry_present', 'pollination_bptable_ds25.csv'),
    'landcover_raster_path': os.path.join(base_path, 'InVEST_2026_cherry_present', 'LU-CH_2018all.tif'),
    'pollinator_abundance_dir': os.path.join(base_path, 'InVEST_2026_cherry_present', 'pollinator_abundance'),

    # OUTPUT
    'results_suffix': '',
    'workspace_dir': output_path,
}
if __name__ == '__main__':
    natcap.invest.pollination.execute(args)
