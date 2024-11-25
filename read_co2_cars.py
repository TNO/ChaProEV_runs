import pandas as pd

co2_cars: pd.DataFrame = pd.read_csv('input/Mopo/co2_cars_2020.csv')
co2_cars_petrol_diesel: pd.DataFrame = co2_cars.loc[
    co2_cars['Ft'].isin(['PETROL', 'DIESEL'])
]
# cars_electricity: pd.DataFrame = co2_cars.loc[co2_cars['Ft'] == 'ELECTRIC']
# cars_petrol: pd.DataFrame = co2_cars.loc[co2_cars['Ft'] == 'PETROL']
# print(cars_petrol.iloc[6])
# exit()

country_emissions_data: pd.DataFrame = co2_cars_petrol_diesel[
    ['Country', 'Ewltp (g/km)', 'Enedc (g/km)']
]
grouped_data: pd.DataFrame = country_emissions_data.groupby(
    by='Country'
).mean()
grouped_data.to_csv('country_emissions.csv')
# print(cars_electricity)
