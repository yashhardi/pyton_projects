#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install openai')


# In[ ]:


import openai

openai.api_key = "#generate key from open ai key site"
model_engine = "text-davinci-002"
prompt = str(input("Enter your prompt: "))
completion = openai.Completion.create(
    engine=model_engine, prompt=prompt,
    max_tokens=1024, n=1, stop=None, temperature=0.9,
)
response = completion.choices[0].text
print(response)


# In[ ]:





# In[ ]:




