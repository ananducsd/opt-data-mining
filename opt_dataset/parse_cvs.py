import csv
import time
from selenium import webdriver

## Use PhantomJS through selenium webdriver

newfile = open("opt.json", 'w')
driver = webdriver.PhantomJS()                  # Get new connection/ this can go outside the loop.
driver.set_window_size(1120, 550)               # Set windows size, just for screenshoots debug

ITNUM = 5
iteration = 0
data = {}
with open('opt.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        # Parse and get User Data
    	data['userName'] = row[0]
    	data['docID'] = row[1]
    	data['postedDate'] = row[2]
    	data['recievedDate'] = row[3]
        # Get Comment from the web
	try:
    	driver.get(row[4])                              # Get web link
		driver.execute_script('document.title')         # Execute scripts inside
		if (iteration == 0): 
			time.sleep(5)                                # Wait until the page downloads (Extremly important)
		else:
			time.sleep(0.5)
		element = driver.find_element_by_xpath("//div[@class='GCARQJCDEXD']")
		comment = element.text                          # Get parsed comment text
	except:
		comment = "N/A"
		print comment
        data['comment'] = comment.encode('ascii', 'ignore').replace("\n", " ")               
        # Write data to JSON file
	    print "Iteration Num: ", iteration
        print data
        newfile.write(str(data) + '\n')                 
     	iteration = iteration + 1
        # DEBUG only 
        # if (iteration >= ITNUM):
			# break
    
driver.quit()
newfile.close()
