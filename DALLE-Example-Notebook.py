#!/usr/bin/env python
# coding: utf-8

# ## Example Notebook with all of the Code from the Lecture (Just Needs an API Key)

# In[1]:


# Making sure OpenAI is install
get_ipython().system('pip install openai')


# In[2]:


# Bringing in Libraries
import os
import openai

# os.environ["OPENAI_API_KEY"] = "YOUR KEY GOES HERE"
# openai.api_key=os.getenv('OPENAI_API_KEY')


# ### Add API key below and delete cell after running

# In[3]:


# os.environ["OPENAI_API_KEY"] = "YOUR KEY GOES HERE"
# openai.api_key=os.getenv('OPENAI_API_KEY')


# In[4]:


from openai import OpenAI
client = OpenAI()


# In[5]:


# Create shopping list and recipe function
def create_shopping_list(recipe):
    prompt = f"Create a shopping list based on the following reciepe and goods that go well with it and cooking instructions: {(recipe)}"

    return prompt


# In[ ]:


# Function Test
recipe = create_shopping_list("Chipotle chicken and rice bowl")

print(recipe)


# ###  Remember this will be using your tokens to running repeated could result in fees

# In[ ]:


# Receaching out to OpenAI for the answer
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"system",
            "content": recipe
        },
    ],
    temperature = 0.7, ### Feel free to change hyperparameters
    top_p = 1,
)

print(response.choices[0].message.content)


# In[ ]:


# Putting the ingredients into a shopping list
import re

text = response.choices[0].message.content

pattern = re.compile(r'- (.+)')
matches = pattern.findall(text)

shopping_list = []

for match in matches:
    shopping_list.append(match)

print(shopping_list)


# In[ ]:


# Sending the item to DALLE 
image_response = client.images.generate(
    model ="dall-e-3",
    prompt=shopping_list[0],
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = image_response.data[0].url 

print(image_url)


# In[ ]:





# In[ ]:





# In[ ]:




