def generate_fibonacci(n=100):
    if n > 100 or n < 0:
        print("Please provide number between 1 and 100")
        raise RuntimeError
    fib_1 = 0
    fib_2 = 1
    for _ in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2






if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)

