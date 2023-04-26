from matplotlib import pyplot as plt

w=[56,45,48,52,50]
h=[177,164,172,164,168]

marks={'Tamil':92,'English':89,'Maths':86,'Science':84,'Social':89}

s=list(marks.keys())
m=list(marks.values())

plt.subplot(1,2,1)
plt.plot(w,h,color='green',ms=10 ,marker='o',mfc='red',ls=':' ,label='x-axis=weight''\n''y-axis=height')
plt.title('Human weight and height',font='cambria',size=15,color='blue')
plt.xlabel("Weight",font='cambria',size=15,c='blue')
plt.ylabel("Height",font='cambria',size=15,c='blue')

plt.legend()

plt.subplot(1,2,2)
plt.bar(s,m,color='darkblue',width=0.5 ,label='x-axis=subjects''\n''y-axis=Average')
plt.title('Marks and Subject',font='cambria',size=15,color='blue')
plt.xlabel("Subjects",font='cambria',size=15,c='blue')
plt.ylabel("Marks",font='cambria',size=15,c='blue')

plt.legend()

plt.show()
