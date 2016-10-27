import os
import sys

### Code for SPAM

count_spam=0
count_ham=0
count_word_spam=0
count_word_ham=0
dictonary_spam={}

def tocken_spam(f):
    global count_word_spam
    f_spam_name=open(f, 'r',encoding="latin1")
    content=f_spam_name.readlines()
    for line in content:
        line=line.strip().split()
        for word in line: 
                if word not in dictonary_spam.keys():
                    dictonary_spam[word]=1
                    count_word_spam=count_word_spam+1
                else:
                    dictonary_spam[word]=dictonary_spam[word]+1
                    count_word_spam=count_word_spam+1
             
##### Walk through from Main Directoyr to TXT file   
for root, dirs, files in os.walk('.'):
    for d in dirs:
        os.path.join(root,d)
    for file in files:
            f=os.path.join(root, file)
            if "spam" in f and "__MACOSX" not in f and f.endswith(".txt") and "dev" not in f:
                count_spam=count_spam+1;
                tocken_spam(f)
print(count_spam)

#####-------------------------------------------------Code for HAM---------------------------------------------------------########

##### CODE for HAM    
dictonary_ham={}

def tocken_ham(f):
    global count_word_ham
    f_name=open(f, 'r',encoding="latin1")
    content=f_name.readlines()
    for line in content:
        line=line.strip().split()
        for word in line: 
                if word not in dictonary_ham.keys():
                    dictonary_ham[word]=1
                    count_word_ham=count_word_ham+1
                else:
                    dictonary_ham[word]=dictonary_ham[word]+1
                    count_word_ham=count_word_ham+1

         
##### Walk through from Main Directoyr to TXT file   
for root, dirs, files in os.walk('.'):
    for file in files:
            f=os.path.join(root, file)
            if "ham" in f and "__MACOSX" not in f and f.endswith(".txt") and "train" in f:
                count_ham=count_ham+1
                tocken_ham(f)
                
# print(dictonary_ham)                          
with open('nbmodel.txt', 'w+',encoding="latin1") as f:
    f.write(str(count_spam)+'\n')
    f.write(str(count_ham)+'\n')
    f.write(str(count_word_spam)+'\n')
    f.write(str(count_word_ham)+'\n')
    d={}
    set_words = set(dictonary_spam.keys()|dictonary_ham.keys())
    total_dict_word_train=len(set_words)
    f.write(str(total_dict_word_train)+'\n')
    for key in set_words:
        if key in dictonary_spam.keys():
            value_spam=dictonary_spam[key]
        else:
            value_spam=0
        if key in dictonary_ham.keys():
            value_ham=dictonary_ham[key]
        else:
            value_ham=0
         
        f.write(str(key)+' '+str(value_spam)+' '+str(value_ham)+"\n")
    f.close()    
print(count_ham)
print(count_word_spam)
print(count_word_ham)
print(total_dict_word_train)