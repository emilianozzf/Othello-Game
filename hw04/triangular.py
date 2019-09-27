# This program, given a number, prints out the "triangular number" of
# the input number (i.e., the sum of values between 1 and the input number).
import sys


def main(in_num):
    tri_num = 0

    for i in range(1, in_num + 1):
        tri_num += i

    print(tri_num)

main(int(sys.argv[1]))
