import datetime
current_date_demo = datetime.datetime.today().date()
print(current_date_demo)
current_time_demo = datetime.datetime.today().time()
print(current_time_demo)

filename = current_time_demo.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(filename)