#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 벅스 크롤링 https://music.bugs.co.kr/chart


# In[78]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# In[24]:


url = "https://music.bugs.co.kr/chart"
html = requests.get(url)

print(html)


# In[26]:


print(html.text)


# In[30]:


soup = bs(html.text)


# In[32]:


len(soup.select('tr'))


# In[33]:


len(soup.select('tbody > tr'))


# In[34]:


len(soup.select('table > tbody > tr'))


# In[36]:


len(soup.select('table.byChart > tbody > tr'))


# In[38]:


songs = soup.select('table.byChart > tbody > tr')


# In[40]:


song = songs[0]


# In[41]:


print(song)


# In[42]:


len(song.select('a'))


# In[43]:


len(song.select(' p > a'))


# In[44]:


print(song.select(' p > a'))


# In[49]:


title = song.select('p.title > a')
print(title)


# In[51]:


title = song.select('p.title > a')[0].text
print(title)


# In[55]:


singer = song.select('p.artist > a')[0].text
print(singer)


# In[72]:


songs = soup.select('table.byChart > tbody > tr')

song = songs[2]

title2 = song.select('p.title > a')[0].text
singer2 = song.select('p.artist > a')[0].text

print(title2)
print(singer2)


# In[84]:


song_data = []
rank = 1


url = "https://music.bugs.co.kr/chart"
html = requests.get(url)
soup = bs(html.text)
songs = soup.select('table.byChart > tbody > tr')


for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    song_data.append(['Bugs' , rank, title, singer])
    rank += 1
    

df = pd.DataFrame(song_data, columns = ['서비스','순위', '노래제목', '가수명'])

df.to_excel('Bugs.xlsx', index=False)


# In[ ]:


#판다시 안될때
# pip install pandas


# In[ ]:


#멜론 차트


# In[ ]:




