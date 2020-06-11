def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n - 1)


print(sum_integers(3))
print(sum_integers(50))
print(sum_integers(100))
