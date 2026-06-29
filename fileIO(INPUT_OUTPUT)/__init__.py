# # Manual steps to write a file
# OPEN NOTEPAD AND CREATE A FILE
# WRITE IN FILE
# CLOSE THE FILE

#MODES
# READ MODE -  r
# WRITE MODE - w
# APPEND - a
# READ/ WRITE - r+

# f = open('file name', 'mode')
# f = open("writedemo.txt", "w")
# f.write("hello this is a demo ")
# f.close()
# real example is to store list from any website to the destination in local
f = open("writedemo.txt", "a")
l = [23, 45, 89, 90, 200]
for items in l:
    f.write((str(items))+"\n")
f.close()

# Note write mode will override the old values passed with new values
# But Append method will append into the same file(it will add the same value but will
# not replace old one)

# Read mode
f = open("writedemo.txt", "r")
print(f.read())
f.close()

# In order to read line one by one read line method is used
# print(f.readline())
# f.close()

