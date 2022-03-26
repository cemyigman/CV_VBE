import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# %%
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# %% One plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')
plt.show()

# %% Vertical Stacking
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)
plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y)
plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y)
plt.show()

# %%
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y, 'o')
axs[0, 0].set_title('Axis [0,0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0,1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1,0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1,1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()

# %%
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.ylabel('Kilo')
plt.xlabel('Boy', fontsize=12)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar().set_label('Renk')
plt.show()

#%%
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='Blues')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);
plt.show()
# cmap
# viridis
# plasma
# inferno
# magma
# cividis




