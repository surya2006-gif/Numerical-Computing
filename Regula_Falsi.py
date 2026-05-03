def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-6):
    if f(a)*f(b) >= 0:
        return "Invalid interval"

    while True:
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c

print("Root:", regula_falsi(1, 2))
