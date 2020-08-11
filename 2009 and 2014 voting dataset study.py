import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections

#================Merging two excel files============

df=pd.DataFrame()

for f in ["C:\\Users\\pints\\Desktop\\python pro\\DATASET\\2009maharashtraresults.xlsx","C:\\Users\\pints\\Desktop\\python pro\\DATASET\\2014maharashtraresults.xlsx"]:
    data=pd.read_excel(f,'Sheet1')#this loop merges the two excel sheets into one
    df=df.append(data)
 
df.to_excel("C:\\Users\\pints\\Desktop\\python pro\\DATASET\\combineddata.xlsx")
data=pd.read_excel("C:\\Users\\pints\\Desktop\\python pro\\DATASET\\combineddata.xlsx")
print(data)  
    
#==============================Matplotlib===================

plt.figure(figsize=(8,4))
plt.scatter(data['PARTYNAME'],data['SEATS'],c='red')
plt.xlabel("party")
plt.ylabel("Seats Won")
plt.xticks(rotation=90)# to print party name vertically
plt.show()

#=======================Selecting=============

final_Data={}
for i in data['PARTYNAME']:
    x=i
    t1=(data[(data.PARTYNAME==x) & (data.YEAR==2009)].SEATS).tolist()
    t2=(data[(data.PARTYNAME==x) & (data.YEAR==2014)].SEATS).tolist()
    t3=t1+t2
    print("------------")
    print("Name of Party=",i)
    print("NUMBER OF SEATS=",int(sum(t3)))
    final_Data.update({i:int(sum(t3))})
 
    
plt.bar(final_Data.keys(),final_Data.values(),color="green")
plt.xlabel("Party")
plt.ylabel("Seats Won")
plt.xticks(rotation=270)    



print("The Change is performance is as Follows")

for i in data['PARTYNAME']:
    x=i
    t1=(data[(data.PARTYNAME==x) & (data.YEAR==2009)].SEATS).tolist()
    t2=(data[(data.PARTYNAME==x) & (data.YEAR==2014)].SEATS).tolist()
    diff=sum(t1[0:])-sum(t2[0:])
    if(diff>0):
        print("Party Name :",x)
        print("loss from 2009 to 2014=",int(diff))
    else:
        if diff<0:
            print("Party Name:",x)
            print("gain from 2009 tp 2014=",abs(int(diff)))
        else:
            print("Party Name:",x)
            print("No change from 2009 to 2014=",int(diff))
















