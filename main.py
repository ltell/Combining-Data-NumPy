import csv
import numpy as np

# ADD CODE: Convert titanic1.csv
with open("titanic1.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  # Assign the CSV data to a variable named data and convert the data to a reader object by writing:
  headers = next(data)
  # And, to retrieve all the rows of the reader object as a list:
  data_list = list(data)
  titanic_data1 = np.array(data_list)
# ADD CODE: Convert titanic2.csv 
with open("titanic2.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  second_data = list(data)
  titanic_data2 = np.array(second_data)

# ADD CODE: Merge two datasets
# axis =0 specifies that you want to concatenate the first list in each array
combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

# ADD CODE: Print out shape and number of dimensions of merged dataset
print(combined_data.shape)
print(combined_data.ndim)

# Transform the combined_data NumPy array back into a regular list
listify = combined_data.tolist()
# store the Titatic data here once I convert them into a string.
titanic_lists_to_string = []
for titanic_lists in listify:
  # turn each Titanic list into a string :
  titanic_string = (",").join(titanic_lists)
  titanic_lists_to_string.append(titanic_string)
# transform the NumPy array into a string
complete_titanic = ("\n").join(titanic_lists_to_string)
# This time instead of using a comma delimiter, you'll use a new line as a delimiter-("\n")-so each row of data is on one line

# Write your fresh string to a new .csv file
with open("titanic.csv", "w") as file:
  # select the headers and data columns you like to add to the CSV file
  file.write('Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n')
  #Writing \n at the end of the headers indicates to Python that the rest of the Titanic data should start on the next row.
  # This code will add the string with all of your Titanic data to your new CSV.
  file.write(complete_titanic)