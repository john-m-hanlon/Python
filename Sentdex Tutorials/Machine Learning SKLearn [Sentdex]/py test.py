import pandas as pd
a = ['a', 'b', 'c', 'd']
b = ['b', 'e', 'd']
c = []
for i in a:
    if i in b:
        c.append(i)

print(c)

df = pd.read_csv('/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/Machine Learning SKLearn [Sentdex]/2013_sp500_list.csv')
print(df)

op = []

for i in df['2013_sp500_list']:
	op.append(str(i))

print(op)

