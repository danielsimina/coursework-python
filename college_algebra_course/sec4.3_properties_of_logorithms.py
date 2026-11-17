import numpy as np


def explore_logarithms():
    # 1. Basic conversions and evaluations
    # log_2(8) = 3 because 2^3 = 8
    val_base2 = np.log2(8)

    # Natural logarithm ln(e^3) = 3
    val_ln = np.log(np.e ** 3)

    # Common logarithm log_10(1000) = 3
    val_log10 = np.log10(1000)

    print(f"log_2(8) = {val_base2}")
    print(f"ln(e^3) = {val_ln}")
    print(f"log_10(1000) = {val_log10}")

    # 2. Change of Base Formula: log_b(x) = ln(x) / ln(b)
    # Let's calculate log_3(81) -> 3^4 = 81, so result should be 4.0
    b, x = 3, 81
    change_of_base_result = np.log(x) / np.log(b)
    print(f"log_3(81) via Change of Base Formula = {change_of_base_result}")


explore_logarithms()