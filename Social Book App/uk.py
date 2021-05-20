import pandas as pd
file_data = open('adminRecords.txt', 'r').read().splitlines()  # Read your file
data = pd.DataFrame(columns=['username', 'full Name', 'email'])
file = []  # filennames
le = []  #length of file
pattern = []  # patterns
for f in file_data:
    s = f.split(" ", 2) #Two times split on space to get a list of all three parameters
    file_name = s[0].split('.', 1)[1] #extracting just the file name ignoring numbers
    length = s[1]
    pattern.append()
    file.append(file_name)
    le.append(length)
data['username'] = file
data['full Name'] = le
data['email'] = pattern
print(data)