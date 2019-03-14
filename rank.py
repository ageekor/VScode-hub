import traceback

n = eval(input())
def rank(n):
    if n == 0:
        return 1
    else:
        return n*rank(n-1)
try:
    print(rank(n))
except Exception as e:
    print(e)
    print(e.args)