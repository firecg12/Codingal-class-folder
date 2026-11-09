
# ================================
# DANCE CLASS JUDGE
# ================================

# ---------- SETUP (given to you) ----------
import numpy as np
import math

# The pose AI's arm points for one dancer at three moments, as (x, y, sure) in pixels.
# 5 and 6 = shoulders, 7 and 8 = elbows, 9 and 10 = wrists.
moments = {
    "Moment 1": {5: (220, 200, 0.9), 7: (160, 197, 0.8), 9: (100, 195, 0.9),
                 6: (300, 200, 0.9), 8: (360, 198, 0.9), 10: (420, 196, 0.8)},
    "Moment 2": {5: (220, 200, 0.9), 7: (180, 160, 0.9), 9: (150, 110, 0.7),
                 6: (300, 200, 0.9), 8: (350, 170, 0.8), 10: (400, 140, 0.9)},
    "Moment 3": {5: (220, 200, 0.9), 7: (160, 200, 0.6), 9: (100, 200, 0.1),
                 6: (300, 200, 0.9), 8: (360, 200, 0.9), 10: (420, 200, 0.2)},
}
TARGET = [180, 180, 0, 0]

print("Moments:", len(moments), " target:", TARGET)

# ---------- PART 1: unsure points ----------
print("\nPART 1: Unsure points")

for name, points in moments.items():
    unsure = [p for p in points if points[p][2] < 0.3]
    unsure.sort(key=lambda p: points[p][2])
    print(name, "Unsure points:", unsure)

# ---------- PART 2: arm angles ----------
print("\nPART 2: Arm angles")

def arm_angles(points):
    pairs = [(5, 7), (7, 9), (6, 8), (8, 10)]
    angles = []

    for start, end in pairs:
        x1, y1, _ = points[start]
        x2, y2, _ = points[end]

        angle = math.degrees(math.atan2(y1 - y2, x2 - x1))
        angles.append(angle)

    return angles

for name, points in moments.items():
    angles = arm_angles(points)
    print(name, [round(a) for a in angles])

# ---------- PART 3: scores ----------
print("\nPART 3: Scores")

def score(points, target):
    arm_points = [5, 7, 9, 6, 8, 10]

    for p in arm_points:
        if points[p][2] < 0.3:
            return 0

    angles = arm_angles(points)
    differences = []

    for angle, wanted in zip(angles, target):
        difference = abs((angle - wanted + 180) % 360 - 180)
        differences.append(difference)

    final_score = 100 - np.mean(differences)
    return max(0, final_score)

scores = {}

for name, points in moments.items():
    scores[name] = round(score(points, TARGET), 1)
    print(name, "Score:", scores[name])

# ---------- PART 4: the judge ----------
print("\nPART 4: The judge")

best_moment = max(scores, key=scores.get)
best_score = scores[best_moment]

result = "PASS" if best_score >= 80 else "TRY AGAIN"

print("Best moment:", best_moment)
print("Score:", best_score)
print(result)
