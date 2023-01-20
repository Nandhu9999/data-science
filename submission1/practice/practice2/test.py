import pandas as pd
import numpy as np
df = pd.read_csv(".\\data science\\practice\\test1.csv")
# print(df)

# print(df.describe())

# print(df.head(3))
# print(df.tail(5))
# print(df.info())
print(df.shape)
# print(df.iloc[242])
print(df.columns)
df.columns = ['Srl No', 'age', 'type_employer', 'fnlwgt','education', 'education_num', 'marital','occupation','relationship', 'race','sex', 'capital_gain', 'capital_loss','hr_per_week', 'country', 'income']
print(df.columns)

# print(df.iloc[0, :5])

df2 = df.groupby("country").count()
print(df2.iloc[:,1])

# df.replace("<=50K","Income", inplace=True)
# df2 = df.replace({"<=50K":"Income"})
# print(df)

# df.where[df["income"] == "<=50K", "income"] = "Income"
# df["income"] = np.where([df["income"] == "<=50K"], "Income", 0)
# df['<=50K'] = df['<=50K'].astype('str') 
# df.replace(to_replace=["<=50K"], value="INCOME", inplace=True)
# print(df)

df3 = df.groupby("education")
print(df3.iloc[5,:])