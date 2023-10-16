import json
import random

def getData(wordType: str):
    ## read the words json file and then return the word list with that word type
    with open('Data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)

    return words[wordType]

# a random coin toss P has to be a number between 0 and 1, by default this is 0.5
def coinToss(p: float = 0.5):
    if random.random() < p:
        return True
    else:
        return False

def randomFromList(L: list):
    index = random.randint(0, len(L) - 1)
    return L[index]

def Sentence():
    sentence =  f"{NounPhrase()} {VerbPhrase()}"
    ##sentence[0] = sentence[0].upper()
    return sentence

# noun phrase in only optional for a verb phrase but mandetory for a prepositional phrase 
# or a full sentence so depending on the type you handle each case differently
def NounPhrase(type: str = "prep"):
    result = ""

    if (type == "verb"):
        if (not coinToss()):
            result = f"{Determinants()} {AdjecivePhrase()} {Noun()} {PrepositionalPhrase()}"
    else:
        result = f"{Determinants()} {AdjecivePhrase()} {Noun()} {PrepositionalPhrase()}"
    
    return result

def VerbPhrase():
    return f"{AuxiliaryVerb()} {Verb()} {NounPhrase('verb')} {PrepositionalPhrase()} {AdverbialPhrase()}"

# optional can return an empty string
def AdjecivePhrase():
    result = ""
    if coinToss():
        result = f"{AdverbialPhrase()} {Adjective()}"
    return result

# optional can return an empty string
def PrepositionalPhrase():
    result = ""
    if coinToss():
        result = f"{Preposition()} {NounPhrase('prep')}"
    return result

# adverbial phrase is optional and sometimes returns an empty string
def AdverbialPhrase():
    result = ""
    if coinToss():
        result = f"{ModifyingAdverb()} {Adverb()}"
    return result

## optional can return an empty string
def Determinants():
    result = ""
    if coinToss():
        determinants = getData("Determinants")
        result = randomFromList(determinants)
    return result

def Noun():
    nouns = getData("Nouns")
    return randomFromList(nouns)

# Auxiliary berbs are optional and can return an empty string
def AuxiliaryVerb():
    result = ""
    if coinToss():
        auxverbs = getData("AuxiliaryVerb")
        result = randomFromList(auxverbs)
    return result

def Verb():
    verbs = getData("Verb")
    return randomFromList(verbs)

def Adjective():
    adj = getData("Adjective")
    return randomFromList(adj)

def Preposition():
    preposition = getData("Preposition")
    return randomFromList(preposition)

## modifuing adverbs are sometimes optional and can return an empty string
def ModifyingAdverb():
    result = ""
    if coinToss():
        modifyingAdverb = getData("ModifyingAdverb")
        result = randomFromList(modifyingAdverb)
    
    return result

def Adverb():
    adverb = getData("Adverb")
    return randomFromList(adverb)

def main():
    ## here we will be generating the sentences
    print(Sentence())

if __name__ == "__main__":
    main()
