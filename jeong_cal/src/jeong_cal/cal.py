from haram_sum.sum import sum
from jeong_mul.mul import mul
from haram_sub.sub import sub
import sys


def cl_sum():
    if len(sys.argv) < 3:
        print("Usage: script <a> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(a, "+", b)
    print(sum(a, b))


def cl_sub():
    if len(sys.argv) < 3:
        print("Usage: script <a> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(a, "-", b)
    print(sub(a, b))


def cl_mul():
    if len(sys.argv) < 3:
        print("Usage: script <a> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(a, "*", b)
    print(mul(a, b))
