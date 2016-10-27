import os
import math
import sys

d_spam={}
d_ham={}  
f=open("nbmodel.txt","r",encoding="latin1")
lines=f.readlines()
count_spam_train=lines[0]
count_ham_train=lines[1]
count_word_spam_train=lines[2]
count_word_ham_train=lines[3]
total_dict_word_train=lines[4]

count_spam_train=(int)(count_spam_train)
count_ham_train=(int)(count_ham_train)
count_word_spam_train=(int)(count_word_spam_train)
count_word_ham_train=(int)(count_word_ham_train)
total_dict_word_train=(int)(total_dict_word_train)

total_file_ham_spam=count_spam_train+count_ham_train
total_word_ham_spam=count_word_spam_train+count_word_ham_train


if total_file_ham_spam!=0:
    prob_spam=(count_spam_train/total_file_ham_spam)
else:
    prob_spam=0
    
if total_file_ham_spam!=0:
    prob_ham=(count_ham_train/total_file_ham_spam)

for i in range(5, len(lines)):
        data = lines[i].split()
        d_spam[data[0]]=data[1]
        d_ham[data[0]]=data[2]     
r=[]
count_dev_file=0
dev_spam_file=0
dev_ham_file=0
p = open('nboutput.txt','w+',encoding="latin1")  
# for root, dirs, files in os.walk('D:\Spam_or_Ham\dev'):
for root, dirs, files in os.walk(sys.argv[1]):
    for file in files:
        if  file.endswith(".txt"):
            if "spam.txt" in file:
                dev_spam_file=dev_spam_file+1
            if "ham.txt" in file:
                dev_ham_file=dev_ham_file+1  
            f=os.path.join(root, file)
            file_name = open(f, 'r', encoding = 'latin1')
            count_dev_file=count_dev_file+1
            prob_msg_spam=0
            prob_msg_ham=0
            for line in file_name:
                line.strip()
                for l in line.split():
                    if(l in  d_spam.keys() or l in  d_ham.keys()):
                        if(l in d_spam.keys()):
                            prob_msg_spam= prob_msg_spam + math.log((int(d_spam[l])+1)/(total_dict_word_train+count_word_spam_train))
                        else:
                            prob_msg_spam=(prob_msg_spam)+math.log(((int)(0+1))/(total_dict_word_train+count_word_spam_train))
                        if(l in d_ham.keys()):
                            prob_msg_ham=(prob_msg_ham)+math.log(((int)(d_ham[l])+1)/(total_dict_word_train+count_word_ham_train))
                        else:
                            prob_msg_ham=(prob_msg_ham)+math.log(((int)(0+1))/(total_dict_word_train+count_word_ham_train))
                                
            prob_final_spam_file=math.log(prob_spam)+(prob_msg_spam)
            prob_final_ham_file=math.log(prob_ham)+(prob_msg_ham) 
            if(prob_final_spam_file>prob_final_ham_file):
                p.write("SPAM"+' '+str(f)+"\n")
                print("SPAM")
            elif(prob_final_spam_file<prob_final_ham_file):
                p.write("HAM"+"  "+str(f)+"\n")
                print("HAM")

p.close()
 
# 
# ###### Accuracy
count=0
g=open('nboutput.txt','r')
lines=g.readlines()
for line in lines:
    line=line.split()
    if line[0]=="SPAM" and "spam.txt" in line[1]:
        count=count+1
    if line[0]=="HAM" and "ham.txt" in line[1]:
        count=count+1
 
accuracy=(count/count_dev_file)*100
print(accuracy)
# 
# ######### Pricision count for SPAM
pre_spam_path_label=0
pre_spam_count=0
g=open('nboutput.txt','r')
lines=g.readlines()
for line in lines:
    line=line.split()
    if line[0]=="SPAM" and "spam.txt" in line[1]:
        pre_spam_path_label=pre_spam_path_label+1
    if line[0]=="SPAM":
        pre_spam_count=pre_spam_count+1
g.close()
precision_spam=(pre_spam_path_label/pre_spam_count)
 
print(precision_spam , " Precision SPAM")
 
# ######### Pricision count for HAM
pre_ham_path_label=0
pre_ham_count=0
g=open('nboutput.txt','r')
lines=g.readlines()
for line in lines:
    line=line.split()
    if line[0]=="HAM" and "ham.txt" in line[1]:
        pre_ham_path_label=pre_ham_path_label+1
    if line[0]=="HAM":
        pre_ham_count=pre_ham_count+1
 
precision_ham=(pre_ham_path_label/pre_ham_count)
g.close()
print(precision_ham, " Precision HAM")
# 
# ######### Recall of SPAM
pre_spam_path_label=0
g=open('nboutput.txt','r')
lines=g.readlines()
for line in lines:
    line=line.split()
    if line[0]=="SPAM" and "spam.txt" in line[1]:
        pre_spam_path_label=pre_spam_path_label+1
  
recall_spam=(pre_spam_path_label/dev_spam_file)
g.close()
print(recall_spam, "Recall SPAM")
#  
# # ######### Recall of HAM
pre_ham_path_label=0
g=open('nboutput.txt','r')
lines=g.readlines()
for line in lines:
    line=line.split()
    if line[0]=="HAM" and "ham.txt" in line[1]:
        pre_ham_path_label=pre_ham_path_label+1
  
recall_ham=(pre_ham_path_label/dev_ham_file)
g.close()
print(recall_ham, "Recall HAM")
# 
# ########## Evaluation for SPAM
F_SPAM=((2*precision_spam*recall_spam)/(precision_spam+recall_spam))
F_HAM=((2*precision_ham*recall_ham)/(precision_ham+recall_ham))
 
print(F_SPAM,"F SPAM")
print(F_HAM,"F HAM")
