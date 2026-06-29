from faker import Faker
fake_data = Faker()
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
for i in range(10):
    print(fake_data.name())



# print(fake_data.first_name())
# print(fake_data.last_name())
# print(fake_data.email())
# print(fake_data.phone_number())