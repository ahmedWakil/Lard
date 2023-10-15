import json

def getData(wordType: str):
    ## read the words json file and then return the word list with that word type
    with open('Data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)

    return words[wordType]

def Sentence():
    sentence =  f"{NounPhrase()} {VerbPhrase()}"
    sentence[0] = sentence[0].upper()
    return sentence

def NounPhrase():
    return f"{Determinants()} {AdjecivePhrase()} {Noun()} {PrepositionalPhrase()}"

def VerbPhrase():
    return f"{AuxiliaryVerb()} {Verb()} {NounPhrase()} {PrepositionalPhrase()} {AdverbialPhrase()}"

# optional can return an empty string
def AdjecivePhrase():
    return f"{AdverbialPhrase()} {Adjective()}"

# optional can return an empty string
def PrepositionalPhrase():
    return f"{Preposition()} {NounPhrase()}"

def AdverbialPhrase():
    return f"{ModifyingAdverb()} {Adverb()}"

## optional can return an empty string
def Determinants():
    determinants = getData("Determinants")

def Noun():
    nouns = getData("Nouns")

def AuxiliaryVerb():
    auxverbs = getData("AuxiliaryVerb")

def Verb():
    verbs = getData("Verb")

def Adjective():
    adj = getData("Adjective")

def Preposition():
    preposition = getData("Preposition")

def ModifyingAdverb():
    modifyingAdverb = getData("ModifyingAdverb")

def Adverb():
    adverb = getData("Adverb")

def main():
    ## here we will be generating the sentences
    print("Hello world")

if __name__ == "__main__":
    main()
