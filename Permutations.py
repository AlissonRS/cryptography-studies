import cProfile


def faculty(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s


def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt


cProfile.run('counter(faculty(12))')
