
import matplotlib.pyplot as plt

size = [35, 39, 40, 41, 47, 50, 53]
time = [0.000025, 2.891704, 0.174795, 0.183957, 0.000057, 0.000284, 0.000015]
throughput = [4280000, 40.80638958897591, 652.192568, 608.837934, 1986842.10, 451584.507042, 7666666.6666]

plt.plot(size, time, color='red', marker='o')
plt.title('RTT ', fontsize=14)
plt.xlabel('Size', fontsize=14)
plt.ylabel(' time ', fontsize=14)
plt.grid(True)
plt.show()

plt.plot(size, throughput, color='red', marker='o')
plt.title('throughput ', fontsize=14)
plt.xlabel('Size', fontsize=14)
plt.ylabel(' throughput ', fontsize=14)
plt.grid(True)
plt.show()