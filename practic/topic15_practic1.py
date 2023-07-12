import matplotlib.pyplot as plt

#1

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)

ax.set_title("Qube of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Qube of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 5100, 0, 5100000])

plt.show()

#2

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,  c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Qube of Value", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Qube of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 5100, 0, 5100000])

plt.show()