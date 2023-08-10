def prefixo(x, y):
    ## Coloque seu código aqui
    if x == "":
        return True
    if y == "" and x != "":
        return False
    
    a = x[0]
    z = x[1:]
    
    b = y[0]
    w = y[1:]
    
    if a == b and prefixo(z,w):
        return True
    else:
        return False
    

def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()