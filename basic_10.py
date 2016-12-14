
def lengest_ascend_subsequence(arr):    
    l = len(arr)
    if(l==0):
        return []
    res = [1]*l
    pre = [-1]*l
    
    maxid = -1;
    maxlen = 0;
    for i in range(l):
        for j in range(i):
            if(arr[i]>arr[j]):
                if(res[i]<res[j]+1):
                    res[i] = res[j]+1
                    pre[i] = j
        if(maxlen<res[i]):
            maxlen = res[i]
            maxid = i
    
    subseq = []
    while(maxid!=-1):
        subseq.append(arr[maxid])
        maxid = pre[maxid]
    subseq.reverse()
    return subseq
                
    
    

if __name__ == '__main__':  
    arr = [53,2,3,60,90,100,70,80,85]
    subseq = lengest_ascend_subsequence(arr)
    
    print ('length is'), len(subseq)
    print (subseq)
    
