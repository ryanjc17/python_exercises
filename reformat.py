import csv

input1 = 'test.csv'

market_data = {} #generate dictionary for market data

with open(input1, mode='r', encoding='utf-8-sig') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		csv_list = list(csv_reader)
		
		for row in csv_list:
			market = row['Market']				#define market as any row with 'market' as header
			cost = round(float(row['Cost']))		#define cost as any row with 'cost' as header
			impressions = round(float(row['Impressions']))	#define impressions as any row with 'impressions' as header

			if market not in market_data:						#if market not found in market data
				market_data[market] = {'Cost': 0.0, 'Impressions': 0.0}		#generate parameters for market dictionary for each market

			market_data[market]['Cost'] += cost			#add cost to each market every time its found in list	
			market_data[market]['Impressions'] += impressions	#add impressions to each market every time its found in list
		
for market, data in market_data.items():	#list unique markets with corresponding data
	print(f"Market: {market}\nTotal Cost: {data['Cost']}\nTotal Impressions: {data['Impressions']}\n**************")
