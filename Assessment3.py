from matplotlib import pyplot as plt

products=['coke','pepsi','maazaa' ,'sprite','limca','bovonto']

coim=[3234,3452,3354,4313,1648,5485]
selam=[2485,2132,5462,6541,5211,4525]

plt.title('Products sales in different Districts',font='cambria',size=20,color='red')

plt.scatter(products,coim,marker='d',c='red',s=100,label='sale in coimbatore')
plt.scatter(products,selam,marker='p',c='g',s=100,label='sale in selam')

plt.xlabel('Products',color='blue',font='cambria',size=15)
plt.ylabel('Sales',color='blue',font='cambria',size=15)

plt.legend()
plt.show()

 
