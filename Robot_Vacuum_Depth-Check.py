# ================================
# ROBOT VACUUM DEPTH CHECK
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

raw = np.tile(np.linspace(1.0, 5.0, 60, dtype=np.float32)[:, None], (1, 80))   # the floor: bigger = nearer the robot
raw[:20, :] = 1.0                                              # the far wall of the hallway
cv2.rectangle(raw, (55, 30), (70, 50), 6.0, -1)                # a toy box close to the robot
photo = np.zeros((60, 80, 3), np.uint8)
photo[:, :, 0] = np.arange(80) * 3                             # a test picture: blue = 3 x the column number
WOBBLE = 12
print("Raw depth", raw.shape, "from", raw.min(), "to", raw.max())

# ---------- PART 1: numbers from 0 to 1 ----------
print("\nPART 1: Normalise")
near = (raw - raw.min()) / (raw.max() - raw.min() + 1e-6)
print("Wall:", round(float(near[10, 40]), 2), " Floor:", round(float(near[45, 20]), 2), " Box:", round(float(near[40, 60]), 2))

# ---------- PART 2: where is the obstacle? ----------
print("\nPART 2: Obstacle")
close = near > 0.85
column = np.nonzero(close)[1].mean()
side = "left" if column < 80 / 3 else "middle" if column < 2 * 80 / 3 else "right"
print(f"Close pixels: {int(close.sum())}, on the {side} (column {column:.1f})")

# ---------- PART 3: one frame of the wobble ----------
print("\nPART 3: Parallax")
xs, ys = np.meshgrid(np.arange(80, dtype=np.float32), np.arange(60, dtype=np.float32))
shift = (WOBBLE * (near - 0.5)).astype(np.float32)
moved = cv2.remap(photo, xs + shift, ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
print("Slide of the box:", round(float(shift[40, 60]), 1), " wall:", round(float(shift[10, 40]), 1))
print("The box pixel at column 60 now shows column", round(moved[40, 60, 0] / 3))

# ---------- PART 4: relative, not metres ----------
print("\nPART 4: Relative depth")
raw2 = raw * 3                                                 # the same hallway, another photo: the AI's numbers are 3 times bigger
near2 = (raw2 - raw2.min()) / (raw2.max() - raw2.min() + 1e-6)
print("Raw nearest:", raw.max(), "and", raw2.max(), " Same map after normalising:", bool(np.allclose(near, near2, atol=1e-5)))
