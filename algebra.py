def calculate_fn(x):
    result = x**5 + 8*x**4 - 5*x**3 + 3*x**2 + x - 12
    return result

n_value = int(input("sonni kiriting: "))

result = calculate_fn(n_value)

print(f"f({n_value}) =", result)
