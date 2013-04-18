Bootstrap server (Node.js):
---------------------------

Stores the 'Meeting id - Master IP' table.

The table is stored in 'files/meetings' for recovery in case of server crash. 

HTTP requests processed:

1. http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/insert?id=123&ip=123.23.45.23

2. http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/lookup?id=123

3. http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/table

4. http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/clear
