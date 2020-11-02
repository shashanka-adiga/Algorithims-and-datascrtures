def max_sum(n, price):
    if n == 0:
        return 0

    return max(price[n-1] + max_sum(n-1,price), max_sum(n-1, price))

n = 3
price = [4,6,9]
print(max_sum(n, price))