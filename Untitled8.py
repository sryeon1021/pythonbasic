#!/usr/bin/env python
# coding: utf-8

# In[2]:


#데이터 입력받아서처리
#숫자로입력받아서 처리
a=map(int,input().split())
print (a)


# In[3]:


a=[1,2,3,4]
b=[100,200,300,400]

print(list(zip(a,b)))

[(1,100), (2,200), (3,300),(4,400)]


# In[5]:


key=input().split()
value=map(int,input().split())
print(dict(zip(key, value)))


# In[6]:


txt=input() #phython 6글자 
for i in range(len(txt)):#6 
  


# In[ ]:


#알파벳 대문자: yes, otherwise No
alpha=input()
if alpha>=chr(65) and alpha <=chr(90):
    print('Yes')
else:
    print('No')


# In[9]:


a='pineapple is yummy'


print(a.find('pine'))


# In[11]:



txt=input()
a=list(txt.split())

print(len(a))
 


# In[12]:


txt=input()
a=list(txt.split())
print(len(a))


# In[15]:


txt=input()
txt2=list(txt.split())
txt3=[int(i) for i in txt2]

for i in range(len(txt3)-1,-1,-1):
    print(txt3[i], end=' ')


# In[23]:


multiples_2 = [n for n in range(1, 20) if n % 2 == 0]
multiples_2
        


# In[20]:


n= int(input())
for i in range (1m, b )


# In[21]:





# In[24]:


n=int(input())




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


a=input().split()
b=list(set(a))

max=0

for i in range(len(b)):  #0,1,2
    if a.count(b[i]) > a.count(b[max]):
        max= i
        
print('%s(이)가 총 %d 표로 반장이 되었습니다.'%(b[max, a.count(b[max])))


# In[ ]:





# In[ ]:


if re ==2:
    print('yes')
else:
    print('no')


# In[ ]:



print(sum(map(int,input())))


# In[ ]:


n=str.range(1:21)


# In[ ]:




