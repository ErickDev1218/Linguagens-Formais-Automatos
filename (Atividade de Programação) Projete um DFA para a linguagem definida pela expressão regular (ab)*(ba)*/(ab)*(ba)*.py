# Coloque aqui as transições do seu autômato
edges = {
   (1,'a') : 2,
   (1,'b') : 5,
   (2,'a') : 3,
   (2,'b') : 1,
   (3,'a') : 3,
   (3,'b') : 3,
   (4,'a') : 3,
   (4,'b') : 5,
   (5,'a') : 4,
   (5,'b') : 3
}

#Coloque aqui os estados finais do seu autômato
accepting = [1,4]

initial   = 1

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = input()
print(dfa(string, initial, edges, accepting))