#from grs import Stock
import sys
import csv
import datetime
import operator

def readCSV(filename):
	"return list of every year"
	data = {}
	with open(filename, newline='') as f:
		reader = csv.reader(f)
		i = 0
		for row in reader:
			if row == []:
				continue
			i = i + 1
			date = str(row[0])
			dateFormat = date.split('/')
			year = str(int(dateFormat[0]) + 1911) #get year
			month = dateFormat[1]
			day = dateFormat[2]
			if not year in data:
				data[year] = []
			row[0] = datetime.date(int(year), int(month), int(day)) #convert date to datetime object
			data[year].append(row)
	return data

def calYearAVG(data):
	yearAVG = {}
	for key, value in data.items():
		i=0
		lastMonth=0
		count=0
		sum=0		
		monthAVG = {}
		yearCount=0
		yearSum=0
		while i<len(value):
			dayInfo=value[i]

			if lastMonth == 0:
				lastMonth = dayInfo[0].month

			if dayInfo[0].month > lastMonth:
				monthAVG[lastMonth] = sum/count
				count=0
				sum=0	
			count=count+1
			yearCount=yearCount+1
			sum = sum+float(dayInfo[6])
			yearSum=yearSum+float(dayInfo[6])
			lastMonth = dayInfo[0].month

			if i == len(value)-1:
				monthAVG[lastMonth] = sum/count

			i=i+1
		monthAVG[0] = yearSum/yearCount
		yearAVG[key] = monthAVG
	return yearAVG


if __name__ == '__main__':
	#0. ���
	#1. ����Ѽ�
	#2. ������B
	#3. �}�L��
	#4. �̰����]��^
	#5. �̧C��
	#6. ���L��
	#7. ���^���t
	#8. ���浧��
	data = readCSV(filename='E:\\2330.csv')
	yearAVG = calYearAVG(data)

	cal = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
	for key, value in yearAVG.items():
		del value[0]
		sorted_x = sorted(value.items(), key=operator.itemgetter(1))
		if len(sorted_x) == 12:
			i=0
			while i<12:
				cal[sorted_x[i][0]] = cal.get(sorted_x[i][0])+(i+1)
				i=i+1
	
	total=sum(cal.values())
	for key, value in cal.items():
		cal[key] = cal.get(key)/total
	sorted_x = sorted(cal.items(), key=operator.itemgetter(1))
	input()
	sys.exit()