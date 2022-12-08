max_iter = 80


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


if __name__ == "__main__":
    print(mandelbrot(complex(0, 0)))
