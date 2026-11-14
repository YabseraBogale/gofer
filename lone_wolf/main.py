import pandas as pd

df = pd.read_csv("data.csv")

print("Number of female",len(df[df["Gender"]=="F"]))

print("Number of male",len(df[df["Gender"]=="M"]))


print("Number of female names with father names",len(df[df["Gender"]=="M"])*len(df[df["Gender"]=="F"]))
