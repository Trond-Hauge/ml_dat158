import pickle
import pandas as pd

#from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report

from sklearn.linear_model import LinearRegression
#from sklearn import metrics

#from collections import defaultdict

with open("LR_Model", "rb") as file:
    model = pickle.load(file)

#def add_calendar(data = None):
#  data["release_date"] = pd.to_datetime(data["release_date"], infer_datetime_format=True)
#  data["release_day"] = data["release_date"].apply(lambda d: d.day)
#  data["release_weekday"] = data["release_date"].apply(lambda d: d.weekday())
#  data["release_month"] = data["release_date"].apply(lambda d: d.month)
#  data["release_year"] = data["release_date"].apply(lambda d: d.year if d.year < 2021 else d.year -100)
#  data.drop(["release_date"], axis = 1, inplace = True)
#
#def convert_dicts(data = None):
#  #Genres
#  genres = data.genres.str.get_dummies(sep = ',')
#  data = pd.concat([data, genres], axis = 1)
#  data.drop(["genres"], axis = 1, inplace = True)
#
#  #Original language
#  lang = pd.get_dummies(data["original_language"])
#  data.drop(["original_language"], axis = 1, inplace = True)
#
#  data = pd.concat([data, lang], axis = 1)
#  
#  return data

def predict(df):
    #add_calendar(df)

    # Disabled due to reasons explained in notebook conclusion. Team is overworked (work to cover absent coworkers due to sicknes) and ourselves being sick.
    #df = convert_dicts(df)

    #print(df.shape)
    #print(df.head)

    prediction = model.predict(df)

    return prediction

#def main():
#    print("Hello! I just arrived..")
#
#    df = pd.read_csv("example.csv", index_col=0)
#
#    p = predict(df)
#    print(p)
#
#if __name__ == "__main__":
#    main()