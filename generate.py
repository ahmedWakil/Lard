def Sentence():
    return NounPhrase() + VerbPhrase()

def NounPhrase():
    return Determinants() + AdjecivePhrase() + Noun() + PrepositionalPhrase()

def VerbPhrase():
    return AuxiliaryVerb() + Verb() + NounPhrase() + PrepositionalPhrase() + AdverbialPhrase()

def AdjecivePhrase():
    return AdverbialPhrase() + Adjective()

def PrepositionalPhrase():
    return Preposition() + NounPhrase()

def AdverbialPhrase():
    return ModifyingAdverb() + Adverb()

def Determinants():
    pass

def Noun():
    pass

def AuxiliaryVerb():
    pass

def Verb():
    pass

def Adjective():
    pass

def Preposition():
    pass

def ModifyingAdverb():
    pass

def Adverb():
    pass
