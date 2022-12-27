import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./wdbc.csv")

y = df["B/M"]  # M or B
not_data = ["ID", "B/M"]
x = df.drop(not_data, axis=1)

data = pd.concat([y, x], axis=1)

x, x_test, y, y_test = train_test_split(x, y, test_size=0.25, stratify=y)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, stratify=y)
