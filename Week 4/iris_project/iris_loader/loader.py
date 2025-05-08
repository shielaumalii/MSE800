import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_iris_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    df = pd.read_csv(url, header=None, names=columns)
    return df

def print_flower_names(df):
    print("Unique flower species in the dataset:")
    for name in df['species'].unique():
        print(f"- {name}")

def visualize_data(df):
    sns.pairplot(df, hue="species", height=2.5)
    plt.suptitle("Pairplot of Iris Dataset", y=1.02)
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x="petal_length",
        y="petal_width",
        hue="species",
        palette="deep"
    )
    plt.title("Petal Length vs Petal Width")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.grid(True)
    plt.show()
