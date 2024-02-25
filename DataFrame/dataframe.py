import pandas as pd


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df  = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print (df)

df(loc[0]) --> Prints 0 th index elements.
df(loc[0, 1]) --> Prints 0 to 1 index elements
