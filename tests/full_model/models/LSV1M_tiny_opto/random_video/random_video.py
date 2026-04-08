import numpy as np
import os

print("hey")
x = 400
y = 400
duration = 1000
update_interval = 1
n_frames = int(duration / update_interval)

np.random.seed(0)
video = np.random.rand(n_frames, x, y).astype(np.float32)

folder = os.path.dirname(__file__)
file_name = "random_opto_video_1s.npy"
path = os.path.join(folder, file_name)

np.save(path, video)
print(video)