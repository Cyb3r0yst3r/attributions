import socket
import sys
import os

# resolve a text file containing a list of hostnames and take a screen shot
# Takes 2 arguments (1) input_subdomains_file, and (2) image_directory (for example: /tmp/fqdnimages/)

fList = sys.argv[1]
oDir = sys.argv[2]

notResolvable = 0
reSolvable = 0

with open(fList, "r") as ins:
   for line in ins:
      hostName = line.strip()
      hostName = hostName[:-1]   # Remove comma
      
      print ("HOSTNAME = [{}]" .format(hostName))
      try:
         ipAddr = socket.gethostbyname_ex(hostName)
      except socket.error:
         notResolvable += 1
         print(f"Not resolvable = " + str(notResolvable))
      else:
         webSite = "curl \"https://website-screenshot.whoisxmlapi.com/api/v1?apiKey=<YOUR_API_KEY>&url=" + hostName + "&credits=DRS\" -o " + oDir + hostName + ".jpg"
         os.system(webSite)
         print(webSite)
         reSolvable += 1
         print(f"Resolvable = " + str(reSolvable))
