# Copied from Deepmind colab notebook tutorial.
# https://colab.research.google.com/github/deepmind/dm_control/blob/main/tutorial.ipynb

# %%

import subprocess
if subprocess.run('nvidia-smi').returncode:
    raise RuntimeError(
        'Cannot communicate with GPU. '
        'Make sure you are using a GPU Colab runtime. '
        'Go to the Runtime menu and select Choose runtime type.')
