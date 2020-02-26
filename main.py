import requests
from bs4 import BeautifulSoup
import operator

response = requests.get(
    'https://www.lotteryusa.com/powerball/pb-year.html')


soup = BeautifulSoup(response.text, 'lxml')

body = soup.find('tbody')

rows = body.findAll('tr', class_=None)

list_of_numbers = []

for row in rows:
    data = row.find('td', class_='result')
    ul = data.find('ul', class_='draw-result list-unstyled list-inline')
    m_list = ul.findAll('li', class_=None)
    for lt in m_list:
        list_of_numbers.append(lt.text)

set_numbers = set(list_of_numbers)

count_of_numbers = {}

for num in set_numbers:
    count_of_numbers[num] = 0

for num in list_of_numbers:
    count_of_numbers[num] += 1

sorted_by_count = sorted(count_of_numbers.items(), key=operator.itemgetter(1))

most_repeated = sorted_by_count[-5:]

nums = [x[0] for x in most_repeated]
print(nums)
