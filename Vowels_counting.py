sentence = input("Enter your sentence : ").lower()
vowels = "aeiou"


count = {}

for ch in sentence:
    if ch in vowels :
        if ch in count:
            count[ch] +=1
        else : 
            count[ch] = 1
            
    
for  vowels , freq in count.items():          
    
    print(vowels, "->" , freq)

