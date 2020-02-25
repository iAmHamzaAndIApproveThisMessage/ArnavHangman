from __future__ import print_function
updatedSpaces=['-','-','-','-','-']
word='steve'
lives=5
def check(letter):
    global lives
    global updatedSpaces
    global word
    if letter in word:
        for i in range(0,len(word)-1):
            Hamza=word.find(letter, i, len(word))
            if Hamza != -1:
                updatedSpaces[Hamza]=letter
    else:
        lives=lives-1
        print('Not in word,', lives, 'lives left!')
    print(updatedSpaces)
        
        
        
        
    
        
        
    

        
