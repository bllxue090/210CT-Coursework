
def count_zeros(n):
    cnt2 = 0
    cnt5 = 0
    x = 2
    while x<=n:
        cnt2 = cnt2 + n/x
        x = x*x
    y = 5
    while y<=n:
        cnt5 = cnt5 + n/y
        y = y*y
    return min(cnt2,cnt5)
        

if __name__ == '__main__':
    n = 100
    print (count_zeros(n))
