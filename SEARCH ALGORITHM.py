#!/usr/bin/env python
# coding: utf-8

# In[1]:


#------------ALGORITHM LAB 1--------------#
#-----------------GROUP 1-----------------#
#---GROUP MEMBERS : ----------------------#

#Snehaa Rajkumar (U1921000H)
#Han Xiao (U1920108G)
#Aileen Laksmono Lie (U1920118E)
#Vivien Chew Jing Wen (U1922718D)
#Triston Low Zhi Yang (U1921229E)


# In[2]:


import time

NO_OF_CHARS = 256

def badCharHeuristic2(string, size): 
    badChar = [size]*NO_OF_CHARS 
    for i in range(size): 
        badChar[ord(string[size-(1+i)])] = size-(1+i); 

    return badChar 

def RBHSearch(text, word): 
    len_word = len(word) 
    len_text = len(text)
    badChar = badCharHeuristic2(word, len_word) 
    s = len_text#9
    index_list = []
    while(s >= len_word):
        pos = 0 #ABC POS = 2

        while pos<len_word and word[pos] == text[s-len_word + pos]: #ABCABCABC
            pos += 1
        if (pos ==len_word):
            index_list.append(s-len_word)
            s -= (1)
        else: 
            s -= max(1,(badChar[ord(text[s-len_word + pos])]-pos)) 
      
    return index_list[-10:]

def BFSearch(txt, pat): 
    ''' 
    A pattern searching function that uses Brute Force Algorithm 
    '''
    m = len(pat) 
    n = len(txt) 
    search_range=n-m
    count=0
    index_list = []

    for x in range(search_range+1):
        for y in range(m):
            if (txt[x+y]!=pat[y]):
                break;
            if (y==(m-1)):
                count+=1
                #print(x)
                index_list.append(x)

    if count==0:
        print('Nothing')
        
    return index_list[0:10]


def preprocess_inputseq(givenStr, m, arr):
    # set i and j/ j and i follow the indexes of the givenStr & not the int u input into the array
    # first ele is always 0
    # same = index of j +1 / inc both i and j
    # diff = check the input of ur arr bef j then jump there and compare / if compare after jumping back alrd = 0
    # i always inc by 1 but j by dec down

    i = 1
    j = 0
    while (i < m):  # eg. if givenStr's len = 4, then i shld run at least 3 times

        if givenStr[j] == givenStr[i]:  # if characters are the same
            arr.append(j + 1)
            j += 1
            i += 1

        else:  # if characters are different
            while (i < m and givenStr[j] != givenStr[i]):  # loop so that eg. AAAB, need to get j to go back to index 0 instead of index 1
                
                if (j == 0):  # consider the case where there's no character before j (where j is at index 0)
                    arr.append(0)
                    i += 1
                else:  # consider when there are characters infront of j (index of j is not 0）
                    j = arr[j - 1]

    return arr

def MOSearch(txt, givenStr):
    m = len(givenStr)
    n = len(txt)
    #print(m)
    #print(n)
    preprocessed_array = [0]
    j = 0  # index for givenStr[]

    # Preprocess the pattern (LPS array)
    preprocess_inputseq(givenStr, m, preprocessed_array) 

    i = 0  # index for txt[]
    index_list = []

    while i < n:
        if givenStr[j] == txt[i]: #match
            i += 1
            j += 1

        else: #mismatch
            if j != 0:
                j = preprocessed_array[j - 1]
            else:
                i += 1
        if j == m: #pattern found in txt
           # print("Found pattern at index " + str(i - j))
            index_list.append(str(i - j))
            j = preprocessed_array[j - 1]
            #print(index_list)
    return index_list[0:10]



# In[3]:


import tkinter as tk
from tkinter import filedialog


    
def UploadAction1():
    filename = filedialog.askopenfilename()
    my_file = open(filename)
    file_contents = my_file.read()
    file_contents = file_contents[71:]
    ans_list = []
    start_time = time.time()
    ans_list = BFSearch(file_contents, name_var.get())
   # print("--- %s seconds ---" % (time.time() - start_time))
    label = tk.Label(root, text = "It occured at positions :") 
    name_label2 = tk.Label(root,text ="RUN TIME (Brute Force Algorithm) :  %s seconds " % (time.time() - start_time))
    name_label2.pack(padx = 50, pady =10)
    name_label2.config(font=("Times New Roman", 18))
    ans_label = tk.Label(root, text=ans_list)
    # this creates x as a new label to the GUI
    label.pack() 
    ans_label.pack()
    nameentrybox.delete(0, tk.END)


def UploadAction2():
    filename = filedialog.askopenfilename()
    my_file = open(filename)
    file_contents = my_file.read()
    file_contents = file_contents[71:]
    ans_list = []
    start_time = time.time()
    ans_list = RBHSearch(file_contents, name_var.get())
   # print("--- %s seconds ---" % (time.time() - start_time))
    label = tk.Label(root, text = "It occured at positions :") 
    name_label2 = tk.Label(root,text ="RUN TIME (Reverse Bad Heuristic Algorithm) :  %s seconds " % (time.time() - start_time))
    name_label2.config(font=("Times New Roman", 18))
    name_label2.pack(padx = 50, pady =10)
    ans_label = tk.Label(root, text=ans_list)
    # this creates x as a new label to the GUI
    label.pack() 
    ans_label.pack()
    nameentrybox.delete(0, tk.END)

def UploadAction3():
    filename = filedialog.askopenfilename()
    my_file = open(filename)
    file_contents = my_file.read()
    file_contents = file_contents[71:]
    ans_list = []
    start_time = time.time()
    ans_list = MOSearch(file_contents, name_var.get())
   # print("--- %s seconds ---" % (time.time() - start_time))
    label = tk.Label(root, text = "It occured at positions :") 
    name_label2 = tk.Label(root,text ="RUN TIME (Match Observation Algorithm) :  %s seconds " % (time.time() - start_time))
    name_label2.config(font=("Times New Roman", 18))
    name_label2.pack(padx = 50, pady =10)
    ans_label = tk.Label(root, text=ans_list)
    # this creates x as a new label to the GUI
    label.pack() 
    ans_label.pack()
    nameentrybox.delete(0, tk.END)


root = tk.Tk()

root.title('DNA & protein sequence searching')    

name_label = tk.Label(root,text = "Enter query sequence : ")
name_label.pack(padx = 50, pady =10)


name_var = tk.StringVar()
nameentrybox = tk.Entry(root, width = 16, textvariable = name_var)
nameentrybox.pack(padx = 50, pady= 10)

button = tk.Button(root, text='Open and compare (Reverse Bad Heuristic)', command=UploadAction2)
button.pack()

button2 = tk.Button(root, text='Open and compare (Brute Force)', command=UploadAction1)
button2.pack()


button3 = tk.Button(root, text='Open and compare (MOS)', command=UploadAction3)
button3.pack()

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




