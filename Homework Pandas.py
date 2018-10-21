
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np


# In[26]:


data_file = "purchase_data.csv"


# In[39]:


purchase_data = pd.read_csv(data_file)
purchase_data.head()


# In[34]:


total_players = len(purchase_data["SN"].value_counts())
pd.DataFrame([total_players], columns = ["Total Players"])


# In[35]:


unique_items = len(purchase_data["Item Name"].value_counts())
average_price = round(purchase_data["Price"].mean(),2)
number_purchases = (purchase_data["Price"].count())
total_revenue = round(purchase_data["Price"].sum(),2)
summary_of_purchases = []
summary_of_purchases.append(unique_items)
summary_of_purchases.append("$" + str(average_price))
summary_of_purchases.append(number_purchases)
summary_of_purchases.append("$" + str(total_revenue))
pd.DataFrame([summary_of_purchases], columns = ["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"])


# In[36]:


genders = purchase_data[["SN", "Gender"]]
genders = genders.drop_duplicates()
counts = genders["Gender"].value_counts()

total_counts = [counts[0],counts[1],counts[2]]
percents = [round((counts[0]/total_players)*100,2),round((counts[1]/total_players)*100,2),round((counts[2]/total_players)*100,2)]

different_genders = pd.DataFrame({"Total Count": total_counts, "Percentage of Players": percents})
different_genders.index = (["Male", "Female", "Other / Non-Disclosed"])
different_genders


# In[37]:


gender_purchase_total = purchase_data.groupby(["Gender"]).sum()["Price"].rename("Total Purchase Value")
gender_average = purchase_data.groupby(["Gender"]).mean()["Price"].rename("Average Purchase Value")
gender_counts = purchase_data.groupby(["Gender"]).count()["Price"].rename("Purchase Count")

normalized_total = gender_purchase_total / different_genders["Total Count"]

gender_data = pd.DataFrame({"Normalized Total": normalized_total, 
                            "Purchase Count": gender_counts, 
                            "Total Purchase Value": gender_purchase_total, 
                            "Average Purchase Value": gender_average})

gender_data


# In[46]:


age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)
age_demographics_totals = purchase_data["Age Ranges"].value_counts()
age_demographics_percents = age_demographics_totals / total_players * 100
age_demographics = pd.DataFrame({"Total Count": age_demographics_totals, "Percentage of Players": age_demographics_percents})
age_demographics = age_demographics.round(2)
age_demographics.sort_index()


# In[47]:


user_total = purchase_data.groupby(["SN"]).sum()["Price"].rename("Total Purchase Amount")
user_average = purchase_data.groupby(["SN"]).mean()["Price"].rename("Average Purchase Price")
user_count = purchase_data.groupby(["SN"]).count()["Price"].rename("Purchase Count")

user_data = pd.DataFrame({"Total Purchase Amount": user_total,
                          "Average Purchase Price": user_average,
                          "Purchase Count": user_count})
user_data.sort_values("Total Purchase Amount", ascending=False).head(5)


# In[48]:


user_total = purchase_data.groupby(["Item ID", "Item Name"]).sum()["Price"]
user_total.head()

