
import random

def shuffle(array):
   
    l = len(array)
    new_array = [0]*l;
    flag = [False]*l;

    for i in range(l):        
        idx = random.randint(0,l-i-1)
        for k in range(l):
            if flag[k]==False:
                if idx!=0:
                    idx = idx - 1
                else:
                    new_array[i] = array[k]
                    flag[k] = True
                    break
    return new_array
    
if __name__ == '__main__':
    array = [1,2,55,43,9,3,34]
    new_array = shuffle(array)
    print (new_array)


