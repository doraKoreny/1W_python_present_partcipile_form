import sys

vowel = "aeuio"

if len(sys.argv) > 1:
    verb = sys.argv[1:]
    for item in verb:
        if item[-2:] == "ie":
            print(item[:-2] + "ying") 
        elif item[-1] == "e":
            print(item[:-1] + "ing")      
        elif item[-3] not in vowel and item[-2] in vowel and item[-1] not in vowel:
            print(item + item[-1] + "ing")
        else:
            print(item + "ing")