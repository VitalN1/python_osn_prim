n, k = map(int, input().split())
def c(n,k):
    if k == 1:
        return n
    elif n== k or k==0:
        return 1
    else:
        return c(n-1, k) + c(n-1, k-1)
