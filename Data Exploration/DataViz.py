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

df.columns = colHead

df.drop('ID', inplace=True, axis=1)


def convert(letter):
    if letter == 'B':
        return False
    else:
        return True


df["B/M"] = df["B/M"].apply(convert)
print(df["B/M"].dtype)

sns.pairplot(data=df[["Radius", "Texture",
                      "Perimeter", "Area", "Smoothness", "Compactness", "Concavity", "ConcavePoints", "Symmetry",
                      "FractalDimension",
                      "RadiusSE", "TextureSE", "PerimeterSE", "AreaSE", "SmoothnessSE", "CompactnessSE", "ConcavitySE",
                      "ConcavePointsSE", "SymmetrySE", "FractalDimensionSE"]], kind='reg', hue="B/M")

plt.show()

print('e')
