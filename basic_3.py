


import math
    
def highest_perfect_square(x):
    y = math.floor(math.sqrt(x))
    y = long(y)
    if (y+1)*(y+1)<=x:
        return (y+1)*(y+1)
    else:
        return y*y
    

if __name__ == '__main__':
    x = 25
    ans = highest_perfect_square(x)
    print ans
