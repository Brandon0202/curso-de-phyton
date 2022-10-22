#!/usr/bin/env python
# coding: utf-8

# In[14]:


class agua():
    def __init__(self,is_alive=True,vida=150,tipo="agua",ataque=3):
        self.is_alive=is_alive
        self.vida=vida
        self.tipo= tipo
        self.ataque= ataque
    
    def __repr__(self):
        mensaje = f"""
        Tipo de Pokemon: {self.tipo}, 
        Vida: {self.vida}, 
        ataque: {self.ataque}"""
        return mensaje
    

    


# In[15]:


pipliop=agua()


# In[16]:


pipliop


# In[ ]:





# In[ ]:




