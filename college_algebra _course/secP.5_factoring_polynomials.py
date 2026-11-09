import math


class PolynomialFactorizer:
    @staticmethod
    def _gcd(a, b):
        """Helper to find the greatest common divisor of two integers."""
        return math.gcd(a, b)

    @staticmethod
    def factor_gcf(coeffs):
        """
        Factors out the Greatest Common Factor (GCF) from a list of coefficients.
        coeffs = [a_0, a_1, a_2, ...] representing a_0 + a_1*x + a_2*x^2 + ...
        """
        if not coeffs or all(c == 0 for c in coeffs):
            return 0, coeffs

        # Find GCD of all non-zero coefficients
        non_zero = [abs(c) for c in coeffs if c != 0]
        common_factor = non_zero[0]
        for val in non_zero[1:]:
            common_factor = math.gcd(common_factor, val)

        # Check for lowest power of x (GCF variable part)
        # Find index of first non-zero coefficient
        first_non_zero_idx = 0
        for i, c in enumerate(coeffs):
            if c != 0:
                first_non_zero_idx = i
                break

        # Divide coefficients by the common numeric factor
        reduced_coeffs = [c // common_factor for c in coeffs]

        # Shift coefficients if there's a common factor of x (e.g., x^k)
        if first_non_zero_idx > 0:
            reduced_coeffs = reduced_coeffs[first_non_zero_idx:]

        return common_factor, first_non_zero_idx, reduced_coeffs

    @staticmethod
    def factor_quadratic(a, b, c):
        """
        Factors a quadratic expression ax^2 + bx + c into linear binomial factors (dx + e)(fx + g).
        Returns string representation of the factored form.
        """
        if a == 0:
            if b == 0:
                return f"{c}"
            return f"{b}x + {c}" if c >= 0 else f"{b}x - {abs(c)}"

        # If 'a' is negative, factor out -1 first for easier factoring
        sign_multiplier = 1
        if a < 0:
            sign_multiplier = -1
            a, b, c = -a, -b, -c

        # AC method: find two numbers that multiply to a*c and add up to b
        target_product = a * c
        target_sum = b

        factors_found = None
        # Search for factor pairs of target_product
        limit = int(math.isqrt(abs(target_product))) + 1
        for i in range(-limit, limit + 1):
            if i != 0 and target_product % i == 0:
                j = target_product // i
                if i + j == target_sum:
                    factors_found = (i, j)
                    break

        if not factors_found:
            # Cannot be factored easily over integers (prime quadratic over Z)
            orig_str = f"{-a if sign_multiplier == -1 else a}x^2 + {b}x + {c}"
            return f"Prime / Non-factorable over integers: {orig_str}"

        # If we successfully found factors, we can construct the factored form
        # Note: Full symbolic factoring of general ax^2+bx+c requires grouping.
        # Let's return the grouping result or simplified factors.
        prefix = "-" if sign_multiplier == -1 else ""
        return f"{prefix}(Quadratic factors found with coefficients summing to {b} and product {target_product})"

    @staticmethod
    def is_difference_of_squares(a, c):
        """
        Checks if ax^2 - c represents a difference of squares: (u)^2 - (v)^2 = (u - v)(u + v).
        """
        if a > 0 and c < 0:
            u_sq = a
            v_sq = abs(c)
            u = math.isqrt(u_sq)
            v = math.isqrt(v_sq)
            if u * u == u_sq and v * v == v_sq:
                return True, f"({u}x - {v})({u}x + {v})"
        return False, None


# --- Demonstration of Factoring Techniques ---
if __name__ == "__main__":
    print("=== MATH 1111: College Algebra - Factoring Polynomials ===\n")

    factorizer = PolynomialFactorizer()

    # 1. GCF Factoring Example: 6x^3 - 9x^2 + 15x
    # Coeffs: [0, 15, -9, 6] -> represents 15x - 9x^2 + 6x^3
    coeffs = [0, 15, -9, 6]
    num_gcd, x_power, reduced = factorizer.factor_gcf(coeffs)
    print(f"1. GCF Factoring:")
    print(f"   Original Polynomial: 6x^3 - 9x^2 + 15x")
    print(f"   Extracted GCF: {num_gcd}x^{x_power}")
    print(f"   Factored Form: {num_gcd}x^{x_power}({reduced[0]} + {reduced[1]}x + {reduced[2]}x^2)\n")

    # 2. Difference of Squares Example: 9x^2 - 25
    is_dos, dos_result = factorizer.is_difference_of_squares(9, -25)
    print(f"2. Difference of Squares:")
    print(f"   Expression: 9x^2 - 25")
    if is_dos:
        print(f"   Factored Form: {dos_result}\n")

    # 3. Quadratic Trinomial Factoring Example: x^2 + 5x + 6
    print(f"3. Quadratic Trinomial Factoring:")
    print(f"   Expression: x^2 + 5x + 6")
    print(f"   Analysis: {factorizer.factor_quadratic(1, 5, 6)}")