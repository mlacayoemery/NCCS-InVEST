NCCS
====

Preferred
---------
Prerequisites

*  Open network access for git, pip, and conda
*  Install git and `register <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_ a SSH key with GitHub
*  Anaconda 

1. Clone NCCS InVEST respository

.. code-block:: bash

   mkdir NCCS
   cd NCCS
   git clone git@github.com:mlacayoemery/NCCS-InVEST.git
   cd NCCS-InVEST

Alternatively, you can download and unzip the `repository <https://github.com/mlacayoemery/NCCS-InVEST/archive/refs/heads/main.zip>`_ manually into NCCS/NCCS-InVEST.

2. Setup development environment

.. code-block:: bash

   conda create -n env-invest -c conda-forge "python=3.11" git gdal "numpy<2" libgcc gxx
   conda activate env-invest

   python -m pip install --upgrade pip setuptools wheel
   pip install -r requirements-dev.txt
   pip install .

   invest list
   invest run --help

3. Run test script

   Note: Species abundance rasters must be in named as **pollinator_abundance_[species].tif**. See pre-formatted `NCCS NMDS data <https://drive.google.com/drive/folders/1B-_RKdOOSH9wDz52FIr8-VvgYkySJ3Id>`_.

   *  Copy data into NCCS/sample

.. code-block:: bash

   python NCCS_invest_pollination_U11.py

4. Deactivate development environment

.. code-block:: bash

   conda deactivate

Alternative
-----------
Restore NCCS win-64 Anaconda image...
