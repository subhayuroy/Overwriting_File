#!/usr/bin/env python3

"""
The CSV module uses classes to read and write tabular data in CSV format. The CSV library allows us to both read from and write to CSV files.
Now, import the CSV module.
"""
import csv

"""
Define the function read_employees. This function takes file_location (path to employees.csv) as a parameter.
"""
def read_employees(csv_file_location):
 """
 Open the CSV file by calling open and then csv.DictReader.
 DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.
 We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.
 Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. We will now register a dialect empDialect.
 """
 csv.register_dialect('empDialect', skipinitialspace = True, strict = True)
 """
 The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
 """
 employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
 """
 You now need to iterate over the CSV file that you opened, i.e., employee_file. When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).
 Append the dictionaries to an empty initialised list employee_list as you iterate over the CSV file.
 """
 employee_list = []
 for data in employee_file:
  employee_list.append(data)
 #Now return this list.
 return employee_list
"""
To test the function, call the function and save it to a variable called employee_list. Pass the path to employees.csv as a parameter to the function. Print the variable employee_list to check whether it returns a list of dictionaries.
"""
employee_list = read_employees('/home/student-02-52d7a36a22e1/data/employees.csv')
print(employee_list)

#The second function process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount.
def process_data(employee_list):
 """
 This function needs to pass the employee_list, received from the previous section, as a parameter to the function.
 Now, initialize a new list called department_list, iterate over employee_list, and add only the departments into the department_list.
 """
 department_list = []
 for employee_data in employee_list:
  department_list.append(employee_data['Department'])
 #The department_list should now have a redundant list of all the department names. We now have to remove the redundancy and return a dictionary. We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.
 department_data = {}
 for department_name in set(department_list):
  department_data[department_name] = department_list.count(department_name)
 return department_data
"""
This uses the set() method, which converts iterable elements to distinct elements.
Now, call this function by passing the employee_list from the previous section. Then, save the output in a variable called dictionary. Print the variable dictionary.
"""
dictionary = process_data(employee_list)
print(dictionary)

"""
Next, we will write the function write_report. This function writes a dictionary of department: amount to a file.
The report should have the format:
<department1>: <amount1>
<department2>: <amount2>
"""
def write_report(dictionary, report_file):
 """
 This function requires a dictionary, from the previous section, and report_file, an output file to generate report, to both be passed as parameters.
 You will use the open() function to open a file and return a corresponding file object. This function requires file path and file mode to be passed as parameters. The file mode is 'r' (reading) by default, so you should now explicitly pass 'w+' mode (open for reading and writing, overwriting a file) as a parameter.
 Once you open the file for writing, iterate through the dictionary and use write() on the file to store the data.
 """
 with open(report_file, "w+") as f:
  for k in sorted(dictionary):
   f.write(str(k)+':'+str(dictionary[k])+'\n')
  f.close()

#Now call the function write_report() by passing a dictionary variable from the previous section and also passing a report_file. The report_file passed within this function should be similar to /home/<username>/data/report.txt. Replace <username> with the one mentioned in Connection Details Panel at left-hand side.
write_report(dictionary, '/home/student-02-52d7a36a22e1/test_report.txt')
