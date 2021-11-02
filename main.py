import json
import re

class CountryIterator:
	host = 'https://en.wikipedia.org/wiki'

	def __init__(self, path_open, path_write):
		self.file_open = open(path_open)
		self.file_write = open(path_write, 'w', encoding='utf-8')

	def __iter__(self):
		self.countries_data = json.load(self.file_open)
		return self

	def __next__(self):
		if not self.countries_data:
			self.file_open.close()
			self.file_write.close()
			raise StopIteration
		country = self.countries_data.pop()
		country_name = re.sub(' ', '_', country['name']['common'])
		country_link = f'{self.host}/{country_name}'
		self.country_dict = {country_name: country_link}
		self.file_write.write(f'{country_name}: {country_link}\n')
		return self.country_dict


for country in CountryIterator("countries.json", "text_1.txt"):
	print(country)
