# numSample = int(input('numSample: '))
# numFeature = int(input('numFeature: '))
#
# X = []
# d = []
# W = []
#
# for i in range(numSample):
#     _x = []
#     for j in range(numFeature):
#         __x = int(input('Sample: '))
#         _x.append(__x)
#     X.append(_x)
#     W.append(0)
#     _d = int(input('Class: '))
#     d.append(_d)
#
# c = int(input("c: "))
# k = int(input("k: "))

numSample = 6
numFeature = 2

X = [
    [0, 0],
    [2, 1],
    [3, 2],
    [1, 2],
    [2, 3],
    [2, 4]
]

d = [1, 1, 1, -1, -1, -1]
W = [0, 0, 0]

c = 1
k = 1


def calculateValueOfD(W, x):
    s = W[0]
    for i in range(len(x)):
        s += W[i + 1] * x[i]
    return s


def sgn(D):
    if D >= 0:
        return 1
    else:
        return -1


def changeW(W, x, d):
    W[0] = W[0] + c * d * k
    for j in range(1, len(W)):
        W[j] = W[j] + (c * d * x[j - 1])
    return W


def label(x, w):
    print("%8s" % 't', end='')
    print("%8s" % 'i', end='')

    for z in range(len(x)):
        print("%8s" % ('x' + str(z + 1)), end='')
    print("%8s" % 'd', end='')
    for z in range(len(w)):
        print("%8s" % ('Old w' + str(z)), end='')
    print("%8s" % 'D', end='')
    print("%8s" % 'Error?', end='')
    for z in range(len(w)):
        print("%8s" % 'New w' + str(z), end='')
    print()
    print('-' * 110)


def display(t, i, x, d, oldW, D, error, newW):
    print("%8d" % t, end='')
    print("%8d" % (i + 1), end='')

    for z in range(len(x)):
        print("%8d" % x[z], end='')
    print("%8d" % d, end='')
    for z in range(len(oldW)):
        print("%8d" % oldW[z], end='')
    print("%8d" % D, end='')
    print("%8s" % error, end='')
    for z in range(len(newW)):
        print("%8d" % newW[z], end='')
    print()


label(X[0], W)

t = 0
while True:
    correctInstance = 0
    for i in range(numSample):
        t += 1
        oldW = W.copy()
        D = calculateValueOfD(W, X[i])
        sgnD = sgn(D)
        error = 'No'

        if sgnD != d[i]:
            error = 'Yes'
            correctInstance -= 1
            W = changeW(W, X[i], d[i])
        else:
            correctInstance += 1
        newW = W.copy()

        display(t, i, X[i], d[i], oldW, D, error, newW)

    if correctInstance == numSample:
        break
