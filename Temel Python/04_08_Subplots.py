import matplotlib.pyplot as plt

plt.style.use('seaborn-white')
import numpy as np

# %%
# Second plot is located
# at [left, bottom, width, height]
# start from 65% from left and bottom
# size is 20% width and height
ax1 = plt.axes()  # standard axes
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])
plt.show()

# %%
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))
plt.show()

# %%
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')
plt.show()

# %%
# adjust is used to arrange the spacing between plots
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
            fontsize=18, ha='center')

# %%
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')

for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
                      fontsize=18, ha='center')
plt.show()

# %%
# Grid Space
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
ax1 = plt.subplot(grid[0, 0])
ax1.plot(x, y)
ax1.text(1, 2, 'dcc', fontsize=32, color='black')
ax2 = plt.subplot(grid[0, 1:])
ax3 = plt.subplot(grid[1, :2])
ax4 = plt.subplot(grid[1, 2]);
plt.show()

# %%
# Create some normally distributed data
# .T transpose
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6), facecolor='#0F4972')
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
main_ax.set_facecolor('#578BAF')
main_ax.tick_params(labelcolor='white')
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
y_hist.set_facecolor('#578BAF')
y_hist.tick_params(labelcolor='white')
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
x_hist.set_facecolor('#578BAF')
x_hist.tick_params(labelcolor='white')

# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=4, alpha=0.9, color='#E3A61B')

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical', color='#E3A61B', alpha=0.7)
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal', color='#E3A61B', alpha=0.7)
y_hist.invert_xaxis()
plt.show()

# %%
