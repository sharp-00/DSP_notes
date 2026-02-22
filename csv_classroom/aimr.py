import numpy as np

n = np.loadtxt('aimr.csv', skiprows=1, delimiter=',')

i =0
mean_all = []
for i in range(124):
    mean = np.mean()
    mean_all += [mean]
    i += 1

print(mean_all)
