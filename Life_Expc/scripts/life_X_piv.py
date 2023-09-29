import pandas as pd
import numpy as np

# Read the initial 
csv = r'C:\Users\USER\Desktop\Life_Project\Life_Expc\data\llife.csv'
df = pd.read_csv(csv)
df.columns = df.columns.astype(str)
pd.set_option('display.max_columns', None)

# Unpivot the Excel data for CSV export
df_unpivot = pd.melt(df, id_vars='Unnamed: 0', value_vars=[ '1999','2000','2001','2002','2003','2004','2005', '2006',
                                                           '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                                                           '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                                                           '2021', '2022'])
df_unpivot.rename(columns={"Unnamed: 0": "Регион", "variable": "Год", "value": "Ожидаемый возраст населения при рождении"}, inplace=True)
df_unpivot.replace("-", np.nan, inplace=True)
df_unpivot.dropna(axis=0, inplace=True)
df_unpivot = df_unpivot.applymap(lambda x: int(x) if isinstance(x, str) and x.isdigit() else x)


print(df_unpivot)

data_types = df_unpivot.dtypes
print(data_types)


df_unpivot.to_csv(r'C:\Users\USER\Desktop\Life_Project\Life_Expc\data\life_X_piv.csv', index=False)