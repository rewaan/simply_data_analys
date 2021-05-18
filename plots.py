import pandas as pd
import matplotlib.pyplot as plt

df_work = pd.read_csv('27_work.csv', sep=',', header=None)
df_work = df_work.drop(0)
df_work.columns = ['a', 'x', 'y', 'z']
df_work.drop(['a', 'x'], axis=1, inplace=True)
df_work['y'] = df_work['y'].astype(float)
df_work['z'] = df_work['z'].astype(float)
print(df_work)

f_plot = plt.plot(df_work['z'], label='f(x)')
plt.xticks(df_work['y'])
plt.scatter(df_work['y'], df_work['z'])

df_inter = pd.read_csv('interpolation_data.txt', sep='\t', header=None)
df_inter.columns = ['Values']
print(df_inter)
iter = [(i+10)/10 for i in range(0, 241)]
df_inter['x'] = iter
print(df_inter)

df_inter.index = df_inter['x']
df_inter = df_inter.drop('x', 1)
df_inter = df_inter.iloc[25:215]
print(df_inter)

df_apro = pd.read_csv('approximation_data.txt', sep='\t', header=None)
print(df_apro)

apr_plot = plt.plot(df_apro, color='green', label='Approximation')

inter_plot = plt.plot(df_inter, label='Interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
