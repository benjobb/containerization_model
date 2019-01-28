
# coding: utf-8

# In[95]:


import pandas as pd
from scipy.optimize import linprog


# In[96]:


of = pd.read_csv('Inputs/Container Optimization Model Inputs - OF.csv')
of.columns = ['Savings']
objective_list = of['Savings'].tolist()


# In[97]:


rhs = pd.read_csv('Inputs/Container Optimization Model Inputs - RHS.csv')
rhs.columns = ['RHS']


# In[170]:


rhs


# In[143]:


consolidated_matrix = pd.read_csv('Inputs/Container Optimization Model Inputs - CM.csv')


# In[144]:


consolidated_matrix.head()


# In[145]:


consolidated_matrix.shape


# In[146]:


MinQty = 21 #count of min quantity contraint >=
MaxQty = 21 #count of max quantity contraint <=
ContCapLBSLB = 140 #count of container capacity lowerbound weight constaint >=
ContCapLBSUB = 140 #count of container capacity upperbound weight constaint <=
ContCapPalletLB = 140 #count of container capacity lowerbound pallet constaint >=
ContCapPalletUB = 140 #count of container capacity upperbound pallet constaint <=


# rep(">=",MinQty),rep("<=",MaxQty), 
#           rep(">=",ContCapLBSLB),rep("<=",ContCapLBSUB),
#           rep(">=",ContCapPalletLB),rep("<=",ContCapPalletUB))
MinQty+MaxQty+ContCapLBSLB+ContCapLBSUB+ContCapPalletLB+ContCapLBSUB


# In[174]:


counter = 0
consolidated_matrix = pd.read_csv('Inputs/Container Optimization Model Inputs - CM.csv')
rhs = pd.read_csv('Inputs/Container Optimization Model Inputs - RHS.csv')

print(consolidated_matrix[:MinQty].head())
print(rhs[:MinQty].head())

print('--')
consolidated_matrix[:MinQty] = consolidated_matrix[:MinQty]*-1
rhs[:MinQty] = rhs[:MinQty] * -1
print(consolidated_matrix[:MinQty].head())
print(rhs[:MinQty].head())
print('--')
counter += MinQty + MaxQty


# In[175]:


print("counter: ",counter)

print(consolidated_matrix[counter:counter+ContCapLBSLB].head())
print(rhs[counter:counter+ContCapLBSLB].head())

consolidated_matrix[counter:counter+ContCapLBSLB] = consolidated_matrix[counter:counter+ContCapLBSLB] *-1
rhs[counter:counter+ContCapLBSLB] = rhs[counter:counter+ContCapLBSLB] *-1
print(consolidated_matrix[counter:counter+ContCapLBSLB].head())
print(rhs[counter:counter+ContCapLBSLB].head())

counter += ContCapLBSLB + ContCapLBSUB
print('---')
print('counter:',counter)


# In[176]:


print(consolidated_matrix[counter:counter+ContCapPalletLB].head())
print(rhs[counter:counter+ContCapPalletLB].head())

consolidated_matrix[counter:counter+ContCapPalletLB] = consolidated_matrix[counter:counter+ContCapPalletLB] *-1
rhs[counter:counter+ContCapPalletLB] = rhs[counter:counter+ContCapPalletLB] *-1
print('--')
print(consolidated_matrix[counter:counter+ContCapPalletLB].head())
print(rhs[counter:counter+ContCapPalletLB].head())
print('counter:',counter)


# In[177]:


RHS_list = rhs['RHS'].tolist()


# In[178]:


consolidated_matrix.describe()


# In[179]:


c = [x * -1 for x in objective_list]
A = consolidated_matrix
b = RHS_list


# In[108]:


len(A)


# In[180]:


res = linprog(c,A_ub=A,b_ub=b, options={'disp':True})

print('')
print(res.x)


# In[190]:


Python_results = pd.DataFrame(res.x)


# In[191]:


R_results = pd.read_csv('Results/R Results.csv')['x']


# In[193]:


Python_results.columns = ['Python']


# In[194]:


Python_results['R'] = R_results


# In[195]:


Python_results

