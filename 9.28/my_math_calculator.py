def sqrt(n):

    # We are using n itself as
    # initial approximation This
    # can definitely be improved
    if type(n) == str:
        raise TypeError("String")

    if n < 0:
        raise ValueError("sqrt received a value less than 0")

    x = n
    y = 1

    e = 0.000001
    while (x - y > e):
        x = (x + y)/2
        y = n / x
    return x
