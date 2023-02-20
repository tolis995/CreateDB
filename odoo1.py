# #5e9172693b676c29ac5640d7fd6bd910ff27acf2
import xmlrpc.client
#
# # Connect to the server
client = xmlrpc.client.ServerProxy('https://integrationrabbit.methodoos.com/xmlrpc/2/common')
#
# # Authenticate
uid = client.authenticate('integrationrabbit', 'testuser', 'testuser@#$', {})
print(uid)
# # Create a new record
# # record_id = client.create('integrationrabbit', uid, 'yourpassword', 'res.partner', {
# #     'name': 'John Smith',
# #     'email': 'john
#
# # Search for records
# # records = client.execute_kw('integrationrabbit', uid, 'testuser@#$', 'res.partner', 'search_read', [[]], {'fields': ['name', 'email', 'phone']})
# rec = client.
# # Print the records
# for record in rec:
#     print(record)

# Search for records
records = client.execute_kw('integrationrabbit', uid, 'testuser@#$', 'sale.order', 'search_read', [[]], {'fields': ['model', 'name']})

# Print the records
for record in records:
    print(f"Model: {record['model']} | Name: {record['name']}")
