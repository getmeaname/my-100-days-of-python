 with open("weather_data.csv") as data:
     list_data = data.readlines()
     print(list_data)

 import csv

 with open("weather_data.csv") as data:
     data_file = csv.reader(data)
     temperature = []
     for row in data_file:
         if row[1] != "temp":
             temperature.append(int(row[1]))
     print(temperature)


 data = pandas.read_csv("weather_data.csv")
 print(data["temp"])
 data_dict = data.to_dict()
 print(data_dict)

 temp_list = data["temp"].to_list()
 avg = sum(temp_list)/(len(temp_list))
 print(avg)

 # getting average
 avg = data["temp"].mean()
 print(avg)

 # getting a column
 print(data.condition)

 # getting a row
 print(data[data.day == "Monday"])

 # Finding maximum
 maxi = data["temp"].max()
 print(maxi)
 print(data[data["temp"] == maxi])

 # Celsius to Fahrenheit conversion
 monday = data[data.day == 'Monday']
 celsius = monday.temp[0]
 print(celsius)
 fahrenheit = (celsius * 9/5) + 32
 print(fahrenheit)

 # Create a DataFrame
 data_dict = {
     "Students": ["Arun", "Pakoda", "Bonda", "Mamu"],
     "scores": [76, 56, 65, 78]
 }
 data = pandas.DataFrame(data_dict)
 data.to_csv("new_data.csv")

 # Squirrels count Exercise
 data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231029.csv")

 gray_squirrels_count = len(data[data.Primary_Fur_Color == "Gray"])
 cinnamon_squirrels_count = len(data[data.Primary_Fur_Color == "Cinnamon"])
 black_squirrels_count = len(data[data.Primary_Fur_Color == "Black"])

 data_dictionary = {
     "Fur Color": ["Gray", "Cinnamon", "Black"],
     "Squirrel Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
 }

 df = pandas.DataFrame(data_dictionary)
 df.to_csv("Squirrel_Count.csv")
