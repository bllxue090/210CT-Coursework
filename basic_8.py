
def remove_vowels(s):
    res_string = ''
    for c in s:
        if(c=='a' or c=='e' or c=='u' or c=='i' or c=='o'):
            continue
        else:
            res_string += c
    return res_string
    

if __name__ == '__main__':
    s = 'beautiful'
    print (remove_vowels(s))
    
