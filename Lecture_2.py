import  pandas as pd
import matplotlib.pyplot as plt

#auto = pd.read_csv("Automobile_data.csv")
accidents = pd.read_csv("US_Accidents_Dec21_updated.csv")

print(accidents.columns)
#
# print((accidents['Wind_Speed(mph)'].head()))