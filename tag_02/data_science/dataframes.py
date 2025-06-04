import pandas as pd
import os

""" Funktionen """

if __name__ == "__main__":
    os.chdir("data")
    datasets_csv = os.listdir()

    if "oktoberfest.csv" in datasets_csv:
        filename = "oktoberfest.csv"
    else:
        print("File does not exist.")

    if not os.path.exists("oktoberfest.csv"):
        print("File does not exist.")
        exit(1)

    df = pd.read_csv(filename, index_col=None)
    print(df.head())
    print(df.columns)
    print(df.info())

    df = df[["year", "beer_price"]]
    print(df.head())
    print(df.info())
    max_price = df["beer_price"].max()
    mean_price = df["beer_price"].mean()
    std_dev = df["beer_price"].std()

    print(mean_price)
    print(std_dev)

    print("Max Price: ", max_price)
    print("Year with max price:")

    print(df["year"])

    result_df = df[-10:]
    print(result_df)
    result_df.to_csv("year_beer.csv")
    df = df.loc[df["beer_price"] == max_price]
    df.reset_index(drop=True, inplace=True)
    print(df["year"].iloc[0])