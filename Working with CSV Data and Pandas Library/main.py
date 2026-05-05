import csv
import pandas

# # File way to do:
# # with open("weather_data.csv") as csv_file:
# #     weather_data = csv_file.readlines()
# #     print(weather_data)
#
# #  CSV way to do:
# with open("weather_data.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     temperatures = []
#     for row in csv_reader:
#
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# # # print(data.head())#It's a dataframe
# # # print(data["temp"])#It's a series
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# # Get data in columns
# print(data["temp"])#Treat like a list
# print(data.temp)#Treat like an object
#
# # Get a row
# print(data[data.day == "Monday"])
# # Returning the day row with the highest temp
# print(data[data.temp == data["temp"].max()]) # or even: print(data[data.temp == data.temp.max()])
#
#
# # Converting temperature:
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/8 +32
# print(monday_temp_f)


# Creating a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("data_dict.csv")