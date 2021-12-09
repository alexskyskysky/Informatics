def toBin(dec):
    result = ''
    while(dec>0):
        result+=str(dec%2)
        dec//=2
    return result[::-1]
