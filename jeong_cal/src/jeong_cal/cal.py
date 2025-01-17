from haram_sum.sum import sum as jeong_sum
from haram_sub.sub import sub as haram_sub
from jeong_mul.mul import mul as haram_mul


def cl_sum():
    import sys

    if len(sys.argv) < 3:
        print("Usage: cl_cal_sum <a> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(a, "+", b)
    jeong_sum(a, b)


def cl_sub():
    import sys

    if len(sys.argv) < 3:
        print("Usage: cl_cal_sub <a> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(a, "-", b)
    haram_sub(a, b)


def cl_mul():
    import sys

    if len(sys.argv) < 3:
        print("Usage: cl_cal_mul <a> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(a, "*", b)
    haram_mul(a, b)
