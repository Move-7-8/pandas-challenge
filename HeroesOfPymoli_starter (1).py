#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[308]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
df = pd.read_csv(file_to_load)
df


# In[371]:


#Defining a DF that only includes one of each player. Keeping it at the top because
#it is used for a lot of code later on 
player = df.drop_duplicates(['SN'])


# ## Player Count

# * Display the total number of players
# 

# In[378]:


#Utilising the count function on a unique player list to find the no. of players
playercount = player['SN'].count()

uniques = pd.DataFrame({
    "Number of Players" : [playercount] 
})

uniques


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[355]:


#Defining relevant variables, performing calculations and creating a dataframe to hold 
#and display the information

unique_items = df['Item Name'].value_counts()

average_price = df['Price'].mean()
average_price = "${:,.2f}".format(average_price)

total_rev = df['Price'].sum()
total_rev = "${:,.2f}".format(total_rev)

pur_count = df['Item ID'].count()

pur_analysis = pd.DataFrame({
        "Unique Items" : [len(unique_items)],
        "Average Price" : [average_price],
        "Number of Purchases" : [pur_count],
        "Total revenues" : [total_rev]
        })

pur_analysis


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[311]:


g_count = player['Gender'].value_counts()

g_percent = g_count/len(player) * 100
g_percent = g_percent.round(2)

genderdem_df=pd.DataFrame({"Gender Count": g_count, 
                   "Gender Percentage": g_percent})
genderdem_df.head()


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[403]:


gen_pur_count = df.groupby(["Gender"]).count()["Price"]

gen_avg_pur = df.groupby(["Gender"]).mean()["Price"]
gen_avg_pur = gen_avg_pur.map('${:,.2f}'.format)

gen_pur_total_person = df.groupby(["Gender"]).sum()["Price"]
gen_pur_total_person = gen_pur_total_person.map('${:,.2f}'.format)

gen_avg_per_person = player.groupby(["Gender"]).mean()["Price"]
gen_avg_per_person = gen_avg_per_person.map('${:,.2f}'.format)

gen_purchasing_df = pd.DataFrame({
    "purchase count": gen_pur_count,
    "avg. purchase price": gen_avg_pur,
    "total purchase value": gen_pur_total_person,
    "avg. total purchase per person": gen_avg_per_person
})

gen_purchasing_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[404]:


#Creating seperate bins to hold the information before performing calculations 
#and creating a dataframe to hold the information

age_bins = [0,9,14,19,24,29,34,39,150]
bin_labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
player['age_range'] = pd.cut(player['Age'], age_bins, labels = bin_labels, include_lowest = True)

gen_age_count = player['age_range'].value_counts()

gen_age_percent = age_count/len(player)
gen_age_percent = gen_age_percent.map('{:.2%}'.format)

gen_age_df=pd.DataFrame({
    "count per age range": gen_age_count, 
    "percentage of players": gen_age_percent
})

gen_age_df.sort_index(0)


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[382]:


df['age_range'] = pd.cut(df['Age'], age_bins, labels = bin_labels, include_lowest = True)

age_pur_count = df.groupby(['age_range']).count()['Price']

age_pur_avg = df.groupby(['age_range']).mean()['Price']
age_pur_avg = age_pur_avg.map('${:,.2f}'.format)

age_pur_avg2 = player.groupby(['age_range']).mean()['Price']
age_pur_avg2 = age_pur_avg2.map('${:,.2f}'.format)

age_pur_tot = df.groupby(['age_range']).sum()['Price']
age_pur_tot = age_pur_tot.map('${:,.2f}'.format)


age_sum_df = pd.DataFrame({
    
    "Purchase Count": age_pur_count,
    "Avg Purchase": age_pur_avg,
    "Total Purchase Value": age_pur_tot,
    "Avg Purchase per Person": age_pur_avg2
})

age_sum_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[402]:


#Same methods utilised as above but including a sorting function at the end 


top_spend_count = df.groupby(['SN']).count()['Price']

top_spend_avg = df.groupby(['SN']).mean()['Price']
top_spend_avf = top_spend_avg.map('${:,.2f}'.format)

top_spend_tot = df.groupby(['SN']).sum()['Price']
top_spend_tot = top_spend_tot.map('${:,.2f}'.format)


top_spend_df = pd.DataFrame({
    
    "Purchase Count": top_spend_count,
    "Avg Purchase": top_spend_avg,
    "Total Purchase Value": top_spend_tot
})

top_spend_df = top_spend_df.sort_values('Purchase Count', ascending = False)

top_spend_df.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[495]:


pop_pur_count = df.groupby(['Item ID','Item Name']).count()['Purchase ID']

pop_price = df.groupby(['Item ID','Item Name']).mean()['Price']
pop_price = pop_price.round(2)

pop_total_value = df.groupby(['Item ID','Item Name']).sum()['Price']
#pop_total_value = pop_total_value.map('${:,.2f}'.format)

popular_df = pd.DataFrame({
    "Purchase Count" : pop_pur_count,
    "Item Price" : pop_price, 
    "Total Purchase Value" : pop_total_value
})

popular_df2 = popular_df.sort_values('Total Purchase Value', ascending = False)

popular_df2.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[500]:



pop2 = popular_df.sort_values('Total Purchase Value', ascending = False)
pop2['Total Purchase Value'] = pop2['Total Purchase Value'].map('${:,.2f}'.format)
pop2['Item Price'] = pop2['Item Price'].map('${:,.2f}'.format)
pop2.head()


# In[ ]:




