#!/usr/bin/env python
# coding: utf-8

# In[2]:


from qiskit import QuantumCircuit, IBMQ
#from qiskit.assembler import disasseble
from qiskit.visualization import plot_histogram


# In[3]:


IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
melbourne = provider.get_backend('ibmq_16_melbourne')
print(melbourne)


# In[8]:


job = melbourne.retrieve_job('60632ca21b50b1ca732609fc')
counts = job.result().get_counts()[6]
#plot_histogram(counts)
#print(counts)


# In[9]:


x = dict(sorted(counts.items(), key=lambda item: item[1]))
print(x)


# In[ ]:




