import pandas as pd

df = pd.read_csv("/home/amorntep/hotel-booking-cancellation-analysis/data/hotels.csv")
df.info()
pd.set_option("display.max_columns", None)
df.sample(20)
df.describe()
