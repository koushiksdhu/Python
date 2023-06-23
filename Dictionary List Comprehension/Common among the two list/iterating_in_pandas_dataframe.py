student_dict = {
    "Student" : ["Koushik Sadhu", "Shuvam Kumar Choudhury", 'Anmol Kumar Gupta', 'Pranay Gupta'],
    "Score" : [100, 58, 95, 86]
}
print(student_dict)

import pandas
data = pandas.DataFrame(student_dict)
data.to_csv("Dictionary List Comprehension\Common among the two list\student_dict_dataframe.csv")

# Pandas is having an inbuilt loop. The normal loop does not able to arrange properly the rows and columns of the DataFrame:
# The Normal loop iterate over the columns of the DataFrame whereas the pandas inbuilt loop iterate over the rows of the DataFrame.
# Pandas inbuilt loop: for(index, row) in DataFrame_name.iterrows():
for (index, row) in data.iterrows():
    print(index)
    print(row)
    print(row.Student)
    print(row.Score)