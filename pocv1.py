import json
import hashlib

    
def Alphabet():
    upperalphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    loweralphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    n = ["1","2","3","4","5","6","7","8","9","0"]
    all = upperalphabet + loweralphabet + n
    return all
    
dict={}

for i in range(0,len(Alphabet())):
    v1 = Alphabet()[i]
    result = hashlib.sha1(v1.encode()).hexdigest()
    dict[result] = v1

print(dict)

#with open('data.json', 'w') as outfile:
#    json.dump(dict, outfile)
