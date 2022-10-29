import matplotlib.pyplot as plt 

x =[2,4,6,8,10]
y = [6,7,8,2,4]


x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]


# plt.bar(x, y, label="Bars 1", color='red')
# plt.bar(x2,y2, label="Bars 2", color='c')

# plt.xlabel('x')
# plt.ylabel('y')

# plt.title('Bar Graph\nby AJ Malicsi')

# plt.legend()

# plt.show()


population_ages = [22,55,62,45,21,22,34,42,56,4,99,102,35,23,60,13,20,31,44,53,54,52,12,23,34,32,35,26,28,23]

ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,120]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Histogram\nby AJ Malicsi')

plt.legend()

plt.show()






