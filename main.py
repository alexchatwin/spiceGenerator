import random
from corpus import inputList
from corpus import inputPhraseList

def generateName(N, inputList): #N is the size of the N-gram, inputlist is a list of strings

    #Get all the N grams (as strings, for N>1)
    nGrams = [["".join(input[n:n+N]) for n in range(len(input)-N+1)] for input in inputList]
    #I think it's to n+N+1 rather than n+N because the range isn't inclusive.. I should check that
    
    #Get sublists of the N-gram with the next character
    links = [[[subarr[i], subarr[i+1][N-1]] for i in range(len(subarr)-1)] for subarr in nGrams]
    
    #Flatten the list
    flatLinks = [subLink for link in links for subLink in link]
    #print(flatLinks)
    
    output=""
    lastbit = random.choice(flatLinks)[0] #choose a random starting N-Gram

    output=output+lastbit

    for i in range(30): #it could run for upto 30 characters

        matchList=[n for n in flatLinks if n[0]==lastbit] #get the possible next characters

        if (len(matchList)>0): #check we find any possibilities
            lastbit=random.choice(matchList) #choose 1 random option for next character

            output=output+""+lastbit[1] #get the next character (index 0 is the exiting N-gram)

            lastbit="".join(output[-N:]) #join it on
    return output


def generateDescription(N, inputPhraseList):
    #Get all the N grams (as strings, for N>1)
    nGrams = [[" ".join(input.split()[n:n+N]) for n in range(len(input.split())-N+1)] for input in inputPhraseList]

    links = [[[subarr[i], subarr[i+1].split()[N-1]] for i in range(len(subarr)-1)] for subarr in nGrams]
    
    flatLinks = [subLink for link in links for subLink in link]

    import random
    output=""
    lastbit=random.choice([" ".join(n.split()[0:N]) for n in inputPhraseList if n.split()[0]=="This"])
    output=output+lastbit
    for i in range(60):

        matchList=[n for n in flatLinks if n[0].upper()==lastbit.upper()]
        if (len(matchList)>0):
            lastbit=random.choice(matchList)
            output=output+" "+lastbit[1]
            lastbit=" ".join(output.split()[-N:])
    return output

#Loop 10 times and create candidate names/descriptions
for i in range(10):
    name = generateName(3,inputList)
    desc = generateDescription(1,inputPhraseList)
    #Check if either is already a copy/subset of the input
    nameCheck=[s for s in inputList if name in s]
    descCheck=[s for s in inputPhraseList if desc in s]
    
    if (len(nameCheck)==0 and len(descCheck)==0):
        #if it's new, output it (with some formatting)
        print(name.lstrip().title())
        print(desc.capitalize())
    else: 
        #otherwise, complain
        print(" collision")

