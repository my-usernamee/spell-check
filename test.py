"""f = open("text.txt","rb")
content = f.read()
words = content.split()"""


def fun(dict_word,input_word):
    n=len(x)
    a_char=[]
    for letters in dict_word:
        a_char.append(letters)

    m=len(dict_word)
    old=[]
    if a_char[0]==lst[0]:
        for i in range(0,m):
            old.append(i)
    else:
        for i in range(1,m+1):
            old.append(i)
            
    for i in range (1,n):
        new =[i]
        for j in range (1,m):
            j_oo=j-1
            rd1=old[j_oo]       #rd is row data just a variable
            rd2=old[j]
            rd3=new[j_oo]
            mini = min(rd1,rd2,rd3)
            mini_oo = mini+1
            if a_char[j]==lst[i]:
                new.append(rd1)
            else:
                new.append(mini_oo)
        old=new
    m_oo= m-1
    offset= old[m_oo]
    semi_final_list=[]
    semi_final_list.append(dict_word)
    semi_final_list.append(offset)
    final_list.append(semi_final_list)

x=input("enter string: ")
lst=[]
for letters in x:
    lst.append(letters)
n=len(x)

final_list=[]

for word in words:
    fun(word,x)

final_list.sort(key = lambda x:x[1])
print(final_list[0:20])

    


