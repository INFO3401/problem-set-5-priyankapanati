from utils import *
from covid import *

df = loadAndCleanData("time_series_covid19_confirmed_global.csv")
df = correctDateFormat(df)
print(df)
x = "Date"
y = "Confirmed"
df1 = loadAndCleanData("time_series_covid19_deaths_global.csv")
df2 = loadAndCleanData("time_series_covid19_recovered_global.csv")
