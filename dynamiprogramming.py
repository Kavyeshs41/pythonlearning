import time

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def dpfibon(n):
    start_time1 = time.time()
    la = [0, 1]
    for x in range(2, n + 1):
        la.append(la[x - 1] + la[x - 2])
    elapsed_time = time.time() - start_time1
    return la[n], elapsed_time


print(dpfibon(1000))

print(fibonacci(10))
