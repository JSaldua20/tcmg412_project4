import os
import urllib.request
from collections import Counter

##Start the file by making sure the file is available
FilePath = './http_access_log.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
    print("It doesn't appear you have the data, downloading it now")
    url = "https://s3.amazonaws.com/tcmg476/http_access_log"
    urllib.request.urlretrieve(url,"./http_access_log.txt")

else:
    print ("It looks like you already have the file")

#Jonathan Part 5 and 6
# Read file directly into a Counter
with open('file') as f:
    cnts = Counter(l.strip() for l in f)

# Display 3 most common lines
cnts.most_common(3)

# Display 3 least common lines
cnts.most_common()[-3:]
