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
	for entry in ip:
		entry[2] = date_conv(entry[2])
		print(entry)
#------------------------
#sortIP. Return sorting key for list
def sortIP(inStr):
	return conv(inStr)[3]
#------------------------
def conv(inStr):
	return tuple(int(okt) for okt in inStr[0].split('.'))
#------------------------
def date_conv(inStr):
	vocMth = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Okt":"10","Nov":"11","Dec":"12"}
	inStr = tuple(dt for dt in inStr.split(' '))
	retStr = inStr[1]+"/"+vocMth[inStr[0]]+" "+inStr[2]
	return retStr
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