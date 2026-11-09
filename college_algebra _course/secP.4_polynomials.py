class Polynomial:
    def __init__(self, coeffs):
        """
        Represent a polynomial by its coefficients in ascending order of powers:
        coeffs = [a_0, a_1, a_2, ..., a_n]
        represents a_0 + a_1*x + a_2*x^2 + ... + a_n*x^n
        """
        # Strip trailing zeros to keep degree accurate, unless it's just [0]
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        self.coeffs = coeffs

    def degree(self):
        """Returns the highest power (degree) of the polynomial."""
        if len(self.coeffs) == 1 and self.coeffs[0] == 0:
            return 0
        return len(self.coeffs) - 1

    def leading_coefficient(self):
        """Returns the coefficient of the term with the highest power."""
        return self.coeffs[-1]

    def evaluate(self, x):
        """Evaluates the polynomial for a given value of x using Horner's method."""
        result = 0
        for coeff in reversed(self.coeffs):
            result = result * x + coeff
        return result

    def __add__(self, other):
        """Adds two polynomials by combining like terms."""
        max_len = max(len(self.coeffs), len(other.coeffs))
        res_coeffs = [0] * max_len
        for i in range(max_len):
            val1 = self.coeffs[i] if i < len(self.coeffs) else 0
            val2 = other.coeffs[i] if i < len(other.coeffs) else 0
            res_coeffs[i] = val1 + val2
        return Polynomial(res_coeffs)

    def __sub__(self, other):
        """Subtracts two polynomials by combining like terms."""
        max_len = max(len(self.coeffs), len(other.coeffs))
        res_coeffs = [0] * max_len
        for i in range(max_len):
            val1 = self.coeffs[i] if i < len(self.coeffs) else 0
            val2 = other.coeffs[i] if i < len(other.coeffs) else 0
            res_coeffs[i] = val1 - val2
        return Polynomial(res_coeffs)

    def __mul__(self, other):
        """Multiplies two polynomials using the distributive property."""
        res_len = len(self.coeffs) + len(other.coeffs) - 1
        res_coeffs = [0] * res_len
        for i, c1 in enumerate(self.coeffs):
            for j, c2 in enumerate(other.coeffs):
                res_coeffs[i + j] += c1 * c2
        return Polynomial(res_coeffs)

    def __str__(self):
        """Returns a human-readable string in descending standard form."""
        terms = []
        for i, coeff in enumerate(reversed(self.coeffs)):
            power = len(self.coeffs) - 1 - i
            if coeff == 0 and len(self.coeffs) > 1:
                continue

            if power == 0:
                term_str = f"{coeff}"
            elif power == 1:
                if coeff == 1:
                    term_str = "x"
                elif coeff == -1:
                    term_str = "-x"
                else:
                    term_str = f"{coeff}x"
            else:
                if coeff == 1:
                    term_str = f"x^{power}"
                elif coeff == -1:
                    term_str = f"-x^{power}"
                else:
                    term_str = f"{coeff}x^{power}"

            terms.append(term_str)

        full_str = ""
        for i, t in enumerate(terms):
            if i == 0:
                full_str += t
            else:
                if t.startswith("-"):
                    full_str += f" - {t[1:]}"
                else:
                    full_str += f" + {t}"
        return full_str


# --- Demonstration of Section P.4 Operations ---
if __name__ == "__main__":
    print("=== MATH 1111: College Algebra - Section P.4 Polynomials ===\n")

    # Define P(x) = 3x^2 + 2x - 5  -> represented as coefficients [-5, 2, 3]
    # Define Q(x) = x^3 - 4x + 7   -> represented as coefficients [7, -4, 0, 1]
    P = Polynomial([-5, 2, 3])
    Q = Polynomial([7, -4, 0, 1])

    print(f"P(x) = {P}")
    print(f"  • Degree: {P.degree()}")
    print(f"  • Leading Coefficient: {P.leading_coefficient()}\n")

    print(f"Q(x) = {Q}")
    print(f"  • Degree: {Q.degree()}")
    print(f"  • Leading Coefficient: {Q.leading_coefficient()}\n")

    # 1. Addition: P(x) + Q(x)
    print(f"Addition: P(x) + Q(x) = {P + Q}")

    # 2. Subtraction: P(x) - Q(x)
    print(f"Subtraction: P(x) - Q(x) = {P - Q}")

    # 3. Multiplication: P(x) * Q(x)
    print(f"Multiplication: P(x) * Q(x) = {P * Q}")

    # 4. Evaluation: P(2)
    x_val = 2
    print(f"Evaluation: P({x_val}) = {P.evaluate(x_val)} (Expected: 3(2)^2 + 2(2) - 5 = 12 + 4 - 5 = 11)")