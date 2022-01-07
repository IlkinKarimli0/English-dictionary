import json
from difflib import get_close_matches
import time

data =  json.load(open("FIrst_Program/data.json"))

def dictionary(word,data):
    if word in data:#cheking for entered input
        return data[word] 
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:#cheking for some special nouns
        return data[word.title()]
    elif get_close_matches(word,data.keys()):#smart check for suitable possibility 
        correction_of_word = str(input("Did you mean %s instead( ANSWER with [Y]   [N] "%get_close_matches(word,data.keys())[0]))
        if correction_of_word.lower() == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif correction_of_word.lower() == "n":
            print("\n The word "+ word +" does not exist")
            print("\n You can check instead:",end="    ")
            for c in range(1,len(get_close_matches(word,data.keys()))):
                print(get_close_matches(word,data.keys())[c],end="  ")
            return " "  
    else:
        return "This word is not exist"

    
def main():
    word =  str(input("Enter the word: ")).lower()
    output = dictionary(word,data)
    if isinstance(output,list):
        for i in output:
            print(i)
    else:
        print(output)

if __name__ == "__main__":
    main()




