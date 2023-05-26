# Copied from Deepmind colab notebook tutorial.
# https://colab.research.google.com/github/deepmind/dm_control/blob/main/tutorial.ipynb

# %%

import subprocess
if subprocess.run('nvidia-smi').returncode:
    raise RuntimeError(
        'Cannot communicate with GPU. '
        'Make sure you are using a GPU Colab runtime. '
        'Go to the Runtime menu and select Choose runtime type.')

# %%

import numpy as np
import matplotlib.pyplot as plt
# %%
# Testing plotting functionality with a simple parabola
x = np.linspace(-5, 5, 1000)
y = x**2
plt.plot(x, y)
 # %%


# %%


# %%
