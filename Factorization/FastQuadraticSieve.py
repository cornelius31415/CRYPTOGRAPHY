import math
import numpy as np
import sympy
from collections import Counter

def prime_factors_base(B):
    """Generiert eine Primzahlbasis bis zur Grenze B."""
    return [p for p in range(2, B) if sympy.isprime(p)]

def is_smooth(n, factor_base):
    """Prüft, ob n glatt ist (nur durch die Faktor-Basis teilbar)."""
    original_n = n
    factor_counts = Counter()
    
    for p in factor_base:
        while n % p == 0:
            n //= p
            factor_counts[p] += 1

    return (n == 1), factor_counts if n == 1 else None

def build_exponent_matrix(smooth_numbers, factor_base):
    """Erstellt eine Matrix mit den Exponenten (mod 2)."""
    matrix = []
    vectors = []

    for num, factor_count in smooth_numbers:
        vector = [factor_count.get(p, 0) % 2 for p in factor_base]
        matrix.append(vector)
        vectors.append(num)

    return np.array(matrix, dtype=int), vectors

def gaussian_elimination(matrix):
    """Führt eine mod-2-Gauß-Elimination durch und findet lineare Abhängigkeiten."""
    m, n = matrix.shape
    matrix = matrix.copy()
    
    pivot_cols = []
    for col in range(n):
        row = next((r for r in range(col, m) if matrix[r, col] == 1), None)
        if row is None:
            continue  # Keine führende 1, überspringen

        matrix[[col, row]] = matrix[[row, col]]  # Zeilen tauschen
        pivot_cols.append(col)

        for r in range(m):
            if r != col and matrix[r, col] == 1:
                matrix[r] ^= matrix[col]  # XOR für Binärmatrix

    dependent_rows = [r for r in range(m) if all(matrix[r, c] == 0 for c in pivot_cols)]
    return dependent_rows if dependent_rows else None

def find_factor(N, x_values, dependent_row):
    """Findet einen Faktor von N mit einer linearen Abhängigkeit."""
    x_product = 1
    y_product = 1

    # Sicherstellen, dass dependent_row eine Liste ist
    if isinstance(dependent_row, int):
        dependent_row = [dependent_row]

    for idx in dependent_row:
        x_product *= x_values[idx]
        y_product *= (x_values[idx] ** 2) % N

    x_product %= N
    y_product = int(math.sqrt(y_product) % N)

    factor = math.gcd(x_product - y_product, N)
    if 1 < factor < N:
        return factor, N // factor
    return None

def quadratic_sieve(N, B=50):
    """Optimiertes Quadratisches Sieb zur Faktorisierung von N."""
    factor_base = prime_factors_base(B)
    root_N = int(math.isqrt(N))

    smooth_numbers = []
    x_values = []
    
    # Sammle glatte Zahlen
    for x in range(root_N, root_N + 5000):
        Qx = (x * x) % N
        smooth, factor_count = is_smooth(Qx, factor_base)
        if smooth:
            smooth_numbers.append((x, factor_count))
            x_values.append(x)

        if len(smooth_numbers) > len(factor_base):
            break

    # Erstelle die Exponentenmatrix
    matrix, x_values_filtered = build_exponent_matrix(smooth_numbers, factor_base)

    # Finde lineare Abhängigkeit
    dependent_rows = gaussian_elimination(matrix)
    if dependent_rows is None:
        return None

    # Sicherstellen, dass dependent_rows eine Liste ist
    if isinstance(dependent_rows, int):
        dependent_rows = [dependent_rows]

    # Versuche, einen Faktor zu finden
    for row in dependent_rows:
        factors = find_factor(N, x_values_filtered, row)
        if factors:
            return factors

    return None

# Beispielzahl zur Faktorisierung
N = 143253464566  # Eine semi-prime Zahl
factors = quadratic_sieve(N)
print("Gefundene Faktoren:", factors)
print(149*587)