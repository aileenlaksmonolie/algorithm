#!/usr/bin/env python
# coding: utf-8

# In[1]:


from networkx.generators.random_graphs import erdos_renyi_graph
import operator
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
import pandas as pd
import random
import time
import queue


# # Generate Random Graph

# In[10]:


n=50
p = 0.5
g = erdos_renyi_graph(n, p)
#to file
node1=[]
node2=[]
for x in g.edges:
    node1.append(x[0])
    node2.append(x[1])
node=[node1,node2]
with open("randomgraphfile.txt", "w") as file:
    count=0
    while count<160:
        file.write('\n')
        count+=1
    for x in zip(*node):
        file.write("{0}\t{1}\n".format(*x))
file.close() 

my_file = open("randomgraphfile.txt")
file_contents = my_file.read()
file_contents = file_contents[160:]
data = StringIO(file_contents)
df = pd.read_csv(data, sep="\t")
records = df.to_records(index=False)
result=list(records)

nodes=0
for x in result:
    for y in x:
        if y>nodes:
            nodes=y


# # Use Real Graph

# In[11]:


my_file = open("roadPA.txt")
file_contents = my_file.read()
file_contents = file_contents[160:]

data = StringIO(file_contents)
df = pd.read_csv(data, sep="\t")
records = df.to_records(index=False)


# # Generating Hospital IDX

# In[12]:


value1 = int(input("Please enter the number of hospitals to be generated :\n"))


# In[13]:


hospitals =[]
no_of_hospitals =value1
print("Number of hospital is", end = " ")
print(no_of_hospitals)

i=0
while (i <no_of_hospitals): 
    randomint = random.randint(0,no_of_hospitals)
    if((randomint not in hospitals)==True):
        hospitals.append(randomint)
        i+=1
    else:
        continue    
print("The hospitals are: ", end = " ")
print(hospitals)

file2 = open('myhospitalfile.txt', 'w')
file2.writelines('# '+str(no_of_hospitals)+'\n')
for x in hospitals:
    file2.writelines(str(x) +'\n')
file2.close() 


my_file2 = open("myhospitalfile.txt")
file_contents2 = my_file2.read()
file_contents2 = file_contents[1:]

data_hosp = StringIO(file_contents2)
df = pd.read_csv(data_hosp, sep="\n")
records = df.to_records(index=False)
result = []
for x in records:
    if type(x)==str:
        result.append(int(x))
    else:
        result.append(x)


# # Part (a)

# In[16]:


def bfsa(g, h):
    my_file = open(g)
    file_contents = my_file.read()
    file_contents = file_contents[160:]

    data = StringIO(file_contents)
    df = pd.read_csv(data, sep="\t")
    records = df.to_records(index=False)
    result = []
    for x in records:
        if type(x)==str:
            result.append(int(x))
        else:
            result.append(x)
    graph=result    
    my_file2 = open(h)
    file_contents2 = my_file2.read()
    file_contents2 = file_contents2[1:]

    data_hosp = StringIO(file_contents2)
    df = pd.read_csv(data_hosp, sep="\n")
    hospital_list = list(df.iloc[:,0])
    
    nodes=0
    for x in graph:
        for y in x:
            if y>nodes:
                nodes=y
                
    finallst=[]
    arrangedbynode=[]
    for x in range(nodes+1):
        for y in range(nodes+1):
            start=x
            end=y
            q = queue.Queue()
            path = [start]
            q.put(path)
            visited = set([start])
            while not q.empty():
                path = q.get()
                last_node = path[-1]
                if last_node == end:
                    distance=len(path)-1
                    lst=[start,end,path,distance]
                    finallst.append(lst)
                for node in graph[last_node]:
                    if node not in visited:
                        visited.add(node)
                        q.put(path + [node])
    for idx in range(nodes+1):
        interm=[]
        for r in finallst:
            node=r[0]
            if node==idx:
                hos=r[1]
                if hos in hospital_list:
                    interm.append(r)
        arrangedbynode.append(interm)
    shortest=[]
    for eachnode in arrangedbynode:
        sorted_list = sorted(eachnode, key=operator.itemgetter(3))
        shortest.append(sorted_list[0])
    node1=[]
    node2=[]
    node3=[]
    node4=[]
    for each in shortest:
        node1.append(each[0])
        node2.append(each[1])
        node3.append(each[2])
        node4.append(each[3])
    node=[node1,node2,node3,node4]
    with open("parta.txt", "w") as file:
        for x in zip(*node):
            file.write("{0}\t{1}\t{2}\t{3}\n".format(*x))
    file.close() 
    return shortest


# In[17]:


start_time = time.time()

lstofdist=bfsa('randomgraphfile.txt','myhospitalfile.txt')
print(lstofdist)
print("--- %s seconds ---" % (time.time() - start_time))


# # Part (c)

# In[30]:


