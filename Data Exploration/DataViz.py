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

# extracted the variables that are important for data visualization
cdf = df[["B/M", "Radius", "Texture", "Perimeter", "Area", "Smoothness", "Compactness", "Concavity", "ConcavePoints",
          "Symmetry", "FractalDimension"]]


# B\M dtype is object, which cannot be used for hue
def convert(letter):
    if letter == 'B':
        return False
    else:
        return True


cdf["B/M"] = cdf["B/M"].apply(convert)

sns.pairplot(data=cdf, hue="B/M")
plt.show()

sns.heatmap(cdf.corr(), cmap="flare")
plt.show()
