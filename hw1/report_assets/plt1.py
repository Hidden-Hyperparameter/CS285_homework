import matplotlib.pyplot as plt
"""
| 1000 | $4534\pm 97$ |
| 800 | $4250\pm 109$ |
| 600 | $4280\pm 67$ | 
| 400 | $2109\pm 990$ |
| 200 | $111\pm 191$ |
"""
# Sample data
x = [1000,800,600,400,200]
y = [4534,4250,4280,2109,111]
error = [98,109,67,990,191]

# Plot the line
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add error bars
plt.errorbar(x, y, yerr=error, fmt='o', color='black')

# Customize the plot
plt.xlabel('train steps per iter')
plt.ylabel('rewards')
# plt.title('Line Plot with Error Bars')

# Show the plot
# plt.show()
plt.savefig('./3-2.png')