import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r'C:\Users\91823\Desktop\code\python\PIET INTERNSHIP\internship-projects\treadmil-users.csv')
features=df.iloc[:,2:]
labels=df['Product']
plt.xlabel('product')
plt.ylabel('miles')
plt.title('treadmil_users')
plt.scatter(features,labels,color='green')
plt.grid()
plt.show()