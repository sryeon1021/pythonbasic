#!/usr/bin/env python
# coding: utf-8

# In[18]:


print('%s자리수입나다.'%len(input()))
    


# In[20]:


a=input('put in number')
print(len(a),'자리수입니다')


# In[22]:


text='공백을 제외한 글자수만을 세는 코드 테스트'
 
print(len(text)-text.count(' '))   #텍스트 글자수 합에서 공백수를뺀값


# In[23]:


student=['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']
student.sort()    #이름 정렬
for i in range(len(student)):     #학생수를 range로 잡는다
    print('번호: {0},이름:{1}'.format(i+1,student[i]))     #번호 0에서 시작-> i 에 1더해서 1로 시작하게함 


# In[24]:


A=str('aacddddeee'.count('a')) #aacddddeee안에 있는 원하는 낱말의숫자를센고 문자형으로 바꿔준다
C=str('aacddddeee'.count('c'))
D=str('aacddddeee'.count('d'))
E=str('aacddddeee'.count('e'))
B=str('aacddddeee'.count('b'))
print(A+B+C+D+B+E+C+D)  #각 개수 숫자를 합해서 원하는 숫자형태를 만든다


# In[25]:


a= input().split(' ')
out=''
for i in a :
    out=out+i[0]
    print(out)
print(out)


# In[26]:


a=list(map(int,input().split()))   #값을 리스트 안에 정수로 저장, 공백을 기준으로 숫자입력
a.sort(reverse=True)  #내림차순으로 정렬
a[0]    #a값 0 으로 설정


# In[27]:


a=input()    #숫자입력
print(a.swapcase())   #CASE 바꾸는 함수입력


# In[ ]:




