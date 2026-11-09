import math
import numpy as np

print("=== MATH 1113: Section 6.7 - The Dot Product ===\n")

# 1. Defining Vectors
u = np.array([3, 4])
v = np.array([1, 2])

print(f"Vector u: {u}")
print(f"Vector v: {v}\n")

# 2. Calculating the Dot Product
# Algebraic definition: u1*v1 + u2*v2
dot_product = np.dot(u, v)  # or u @ v
print(f"Dot Product (u · v): {dot_product}")
# Explanation: (3 * 1) + (4 * 2) = 3 + 8 = 11

# 3. Vector Magnitudes (Norms)
magnitude_u = np.linalg.norm(u)
magnitude_v = np.linalg.norm(v)
print(f"Magnitude of u (||u||): {magnitude_u:.4f}")
print(f"Magnitude of v (||v||): {magnitude_v:.4f}")

# 4. Finding the Angle Between Vectors
# cos(theta) = (u · v) / (||u|| * ||v||)
cos_theta = dot_product / (magnitude_u * magnitude_v)
# Clamp value between -1 and 1 to avoid floating point domain errors in arccos
cos_theta = np.clip(cos_theta, -1.0, 1.0)
angle_radians = np.arccos(cos_theta)
angle_degrees = np.degrees(angle_radians)

print(f"Angle between u and v: {angle_degrees:.2f}°")

# 5. Checking for Orthogonality
w = np.array([-4, 3])  # vector orthogonal to u since (3*-4) + (4*3) = -12 + 12 = 0
dot_uw = np.dot(u, w)
print(f"\nChecking orthogonality between u and w {w}:")
print(f"Dot product u · w = {dot_uw}")
if dot_uw == 0:
    print("Result: Vectors u and w are ORTHOGONAL (perpendicular).")
else:
    print("Result: Vectors u and w are NOT orthogonal.")

# 6. Vector Projection of u onto v
# proj_v(u) = ((u · v) / ||v||^2) * v
scalar_proj = dot_product / (magnitude_v ** 2)
projection = scalar_proj * v
print(f"\nProjection of u onto v (proj_v u): {projection}")