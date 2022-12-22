import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

### Getting the data and format
# implement standard error?

df = pd.read_csv("./wdbc.csv")

y = df["B/M"]  # M or B
not_data = ["ID", "B/M"]
x = df.drop(not_data, axis=1)

data = pd.concat([y, x], axis=1)  # basically just re-join to have a working full dataset


def graph_violin_plot():
    temp_y, temp_x = y, x  # so we dont alter original df
    normal_data = (temp_x - temp_x.mean()) / (temp_x.std())  # must be stnadardized for this type of plot
    data = pd.concat([y, normal_data.iloc[::, 20:]], axis=1)  # index 0:10, 10:20, 20: # for usual, se, worst
    data = pd.melt(data, id_vars="B/M", var_name="features", value_name='value')
    sns.violinplot(x="features", y="value", hue="B/M", data=data, split=True, inner="quart")
    plt.xticks(rotation=90)  # roate labels on variables
    plt.show()

def graph_pairplot():
    # all individual variables seem to be approximately normally distributed (leading diag)
    # removing B/M from data, i dont know how to get the hue for diag again.
    sns.pairplot(data=data.iloc[::, :10])
    plt.show()
    plt.close()

def graph_heatmap_corr():  # why is it rectangular?????
    f, ax = plt.subplots(figsize=(18, 18))
    sns.heatmap(x.corr(), annot=True, fmt=".1f", ax=ax)  # only 1 dp as easier to read but obv lose info
    plt.title("Feature Correlation")
    plt.show()

def graph_diag():
    sns.countplot(data=x, x=y)
    plt.title("Diagnosis")
    plt.show()

def calc_describe():
    B, M = y.value_counts()  # 0 or False is for having cancer
    print("Benign:", B)
    print("Malignant:", M)
    print(x.describe())

def graph_deep_corr():  # not too sure how to read this apart from regression line
    sns.jointplot(x=x.loc[:, 'Area'], y=x.loc[:, 'Radius'], kind="reg")
    plt.show()

graph_violin_plot()
