import numpy as np
print('BoW - Bag Of Words (To count word frequency in a string)\n\n')
check=0
print(':::Enter:::\n')
temp=''
while check==0:
    size=len(temp)
    string=input()
    temp+=' '+string.lower()
    if size==len(temp)-1:
        break
 
print('Here is the list of words and their frequencies in this string of',len(temp),'entries in total\n')
List=list(temp.split(' '))
Repeated=[]
mostCount=0
mostString=""
for i in range(0,len(List)):
    count=0
    if List[i] not in Repeated and List[i]!='':
        Repeated.append(List[i])
        print(List[i]+'--->',end='')
        for j in range(i+1,len(List)):
            if List[i]==List[j]:
                count+=1
                
        print(count+1,end='\n')
        if mostCount<count+1:
            mostCount=count+1
            mostString=List[i]
    

print('\n\nThe most repeated word is {',mostString,'} with its repeatition of {',mostCount,'} times\n\n')
    
