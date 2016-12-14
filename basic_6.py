


    
def reverse_sentence(s):
    words = s.split(' ')
    r_s = ''
    l = len(words)
    # join the words in reversed order
    for i in range(l):
        r_s = ' '.join([words[i],r_s])
    return r_s

if __name__ == '__main__':
    s = "This is awesome"
    r_s = reverse_sentence(s)
    print (r_s)
