import json
import hashlib

    
def Alphabet():
    upperalphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    loweralphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    n = ["1","2","3","4","5","6","7","8","9","0"]
    all = upperalphabet + loweralphabet + n
    return all
    




Alphabet_list=Alphabet()
allalphabet = []
dict={}
str = "a"
result=hashlib.sha1(str.encode()).hexdigest()
#dict[result.hexdigest()]=str
result2=hashlib.sha256(str.encode())
dict[result2.hexdigest()]=str

#print(allalphabet)

#for i in range(0,len(Alphabet_list)):
#    str = Alphabet_list[i]
#    result1=hashlib.sha1(str.encode())
#    dict[result1.hexdigest()]=str
    #allalphabet+= [result1.hexdigest()+" : "+Alphabet_list[i]]

#print(result)



#with open('data.json', 'w') as mon_fichier:
#    json.dump(dict, mon_fichier)



a = "1"
b = "2"

c = a + b

print(c)
