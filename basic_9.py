
def binary_search(arr, low, high):
    
    l = len(arr)
    left = 0
    right = l-1
    while(left<right):
        mid = (left+right)/2
        # if the element in the middle is smaller than low, 
        # then we can ignore the left half, otherwise ignore the right half
        if(arr[mid]<low):
            left = mid+1
        else:
            right = mid
    if(left<=right and arr[left]<low):
        left += 1
    # a is the smallest value that >= low
    a = left
    left = 0
    right = l-1
    while(left<right):
        mid = (left+right+1)/2
        if(arr[mid]<=high):
            left = mid
        else:
            right = mid-1
    if(left<=right and arr[right]>high):
        right -= 1
    # b is the largest value that <= high
    b = right
    if(a<=b):
        return True
    else:
        return False
    

if __name__ == '__main__':
    arr = [2,3,5,7,9,13]
    low = 10
    high = 14
    print binary_search(arr, low, high)
    
