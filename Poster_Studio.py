
# ================================
# POSTER STUDIO
# ================================

# ---------- SETUP (given to you) ----------
import numpy as np

rng = np.random.default_rng(6)
photo = rng.integers(0, 256, (6, 8, 3)).astype(np.uint8)
matte = np.zeros((6, 8))
matte[1:6, 3:6] = 1.0
matte[1:6, 2] = 0.5

STYLES = {
    name: np.random.default_rng(seed).normal(0, 1, (1, 1, 1, 100)).astype(np.float32)
    for name, seed in [("Comic", 1), ("Dream", 2), ("Neon", 3)]
}

TIMES = {
    "camera picture": 0.033,
    "painting": 0.18,
    "cut-out": 0.1
}


def poster_ai(content_image, style_numbers):
    if content_image.ndim != 4:
        raise ValueError(f"Invalid rank for input: content_image Got: {content_image.ndim} Expected: 4")
    if content_image.max() > 1:
        raise ValueError(f"content_image must be 0 to 1, got numbers up to {content_image.max():.0f}")

    colour = 1 / (1 + np.exp(-style_numbers.reshape(100)[:3]))
    return content_image * 0.4 + colour * 0.6


print("Photo:", photo.shape, " styles:", list(STYLES))

# ---------- PART 1: picture in ----------
print("\nPART 1: Ready for the AI")

x = photo[:, :, ::-1].astype(np.float32) / 255.0
x = x[np.newaxis, ...]

print("Shape:", x.shape)
print("Minimum:", round(float(x.min()), 2))
print("Maximum:", round(float(x.max()), 2))

# ---------- PART 2: one network, any style ----------
print("\nPART 2: Three posters, one AI")

posters = {}

for name, style in STYLES.items():
    result = poster_ai(x, style)[0]
    poster = np.clip(np.round(result[:, :, ::-1] * 255), 0, 255).astype(np.uint8)

    posters[name] = poster

    averages = np.round(poster.mean(axis=(0, 1))).astype(int)
    print(name, "Shape:", poster.shape, "Average BGR:", averages)

# ---------- PART 3: keep the student real ----------
print("\nPART 3: Dream poster, student kept real")

dream = posters["Dream"]

alpha = matte[:, :, np.newaxis]

final = (
    photo.astype(np.float32) * alpha
    + dream.astype(np.float32) * (1 - alpha)
)

final = np.clip(final, 0, 255).astype(np.uint8)

print("Room pixel:")
print("Final:", final[0, 0], "Photo:", photo[0, 0], "Poster:", dream[0, 0])

print("Student pixel:")
print("Final:", final[2, 4], "Photo:", photo[2, 4], "Poster:", dream[2, 4])

print("Edge pixel:")
print("Final:", final[2, 2], "Photo:", photo[2, 2], "Poster:", dream[2, 2])

same_pixels = np.all(final == photo, axis=2)
print("Pixels exactly matching photo:", int(same_pixels.sum()))

# ---------- PART 4: background threads ----------
print("\nPART 4: Pictures per second")

total_time = sum(TIMES.values())
serial_rate = 1 / total_time

print("Without background threads:", round(serial_rate, 1), "pictures/second")

for name, seconds in TIMES.items():
    rate = 1 / seconds
    print(name, ":", round(rate, 1), "pictures/second")
