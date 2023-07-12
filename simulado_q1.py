# Simulado II - questão 1
def sqrt(n):
    if n == 0:
        return 0
    resp = 1/(6 + sqrt(n-1))
    return resp

n = int(input())
ans = 3 + sqrt(n)
print(f"{ans:.10f}")
