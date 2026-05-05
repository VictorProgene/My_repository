import pandas

data = pandas.read_csv("Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray, black, cinnamon)

data_dict = {
    "Primary fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon],
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")
