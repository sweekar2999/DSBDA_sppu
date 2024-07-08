import pandas as pd

dataset = pd.read_csv("covid_vaccine_statewise.csv")
print(dataset.info())
print(dataset.groupby("State")[["First Dose Administered"]].sum())
print(dataset.groupby("State")[["Second Dose Administered"]].sum())
print(dataset["Male(Individuals Vaccinated)"].sum())
print(dataset["Female(Individuals Vaccinated)"].sum())