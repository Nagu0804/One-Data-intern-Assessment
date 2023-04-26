import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,10,2)

# Calculate the area and perimeter for the square and circle
sq_area=(x*x)
sq_peri=x*4

cr_area=3.14*x*x
cr_peri=2*3.14*x

plt.subplot(2,1,1)

# Plot the area for the square and circle
plt.plot(x,sq_area,color='green' ,ms=5,marker='o',mfc='Skyblue',ls='--',label='Area of square')
plt.plot(x,cr_area,color='green' ,ms=5,marker='o',mfc='blue',ls='--',label='Area of Circle')
#plt.xlabel("Side",font='cambria',size=15,c='red')
plt.ylabel("Area",font='cambria',size=15,c='red')
plt.legend()

# Plot the perimeter for the square and circle
plt.subplot(2,1,2)
plt.plot(x,sq_peri,color='green' ,ms=5,marker='o',mfc='Skyblue',ls='--',label='Perimeter of Square')
plt.plot(x,cr_peri,color='green',ms=5 ,marker='o',mfc='blue',ls='--',label='Preimeter of Circle')
plt.xlabel("Side",font='cambria',size=15,c='red')
plt.ylabel("Perimeter",font='cambria',size=15,c='red')
plt.legend()

plt.suptitle('Area and Perimeter of Square and Circle',font='cambria',size=15,c='red')
plt.show()

