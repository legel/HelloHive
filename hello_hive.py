# To install the "hiver" Python library:

# 1. Go to your site-packages directory for the Python installation of choice.
# cd username/lib/pythonX.Y/site-packages

# 2. Clone the "hiver" library here
# git clone https://github.com/tebeka/hiver.git

# 3. Go into the "hiver" folder, and install it
# cd hiver
# python setup.py install

# The following should now work.  

import hiver

# connect to the cluster
host = 'hive2-10001-prod-nydc1.nydc1.outbrain.com'
port = 10010
client = hiver.connect(host,port)
# authentication may be as simple as adding 'user' and 'password' in the hiver.connect() call above
# hiver is built from code that authenticates as documented here: https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2

# specify parameters
table = 'Beasts'
key = 'Beast_Type'
value = '\'Cats\''

query = 'SELECT * FROM {0} WHERE {1} = {2} LIMIT 1'.format(table, field, value)

print 'The following query will be sent to Hive:'
print query

# execute the query by passing the string to the connection
print '\nExecuting query... This may take several seconds. (Errors are returned here.)'
client.execute(query)
# get a list of documents matching the query, where each document is a tab-delimited string
responses = client.fetchAll()

# convert each tab-delimited string to a list of fields that are indexable
documents = []
for response in responses:
	document = response.split('\t')
	documents.append(document)

# now all of your fields from all of your Hive documents can be easily and quickly processed as you wish in Python
print '\nThe 1st document:'
print documents[0]
print '\nThe 1st field in the 1st first document:'
print documents[0][0]