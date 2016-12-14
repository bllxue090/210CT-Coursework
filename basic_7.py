
def check_prime(n, x):
    if(n<=1): 
        return False
    if(x>=n):
        return True
    if(n%x==0):
        return False
    return check_prime(n,x+1)
    

if __name__ == '__main__':
    n = 47
    print check_prime(n, 2)
    
