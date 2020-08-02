#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import time
    

def get_random_number_for_right_deck(deck_list):
    value = np.random.choice(deck_list)
    return value

def display_distribution(deck_distribution, distribution_title):
    left_deck = []
    right_deck = []
    for cnt ,x in enumerate(deck_distribution):
        if 'L' in x:
            left_deck.append(cnt)
        else:
            right_deck.append(cnt)
    n_bins = 10            
    colors = ['red','blue']        
    labels = ['left','right']

    left_deck.sort()
    right_deck.sort()
    x = [left_deck, right_deck]
    plt.title(distribution_title, fontsize=30)
    plt.hist(x, n_bins, density=True, histtype='bar', color=colors, label=labels)
    plt.legend(prop={'size': 10})
   # plt.set_title('bars with legend')
    plt.show()
    plt.clf()
    #print (deck_distribution)
    
def should_drop_from_right_deck(left_deck, right_deck):
    deck_index =  np.random.choice(np.hstack((left_deck,right_deck)))
    if deck_index in left_deck:
        return False
    return True

def shuffle(deck_list):
    i = 0
    random_value = get_random_number_for_right_deck(deck_list)

    left_deck, right_deck = np.array(['L'+str(x) for x in range(0, random_value)]), np.array(['R'+str(x) for x in range(random_value, len(deck_list))])

    display_distribution(np.hstack((left_deck,right_deck)),'un shuffled deck')

    while True:
        shuffled_deck = []
    

        first_deck = should_drop_from_right_deck(left_deck, right_deck)
        j = len(right_deck)-1
        k = len(left_deck)-1
        while j>=0 and k>=0:
            if first_deck ==True and j>=0:
                shuffled_deck.append(right_deck[j])
                j-=1
                first_deck = False    
            elif first_deck == False and k>=0:
                shuffled_deck.append(left_deck[k])
                k-=1
                
                first_deck = True
    
            #first_deck = should_drop_from_right_deck(left_deck, right_deck)
            
        
        if (k>=0):
            rem_l_deck = left_deck[:k+1]
            rem_l_deck = rem_l_deck[::-1]
            shuffled_deck.extend(rem_l_deck)
        if (j>=0):
            rem_r_deck = right_deck[:j+1]
            rem_r_deck = rem_r_deck[::-1]
            shuffled_deck.extend(rem_r_deck)
        
        prev_elm = ''
        index_li = []
        for elm in shuffled_deck:
            if (not prev_elm):
                prev_elm = elm
                continue
            #print (prev_elm[0], elm[0])
    
            if prev_elm[0]==elm[0]:
                index_li.append(elm)
            prev_elm = elm
            
        if (len(index_li)*100/len(shuffled_deck))<10:
            break
        
        #if (i>10):break    
        random_value = get_random_number_for_right_deck(deck_list)

        left_deck, right_deck = np.array(['L'+str(x) for x in range(0, random_value)]), np.array(['R'+str(x) for x in range(random_value, len(deck_list))])
        i+=1  
    display_distribution(shuffled_deck,'shuffled_deck')    
    print ("No. of shuffles", i+1)
    return shuffled_deck    
            
print ("Enter Number of deck")        
total_no = int(input())    

st = time.time()
print ("total no of cards in deck", total_no)
input_deck = np.array(range(0, total_no))
shuffled_deck = shuffle(input_deck)
print ("Time Taken", (time.time()-st))
#print (shuffled_deck)
#plt.show()


# In[ ]:





# ###### 

# In[ ]:





# In[ ]:





# In[ ]:




