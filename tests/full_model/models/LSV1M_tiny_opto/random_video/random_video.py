import numpy as np
import os

x = 16
y = 16
duration = 1000
update_interval = 100
n_frames = int(duration / update_interval)

np.random.seed(0)
video = np.random.rand(x, y, n_frames).astype(np.float32)

folder = os.path.dirname(__file__)
file_name = "random_opto_video_1s.npy"
path = os.path.join(folder, file_name)

np.save(path, video)