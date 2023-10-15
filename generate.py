import json
import random

def getData(wordType: str):
    ## read the words json file and then return the word list with that word type
    with open('Data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)

    return words[wordType]

def Sentence():
    sentence =  f"{NounPhrase()} {VerbPhrase()}"
    sentence[0] = sentence[0].upper()
    return sentence

# noun phrase in only optional for a verb phrase but mandetory for a prepositional phrase
# so depending on the type you handle each case differently
def NounPhrase(type: str):
    return f"{Determinants()} {AdjecivePhrase()} {Noun()} {PrepositionalPhrase()}"

def VerbPhrase():
    return f"{AuxiliaryVerb()} {Verb()} {NounPhrase()} {PrepositionalPhrase()} {AdverbialPhrase()}"

# optional can return an empty string
def AdjecivePhrase():
    return f"{AdverbialPhrase()} {Adjective()}"

# optional can return an empty string
def PrepositionalPhrase():
    return f"{Preposition()} {NounPhrase()}"

# optional adverbial phrase is optional and sometimes returns an empty string
def AdverbialPhrase():
    return f"{ModifyingAdverb()} {Adverb()}"

## optional can return an empty string
def Determinants():
    determinants = getData("Determinants")

def Noun():
    nouns = getData("Nouns")
    index = random.randint(0, len(nouns) - 1)
    return nouns[index]

# Auxiliary berbs are optional and can return an empty string
def AuxiliaryVerb():
    auxverbs = getData("AuxiliaryVerb")

def Verb():
    verbs = getData("Verb")
    index = random.randint(0, len(verbs) - 1)
    return verbs[index]

def Adjective():
    adj = getData("Adjective")
    index = random.randint(0, len(adj) - 1)
    return adj[index]

def Preposition():
    preposition = getData("Preposition")
    index = random.randint(0, len(preposition) - 1)
    return preposition[index]

## modifuing adverbs are sometimes optional and can return an empty string
def ModifyingAdverb():
    modifyingAdverb = getData("ModifyingAdverb")

def Adverb():
    adverb = getData("Adverb")
    index = random.randint(0, len(adverb) - 1)
    return adverb[index]

def main():
    ## here we will be generating the sentences
    print(Noun())

if __name__ == "__main__":
    main()
