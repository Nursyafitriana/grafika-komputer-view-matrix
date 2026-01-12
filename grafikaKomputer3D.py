import numpy as np

# ==================================================
# DATA AWAL
# ==================================================
P_eye = np.array([6.0, 3.0, 5.0])
P_ref = np.array([2.0, 0.0, 5.0])
V_up  = np.array([0.0, 1.0, 0.0])

print("=== DATA AWAL ===")
print("P_eye :", P_eye)
print("P_ref :", P_ref)
print("V_up  :", V_up)

# ==================================================
# VEKTOR n (arah pandang kamera)
# ==================================================
print("\n=== VEKTOR n ===")
n = P_eye - P_ref
print("P_eye - P_ref =", n)

n_len = np.linalg.norm(n)
print("Panjang n =", n_len)

n = n / n_len
print("n =", n)

# ==================================================
# VEKTOR u (arah kanan kamera)
# ==================================================
print("\n=== VEKTOR u ===")
u = np.cross(V_up, n)
print("V_up x n =", u)

u_len = np.linalg.norm(u)
print("Panjang u =", u_len)

u = u / u_len
print("u =", u)

# ==================================================
# VEKTOR v (arah atas kamera)
# ==================================================
print("\n=== VEKTOR v ===")
v = np.cross(n, u)
print("v =", v)

# ==================================================
# MATRIKS TRANSFORMASI VIEW
# ==================================================
print("\n=== MATRIKS VIEW (LOOKAT) ===")
M_view = np.array([
    [u[0], u[1], u[2], -np.dot(u, P_eye)],
    [v[0], v[1], v[2], -np.dot(v, P_eye)],
    [n[0], n[1], n[2], -np.dot(n, P_eye)],
    [0.0,  0.0,  0.0,   1.0]
])

print(M_view)

# ==================================================
# HASIL AKHIR
# ==================================================
print("\n=== HASIL AKHIR ===")
print("Matriks View Kamera:")
print(M_view)
