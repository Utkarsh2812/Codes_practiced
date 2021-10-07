def factor_recur(n):
    if n ==1 or n ==0 :
        return 1
    return n * factor_recur(n-1)

print(factor_recur(99))