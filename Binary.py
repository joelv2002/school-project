def convert(bin):
    numb=0
    for i in range(0,len(bin)):
        numb+=(2**(len(bin)-1-i)*int(bin[i]))
    return(numb)

print(convert("1010"))
