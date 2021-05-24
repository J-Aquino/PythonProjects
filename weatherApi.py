from typing import List
import requests
import json
import operator

base_url = "https://www.metaweather.com/api"
woeid = {}
city_data = {}
query = input("provide query: ")

def search_locations(query):
	url = "https://www.metaweather.com/api/location/search/?query={query}"
	filter = {'query': query}
	city = []
	city_response = requests.get(url, params=filter)
	cities = city_response.json()
	woeid = dict({ "worldID": []});

	for city_response in cities:
		city.append({
			"City": city_response.get('title')
			})
		city_data = {
			city_response.get('woeid'):city_response.get('title')
		}
		woeid["worldID"].append(city_response.get('woeid'))
		print(city_data)

	
	print("Filter has returned these results: ")
	print(city)
	#return(city_data)
	return(woeid["worldID"])
	
	
def temperatures_for_location(woeid):
	
	base_url = "https://www.metaweather.com/api/location/{}/"
	
	print(woeid)
	temperature_values = []
	
	url = base_url.format(woeid)
	temperature_response = requests.get(url)
	temperatures = temperature_response.json()
	for temperature_response in temperatures["consolidated_weather"]:
		
		temperature_values.append(temperature_response.get('the_temp'))
	return(temperature_values)

	
def calculate_temperature_average(temperature_values):
	count = 0
	sum = 0
	for i in temperature_values:
		count += 1
		sum += i
	average = sum/count
	
	print(average)
	print("Average temperature for woeid location: ")
	return(average)    


def sum_digits(num):
	num_as_string = str(num)
	sum_list = []
	for element in num_as_string:
		sum_list.append(element)
	#print(sum_list)
	sum = 0
	for i in sum_list:
		sum += int(i)
		sum = int(sum)
	#print(sum)

	return(sum)
    

def is_harshad_number(sum):
	sum = sum_digits(num)
	print(num)
	print(sum)
	#harshad = []
	
	if num % sum == 0:
		print("true, harshad number")
		#harshad.append(num)
	else:
		print("false, not harshad number")
	#print(harshad)
	#return(harshad)


if __name__ == '__main__':
	woeids = search_locations(query)
	print("Woeids for locations from the filter are: ", woeids)
	averages = []
	for woeid in woeids:
		temps = temperatures_for_location(woeid)
		average = calculate_temperature_average(temps)
		average_info = {
  			'woeid': woeid,
  			'average': average
		}
		averages.append(average_info)
	
	max_average = 0
	max_woeid = 0
	for average in averages:
		if average['average'] > max_average:
			max_average = average['average']
			max_woeid = average['woeid']
	print("Highest average temperature is: ", max_average)
	print("at this location: ", max_woeid)
	
	for average in averages:
		num = average['average']
		num = int(num)
		print("average number found: ", num)
		sum_digits(num)
		is_harshad_number(sum)
		#print(averages)
		#harshad = is_harshad_number(sum)
		#print(harshad)

#TODO:
"""
Final portion is the output of the harshad numbers in the desired format.
Essentially the last bit would be to put all confirmed 
harshad numbers into a list, then use the dictionary 
in averages to compare and connect the woeid's to the average temperatue value.
Finally using the dictionary
city_data found in the function search_locations as a lookup table to match those 
woeid's to their city and then print out the harshad numbers in the desired fashion
[San Franciscto: 18]
"""
	
	
