import requests
from bs4 import BeautifulSoup
from random import choice

source = requests.get(
    'https://www.lotteryusa.com/powerball/pb-year.html').text


soup = BeautifulSoup(source, 'lxml')

body = soup.tbody
rows = body.findAll('tr', class_=None)


def get_winning_numbers():
    list_of_numbers = []
    for row in rows:
        data = row.find('td', class_='result')
        ul = data.find('ul', class_='draw-result list-unstyled list-inline')
        m_list = ul.findAll('li', class_=None)
        for lt in m_list:
            list_of_numbers.append(lt.text)
    return list_of_numbers


def get_count_dictionary(winning_numbers_list):
    count_of_numbers = {}
    set_numbers = set(winning_numbers_list)
    for num in set_numbers:
        count_of_numbers[num] = 0
    for num in winning_numbers_list:
        count_of_numbers[num] += 1
    return count_of_numbers


def get_most_repeated_nums(numbers_count):
    repeated_counts = sorted(set(sorted(numbers_count.values())))
    five_most_repeated_counts = repeated_counts[-5:]
    nums = []
    for key in numbers_count:
        if numbers_count[key] in five_most_repeated_counts:
            nums.append(key)
    return nums


def get_five_random_numbers(numbers):
    lottery_draw = []
    for _ in range(5):
        random_num = choice(numbers)
        lottery_draw.append(random_num)
    return lottery_draw


winning_list = get_winning_numbers()
count = get_count_dictionary(winning_list)
numbers = get_most_repeated_nums(count)
draw = get_five_random_numbers(numbers)
print(draw)
