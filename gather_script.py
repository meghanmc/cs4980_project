import time
import datetime
import os
# Continue running the script up to November 19th
while(datetime.datetime.now().day < 19):
	# Run the script starting Sun. November 11th until Sun. November 18th (1 week)
	while(datetime.datetime.now().day >= 11 and datetime.datetime.now().day < 19):
		timestamp = str(time.time())
		cmd = "curl -s https://venmo.com/api/v5/public -o venmo" + timestamp + ".json"
		os.system(cmd)
		time.sleep(30)
