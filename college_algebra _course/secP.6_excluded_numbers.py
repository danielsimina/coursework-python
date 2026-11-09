class RationalExpression:
    """
    Represents a rational expression: P(x) / Q(x)
    For educational clarity, numerators and denominators are represented
    as algebraic strings, alongside their roots/restrictions.
    """
    def __init__(self, numerator: str, denominator: str, restricted_values: list):
        self.numerator = numerator
        self.denominator = denominator
        self.restrictions = sorted(list(set(restricted_values)))

    def domain(self):
        """Returns the domain restriction description."""
        if not self.restrictions:
            return "All real numbers (-∞, ∞)"
        res_str = ", ".join(map(str, self.restrictions))
        return f"All real numbers except x ≠ {res_str}"

    def __str__(self):
        return f"[{self.numerator}] / [{self.denominator}]"


class RationalOperations:
    @staticmethod
    def simplify_example():
        """
        Demonstrates simplifying: (x^2 - 4) / (x^2 + 4x + 4)
        Numerator factors to: (x - 2)(x + 2)
        Denominator factors to: (x + 2)(x + 2)
        Cancelled factor: (x + 2), leaving (x - 2) / (x + 2) with x ≠ -2
        """
        original = RationalExpression("x^2 - 4", "x^2 + 4x + 4", [-2])
        simplified = RationalExpression("x - 2", "x + 2", [-2])
        return original, simplified

    @staticmethod
    def multiply_example():
        """
        Demonstrates multiplication of rational expressions.
        (2x / (x - 3)) * ((x^2 - 9) / 4x)
        """
        # Restrictions come from both denominators: x ≠ 3, x ≠ 0
        return RationalExpression("(2x) * (x^2 - 9)", "(x - 3) * (4x)", [0, 3])

    @staticmethod
    def find_lcd(denom1_factors, denom2_factors):
        """
        Finds the Least Common Denominator (LCD) by taking the highest power
        of each distinct factor present in the denominators.
        """
        lcd_dict = {}
        for factor, power in denom1_factors.items():
            lcd_dict[factor] = power
        for factor, power in denom2_factors.items():
            if factor in lcd_dict:
                lcd_dict[factor] = max(lcd_dict[factor], power)
            else:
                lcd_dict[factor] = power
        return lcd_dict


# --- Demonstration of Section P.6 Operations ---
if __name__ == "__main__":
    print("=== MATH 1111: College Algebra - Section P.6 Rational Expressions ===\n")

    # 1. Domain and Simplification
    orig, simp = RationalOperations.simplify_example()
    print("1. Simplifying Rational Expressions:")
    print(f"   Original Expression: {orig}")
    print(f"   Domain: {orig.domain()}")
    print(f"   Simplified Form: {simp}\n")

    # 2. Multiplication
    mult_expr = RationalOperations.multiply_example()
    print("2. Multiplying Rational Expressions:")
    print(f"   Expression: {mult_expr}")
    print(f"   Domain Restrictions: {mult_expr.domain()}\n")

    # 3. LCD Finder for Addition/Subtraction
    # Example: Denom 1 = x(x+2)^2, Denom 2 = (x+2)(x-3)
    d1 = {"x": 1, "(x+2)": 2}
    d2 = {"(x+2)": 1, "(x-3)": 1}
    lcd = RationalOperations.find_lcd(d1, d2)
    print("3. Least Common Denominator (LCD) Calculation:")
    print(f"   Denominator 1 factors: {d1}")
    print(f"   Denominator 2 factors: {d2}")
    lcd_str = " * ".join([f"{f}^{p}" if p > 1 else f"{f}" for f, p in lcd.items()])
    print(f"   Resulting LCD: {lcd_str}")