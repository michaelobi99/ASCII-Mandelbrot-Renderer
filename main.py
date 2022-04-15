from typing import List

def scaler(min_from: int, max_from:int , min_to: float, max_to: float):
    w_from: int = max_from - min_from
    w_to: float = max_to - min_to
    mid_from: int = (max_from - min_from) // 2 + min_from
    mid_to: float = (max_to - min_to) / 2.0 + min_to
    return lambda from_: (from_ - mid_from) / w_from * w_to + mid_to

def scaled_complex(scaler_x, scaler_y):
    return lambda x, y: complex(scaler_x(x), scaler_y(y))

def mandelbrot_iterations(c: complex):
    z: complex = 0
    iterations: int = 0
    max_iterations: int = 1000
    while abs(z) < 2 and iterations < max_iterations:
        iterations += 1
        z = (z ** 2) + c
    return iterations

def render_mandelbrot(vector: List, width: int):
    counter = 0
    for elem in vector:
        if elem > 50:
            print('*', end ='')
        else:
            print(' ', end = '')
        counter += 1
        if (counter % width == 0):
            print()


def main():
    w, h = 150, 40
    scale = scaled_complex(scaler(0, w, -2.0, 1.0), scaler(0, h, -1.0, 1.0))
    i_to_xy = lambda i: scale(i % w, i // w)
    to_iteration_count = lambda j: mandelbrot_iterations((i_to_xy(j)))
    vector: List = [_ for _ in range(w*h)]
    for i in range(len(vector)):
        vector[i] = to_iteration_count(i)
    render_mandelbrot(vector, w)

if __name__ == '__main__':
    main()