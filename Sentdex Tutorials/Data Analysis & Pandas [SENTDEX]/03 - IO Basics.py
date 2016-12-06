import pandas as pd

df = pd.read_csv('Zillow Median Sale Price - 10803.csv')
print(df.head())

df.set_index('Date', inplace=True)

#creating a new csv file from the dataframe which is now indexed to date
df.to_csv('Zillow_Mean_Sale_Price_10803_v2.csv')

df = pd.read_csv('Zillow_Mean_Sale_Price_10803_v2.csv')
print(df.head())

df = pd.read_csv('Zillow_Mean_Sale_Price_10803_v2.csv', index_col=0)
print(df.head())

df.columns = ['Pelham_3BR_HVI']
print(df.head())

df.to_csv('Pelham_3BR_HVI.csv')
df.to_csv('Pelham_3BR_HVI_data.csv', header=False)

df = pd.read_csv('Pelham_3BR_HVI_data.csv', names=['Data', 'Pelham_3BR_HVI'], index_col=0)
print(df.head())

df.rename(columns={'Pelham_3BR_HVI' : '10803 3BR HVI'}, inplace=True)
print(df.head())