def bfsc(g, h):
    my_file = open(g)
    file_contents = my_file.read()
    file_contents = file_contents[160:]

    data = StringIO(file_contents)
    df = pd.read_csv(data, sep="\t")
    records = df.to_records(index=False)
    result = []
    for x in records:
        if type(x)==str:
            result.append(int(x))
        else:
            result.append(x)
    graph=result    
    my_file2 = open(h)
    file_contents2 = my_file2.read()
    file_contents2 = file_contents2[1:]

    data_hosp = StringIO(file_contents2)
    df = pd.read_csv(data_hosp, sep="\n")
    hospital_list = list(df.iloc[:,0])
    
    nodes=0
    for x in graph:
        for y in x:
            if y>nodes:
                nodes=y
                
    finallst=[]
    for x in range(nodes+1):
        for y in range(nodes+1):
            start=x
            end=y
            q = queue.Queue()
            path = [start]
            q.put(path)
            visited = set([start])
            while not q.empty():
                path = q.get()
                last_node = path[-1]
                if last_node == end:
                    distance=len(path)-1
                    lst=[start,end,path,distance]
                    finallst.append(lst)
                for node in graph[last_node]:
                    if node not in visited:
                        visited.add(node)
                        q.put(path + [node])
    arrangedbynode=[] 
    for idx in range(nodes+1): #TRAVERSE ALL THE NODES IN THE GRAPH
        interm=[]
        for r in finallst:
            node=r[0]
            if node==idx:
                hos=r[1]
                if hos in hospital_list: #APPENDS ALL THE SHORTEST DISTANCE FROM NODE TO ALL HOSPITAL
                    interm.append(r)
        arrangedbynode.append(interm)
    shortest=[]
    for eachnode in arrangedbynode: #TRAVERSE ALL THE NODES IN THE GRAPH
        sorted_list = sorted(eachnode, key=operator.itemgetter(3)) #SORT THE DISTANCES FROM EACH HOSPITAL TO A PARTICULAR NODE
        for i in range(2):#RETURNS TOP 2 NEAREST HOSPITAL #(ABLE TO CHANGE THIS TO K NEAREST HOSPITAL)
            shortest.append(sorted_list[i])
            print(sorted_list[i])
    node1=[]
    node2=[]
    node3=[]
    node4=[]
    for each in shortest:
        node1.append(each[0])
        node2.append(each[1])
        node3.append(each[2])
        node4.append(each[3])
    node=[node1,node2,node3,node4]
    with open("partc.txt", "w") as file:
        for x in zip(*node):
            file.write("{0}\t{1}\t{2}\t{3}\n".format(*x))
    file.close() 
    return shortest


# In[31]:


start_time = time.time()

lstofdist=bfsc('randomgraphfile.txt','myhospitalfile.txt')
print("--- %s seconds ---" % (time.time() - start_time))


# # Part (d)

# In[20]:


def bfsd(g, h, k):
    my_file = open(g)
    file_contents = my_file.read()
    file_contents = file_contents[160:]

    data = StringIO(file_contents)
    df = pd.read_csv(data, sep="\t")
    records = df.to_records(index=False)
    result = []
    for x in records:
        if type(x)==str:
            result.append(int(x))
        else:
            result.append(x)
    graph=result    
    my_file2 = open(h)
    file_contents2 = my_file2.read()
    file_contents2 = file_contents2[1:]

    data_hosp = StringIO(file_contents2)
    df = pd.read_csv(data_hosp, sep="\n")
    hospital_list = list(df.iloc[:,0])
    
    nodes=0
    for x in graph:
        for y in x:
            if y>nodes:
                nodes=y
                
    finallst=[]
    for x in range(nodes+1):
        for y in range(nodes+1):
            start=x
            end=y
            q = queue.Queue()
            path = [start]
            q.put(path)
            visited = set([start])
            while not q.empty():
                path = q.get()
                last_node = path[-1]
                if last_node == end:
                    distance=len(path)-1
                    lst=[start,end,path,distance]
                    finallst.append(lst)
                for node in graph[last_node]:
                    if node not in visited:
                        visited.add(node)
                        q.put(path + [node])
    arrangedbynode=[]
    for idx in range(nodes+1):
        interm=[]
        for r in finallst:
            node=r[0]
            if node==idx:
                hos=r[1]
                if hos in hospital_list:
                    interm.append(r)
        arrangedbynode.append(interm)
    shortest=[]
    for eachnode in arrangedbynode:
        sorted_list = sorted(eachnode, key=operator.itemgetter(3))
        for i in range(k):
            shortest.append(sorted_list[i])
    node1=[]
    node2=[]
    node3=[]
    node4=[]
    for each in shortest:
        node1.append(each[0])
        node2.append(each[1])
        node3.append(each[2])
        node4.append(each[3])
    node=[node1,node2,node3,node4]
    with open("partd.txt", "w") as file:
        for x in zip(*node):
            file.write("{0}\t{1}\t{2}\t{3}\n".format(*x))
    file.close() 
    return shortest


# In[23]:


k = int(input("How many nearest hospitals do you want the path and distance to? : \n"))


# In[24]:


start_time = time.time()

lstofdist=bfsd('randomgraphfile.txt','myhospitalfile.txt',k)
print(lstofdist)
print("--- %s seconds ---" % (time.time() - start_time))


# In[ ]:




