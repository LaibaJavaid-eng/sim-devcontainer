#!/bin/bash

USER=$(whoami)
mkdir -p /home/$USER/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/$USER/miniconda3/miniconda.sh
bash /home/$USER/miniconda3/miniconda.sh -b -u -p /home/$USER/miniconda3
rm -rf /home/$USER/miniconda3/miniconda.sh
/home/$USER/miniconda3/bin/conda init bash
echo "Build completed"