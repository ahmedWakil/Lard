import glob
import os
import codecs
import json

## Takes in a file name or a url to the file and then adds them to the
## words data file to be used in the generation
DATA_FILEPATH = "/Data"

def findFiles(path):
    return glob.glob(path)

## procedure for reading each word line by line
def readLines(filepath, ignore: set = {}):
    lines = []

    with codecs.open(filepath, encoding='utf-8') as f:
        for line in f:
            for i in ignore:
                line = line.replace(i, '')
            lines.append(line)

    return lines

## procedure for loading the data from the data folder 
def loadData(path, ignore: set = {}):
    data = {}
    all_catagories = []
    for file_url in findFiles(path):
        ## get all of the words in the file line by line
        words = readLines(file_url, ignore)
        ## the file name is going to be the key for this dictionary
        catagory = os.path.splitext(os.path.basename(file_url))[0]
        ## map the words to the type of english word it is which are the names of the files
        data[catagory] = words
        all_catagories.append(catagory)

    return (data, all_catagories)

def main():
    ## first load words.json if it does not exist it we will create a new file
    with open('Data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)

    print(words)

    ## then get the file names that are in data


    ## create a dictionary with the keys as the file names and the words
    ## in the file as the entries to a list which will be the value of the key

    ## add the words to the proper entries in the word.json file

    ## write the word.json file

if __name__ == "__main__":
    main()