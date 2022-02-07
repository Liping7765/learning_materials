import requests
# Define the remote file to retrieve
remote_url = "https://files.51voa.cn/202202/in-thailand-cafe-serves-coffee-and-investment-advise-serving.mp3"
# Define the local filename to save data
local_file = 'local_copy.mp3'
# Make http request for remote file data
data = requests.get(remote_url)
# Save file data to local copy
with open(local_file, 'wb') as file:
    file.write(data.content)

"""
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

"r" - read only 
    f = open("demofile.txt", "r")
    print(f.read(5))

    f = open("demofile.txt", "r")
    print(f.readline())

"""