# Exercise 5
# Create a fixture named login_data that returns:
# {
#     "username": "admin",
#     "password": "admin123"
# }
# Write a test that verifies both values.
def test(login_data):
    print(login_data)
    assert login_data['username'] == 'admin'
    assert login_data['password'] == 'admin123'