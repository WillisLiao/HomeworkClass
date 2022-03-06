# opening the file in read mode
my_file = open("1mil_paswrd.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
  
# printing the data
print(data_into_list)
my_file.close()
while True:
    a = input('your pw: ')
    if a in data_into_list:
        print('bad pw')
    elif a == "stop_code":
        break
    else:
        print('nice pw!')