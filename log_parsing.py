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
with open(FilePath) as f:
    cnts = Counter(l.strip() for l in f)

# Display 3 most common lines
cnts.most_common(3)

# Display 3 least common lines
cnts.most_common()[-3:]

#Tanner splitting file into more files
input = open(FilePath, "r")
outputJan = open("JanuaryLog.txt", "w")
outputFeb = open("FebuaryLog.txt", "w")
outputMar = open("MarchLog.txt", "w")
outputApr = open("AprilLog.txt", "w")
outputMay = open("MayLog.txt", "w")
outputJun = open("JuneLog.txt", "w")
outputJul = open("JulyLog.txt", "w")
outputAug = open("AugustLog.txt", "w")
outputSep = open("SeptemberLog.txt", "w")
outputOct = open("OctoberLog.txt", "w")
outputNov = open("NovemberLog.txt", "w")
outputDec = open("DecemberLog.txt", "w")

for line in input:
	if "/Jan/" in line:
		outputJan.write(line)
	elif "/Feb/" in line:
		outputFeb.write(line)
	elif "/Mar/" in line:
		outputMar.write(line)
	elif "/Apr/" in line:
		outputApr.write(line)
	elif "/May/" in line:
		outputMay.write(line)
	elif "/Jun/" in line:
		outputJun.write(line)
	elif "/Jul/" in line:
		outputJul.write(line)
	elif "/Aug/" in line:
		outputAug.write(line)
	elif "/Sep/" in line:
		outputSep.write(line)
	elif "/Oct/" in line:
		outputOct.write(line)
	elif "/Nov/" in line:
		outputNov.write(line)
	elif "/Dec/" in line:
		outputDec.write(line)

input.close()
outputJan.close()
outputFeb.close()
outputMar.close()
outputApr.close()
outputMay.close()
outputJun.close()
outputJul.close()
outputAug.close()
outputSep.close()
outputOct.close()
outputNov.close()
outputDec.close()
