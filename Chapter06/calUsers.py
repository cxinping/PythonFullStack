import os

users = os.popen('awk -F ":" \'{ print $1 , $7}\' /etc/passwd').readlines()
userCount = 0

for user in users:
	username, shell = user.split()
	userCount = userCount + 1
	print("username={0},shell={1}".format(username, shell) )
print("总用户数为={0}".format(userCount) )