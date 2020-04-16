import pandas as pd
import matplotlib.pyplot as plt


#1.Done

#2. I believe The World Health Organization is a credible source because it is a
#3 UN health agency. When it comes to country organizations
# I'm not sure if the China CDC is intirely credible because
# I have read they are not measuring all cases and are only counting hospitalized cases and not counting
# all deaths. As far as news channels worldometer is one the data set is using.
# I don't think they are as accurate because they might not get as much funding or
#they are receiving data slower than international and government organizations.

 #4.


def correctDateFormat(df):
df = df.melt(id_vars=df.columns[0:4], var_name="Date", value_name="Confirmed")
df["Date"]=pd.to_datetime(df["Date"])
return df

def aggregateCountry(df, country):
    data = df.loc[df["Country/Region"] == country]
    return data.groupby("Date", as_index=False).sum()
