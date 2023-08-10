
def main():
    
    sigma = eval(input())
    (states1, edges1, initial1, final1) = eval(input())
    (states2, edges2, initial2, final2) = eval(input())
    
    #adicionando um par ordenado relacionando
    #os dois autômatos 
    states3 = []
    for x in states1:
        for y in states2:
            states3.append( (x,y) )
    
    
    edges3 = {}
    edges3[ ((1,2), '0')] = (2,3)
    
    final3 = []
    for x in final1:
        for y in final2:
            final3.append( (x,y) )
    
    initial3 = (initial1, initial2)
    
    teste(states3, edges3, initial3, final3)             


