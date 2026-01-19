import matplotlib
import matplotlib.pyplot as plt
import numpy as np

categories=["Butter naan","Pani Puri","Biryani","Manchuriyan","Momos","Waffles"]
values=np.array([8.2,9.5,10,9,8.5,7])

colors=["#fcad03","#cafc03","#fc6f03","#fc2003","ivory","chocolate"]

plt.pie(values,labels=categories,
        colors=colors,
        explode=[0,0,0.2,0,0.1,0],
        shadow=True)

plt.title("CURRENT CRAVINGSSSS")
plt.tight_layout()
plt.show()