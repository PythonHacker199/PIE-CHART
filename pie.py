# pip install matplotlib

import matplotlib.pyplot as plt 

labels='Python','C++','Ruby','Java','C#'
sizes=[259,100,101,140,99]
colors=['green','blue','yellow','orange','red']
explode=[0.1,0,0,0,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,shadow=True,autopct='%1.1f%%',startangle=140)
 plt.axis('equal')
 plt.show()