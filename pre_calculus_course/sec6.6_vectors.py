import math
import numpy as np

print("--- MATH 1113: Section 6.6 Vectors Toolkit ---\n")

# 1. Defining Vectors
# Vectors can be represented as tuples, lists, or numpy arrays
v = np.array([3, 4])
u = np.array([1, -2])

print(f"Vector v: {v}")
print(f"Vector u: {u}\n")

# 2. Magnitude (Length) of a Vector
# Formula: ||v|| = sqrt(a^2 + b^2)
magnitude_v = np.linalg.norm(v)
print(f"Magnitude of v (||v||): {magnitude_v:.4f}")

# 3. Direction Angle (in degrees)
# Formula: theta = arctan(b / a), adjusted for quadrants
direction_rad = math.atan2(v[1], v[0])
direction_deg = math.degrees(direction_rad)
print(f"Direction angle of v: {direction_deg:.2f}°\n")

# 4. Vector Addition and Scalar Multiplication
scalar = 3
sum_vu = v + u
scaled_v = scalar * v

print(f"v + u = {sum_vu}")
print(f"{scalar} * v = {scaled_v}\n")

# 5. Unit Vector in the Direction of v
# Formula: u_vec = v / ||v||
unit_v = v / magnitude_v
print(f"Unit vector in direction of v: {unit_v}")
print(f"Check magnitude of unit vector (should be 1.0): {np.linalg.norm(unit_v):.4f}\n")

# 6. Dot Product (Scalar Product)
# Formula: v · u = v_1*u_1 + v_2*u_2
dot_product = np.dot(v, u)
print(f"Dot product (v · u): {dot_product}")

# 7. Angle Between Two Vectors
# Formula: cos(theta) = (v · u) / (||v|| * ||u||)
mag_u = np.linalg.norm(u)
cos_theta = dot_product / (magnitude_v * mag_u)
# Clamp value between -1 and 1 to avoid domain errors due to floating-point precision
cos_theta = np.clip(cos_theta, -1.0, 1.0)
angle_rad = math.acos(cos_theta)
angle_deg = math.degrees(angle_rad)

print(f"Angle between v and u: {angle_deg:.2f}°")