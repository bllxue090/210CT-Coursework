
def predict_aliens_num(x, y, days):

    aliens = [0]*(days+1)
    eggs = [0]*(days+1)
    aliens[0] = 1
    idx = 1
    while idx <= days:
        if idx>=y:
            aliens[idx] = aliens[idx-1]+eggs[idx-y]
        else:
            aliens[idx] = aliens[idx-1]
        eggs[idx] = aliens[idx]*x
        idx += 1
    return aliens[days]

if __name__ == '__main__':
    x,y,days = 3,5,30
    print ('the number of aliens:')
    print (predict_aliens_num(x, y, days))
