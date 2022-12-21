import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("./wdbc.csv", header=None)

colHead = ["ID", "B/M", "Radius", "Texture",
           "Perimeter", "Area", "Smoothness", "Compactness", "Concavity", "ConcavePoints", "Symmetry",
           "FractalDimension",
           "RadiusSE", "TextureSE", "PerimeterSE", "AreaSE", "SmoothnessSE", "CompactnessSE", "ConcavitySE",
           "ConcavePointsSE", "SymmetrySE", "FractalDimensionSE", "RadiusWorst", "TextureWorst",
           "PerimeterWorst", "AreaWorst", "SmoothnessWorst", "CompactnessWorst", "ConcavityWorst",
           "ConcavePointsWorst", "SymmetryWorst", "FractalDimensionWorst"]

# assign column names as .data file doesn't work on MacOS correctly
df.columns = colHead

# extracted the input variables
xs = df[["Radius", "Texture", "Perimeter", "Area", "Smoothness", "Compactness", "Concavity", "ConcavePoints",
          "Symmetry", "FractalDimension"]]
# output label, our diagnosis
diag = df["B/M"]

def convert(letter):
    if letter == 'B':
        return False
    else:
        return True



def pairplot_all():
    # all individual variables seem to be approximately normally distributed (leading diag)
    # removing B/M from data, i dont know how to get the hue for diag again.
    sns.pairplot(data=xs)
    plt.show()
    plt.close()

def headmap_corr_all():
    sns.heatmap(xs.corr(), cmap="flare")
    plt.show()
    plt.close()

def simple_diagnosis():
    sns.countplot(data=xs, x = diag)
    plt.show()

def statistics():
    B, M = diag.value_counts()  # 0 or False is for having cancer
    print("Benign:", B)
    print("Malignant:", M)
    print(xs.describe())

sns.violinplot(data=xs, split=True, inner="quart")
plt.show()