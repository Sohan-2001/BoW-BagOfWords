
print('\n\nBoW - Bag Of Words (To count word frequency in a string)\n\n')

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
List=temp.split()

dictionary={}

for i in List:
    try:
        dictionary[i]+=1
    except:
        dictionary[i]=1
    
dictionary=sorted(dictionary.items(), key=lambda x: x[1])

for i,j in dictionary:
    if i!="":
        print(i,"-->",j)

print('\n\n')
