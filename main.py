# Convert Epoch to Datetime in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bobby', 'Carl'],
    'Date': ['1688025596', '1687013326', '1689071143']
})

df['Date'] = pd.to_datetime(df['Date'], unit='s')

#     Name                Date
# 0  Alice 2023-06-29 08:00:00
# 1  Bobby 2023-06-17 14:49:36
# 2   Carl 2023-07-11 10:25:04
print(df)