import sys


def eukld(a, m):
    y = [0, 1]
    r = [a, m]
    q = ["  -"]
    while True:
        q.append(r[-2] // r[-1])
        r.append(r[-2] % r[-1])
        if r[-1] == 0:
            break
        y.append(y[-2] - int(q[-1]) * y[-1])
    # print table
    print("\n    y     r |   q\n" + "-" * 18)
    for i in range(len(y)):
        print("{0:5} {1:5} | {2:3}".format(y[i], r[i], q[i]))
    print(" " * 10 + "0 |\n")
    print("ggT({0}, {1}) = {2}\n".format(a, m, r[-2]))


sys.argv.pop(0)
sys.argv.sort()
eukld(int(sys.argv[0]), int(sys.argv[1]))
