# This program, given a number, prints out a list of numbers representing
# the first N Fibonacci sequence where N is the input number.
import sys


def main(n):
    fib_seq = []

    for i in range(n):
        if i == 0:
            fib_seq.append(0)
        elif i == 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])

    print(fib_seq)

main(int(sys.argv[1]))
