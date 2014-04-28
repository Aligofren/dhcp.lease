#DHCP log parsing
#by Aligofren, 2014
import re
logFile = 'dhcpd.log'
ip=[]		#list all entry
ipq = []	#last leasing (unique values)
#------------------------
#main function. application entry point 
def main():
	hFile = open(logFile)
	# reading file into list
	for line in hFile.readlines():
		line = line[:-1]
		parser(line)
	# print list
	ip.sort(key=sortIP)
	unique(ip)
#------------------------
#sortIP. Return sorting key for list
def sortIP(inStr):
	return conv(inStr)[3]
#------------------------
def conv(inStr):
	return tuple(int(okt) for okt in inStr[0].split('.'))
#------------------------
def unique(inList):
	for i in range(len(inList)):
		print(inList[i][0])
#------------------------
def parser(pStr):
    p = re.compile(r'DHCPACK')
    strRes = p.search(pStr)
    if not strRes is None:
        p = re.compile(r'[A-z]{3} \d{2} (\d{2}\:){2}\d{2}')
        strDate = p.search(pStr)
        
        p = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
        strIp = p.search(pStr)
        
        p = re.compile(r'([a-f0-9]{2}\:){5}[a-f0-9]{2}')
        strMac = p.search(pStr)
        ip.append([	str(strIp.group()),
        			str(strMac.group()),
        			str(strDate.group())])
#------------------------
main()