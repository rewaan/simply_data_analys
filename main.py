import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

i = 1
max_std = 0
line = 1
df = pd.read_csv('27.txt', sep='\t', header=None)
df.columns = ['x', 'y', 'z']
print(df)
for frame in np.array_split(df, 25):
    frame_std = frame['z'].std()
    min_value = frame['z'].min()
    max_value = frame['z'].max()
    median = np.median(frame['z'])
    print('Line {}, standard deviation = {:.5f}, min value = {:.5f}, max value = {:.5f}, median = {:.5f}'.format(i, frame_std,
                                                                                                min_value, max_value, median))
    i += 1
    if frame_std > max_std:
        max_std = frame_std
        line = i - 1
        df_work = frame
print("Highest standard deviation was found in {}rd frame and it's value is {:.5f}".format(line, max_std))
print(df_work)
heatmap1_data = pd.pivot_table(df, values='z',
                     index='y',
                     columns='x')
sns.heatmap(heatmap1_data, cmap="GnBu").set(title='2D Heatmap')
Y = range(df.shape[0])
X = range(df.shape[1])
X, Y = np.meshgrid(X, Y)

plot_3d = plt.figure().gca(projection='3d', title='3D visualization')
plot_3d.plot_surface(Y, X, df, cmap='GnBu')
plot_3d.set_xlabel('x')
plot_3d.set_ylabel('y')
plot_3d.set_zlabel('z')
plt.show()

df_work['z'].to_csv('27_work.txt', header=None, index=None, sep=' ')






