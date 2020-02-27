import requests
from bs4 import BeautifulSoup
from random import choice

source = requests.get(
    'https://www.lotteryusa.com/powerball/pb-year.html').text


soup = BeautifulSoup(source, 'lxml')

body = soup.tbody
rows = body.findAll('tr', class_=None)


# gives you the list of all numbers that was in the winning lotteries
def get_winning_numbers():
    list_of_numbers = []
    for row in rows:
        data = row.find('td', class_='result')
        ul = data.find('ul', class_='draw-result list-unstyled list-inline')
        m_list = ul.findAll('li', class_=None)
        for lt in m_list:
            list_of_numbers.append(lt.text)
    return list_of_numbers

# gives you the list of all powerballs


def get_all_powerballs():
    powerballs = []
    for row in rows:
        data = row.find('td', class_='result')
        ul = data.find('ul', class_='draw-result list-unstyled list-inline')
        m_list = ul.findAll('li', class_='bonus powerball')
        for lt in m_list:
            pb = lt.text.split()
            powerballs.append(pb[0])
    return powerballs


# gives you the dictionary of the winning number with its count
def get_count_dictionary(number_list):
    count_of_numbers = {}
    set_numbers = set(number_list)
    for num in set_numbers:
        count_of_numbers[num] = 0
    for num in number_list:
        count_of_numbers[num] += 1
    return count_of_numbers

# gives the list of most repeated numbers


def get_most_repeated_nums(numbers_count):
    repeated_counts = sorted(numbers_count.values())
    five_most_repeated_counts = repeated_counts[-5:]
    nums = []
    for key in numbers_count:
        if numbers_count[key] in five_most_repeated_counts:
            nums.append(key)
    return nums

# gets most repeated powerballs


def get_most_repeated_powerballs(numbers_count):
    repeated_counts = sorted(numbers_count.values())
    most_repeated_count = repeated_counts[-1]
    nums = []
    for key in numbers_count:
        if numbers_count[key] == most_repeated_count:
            nums.append(key)
    return nums


# gets the draw with last number being powerball


def get_draw(numbers):
    lottery_draw = []
    for _ in range(5):
        random_num = choice(numbers)
        numbers.remove(random_num)
        lottery_draw.append(random_num)
    lottery_draw = sorted(lottery_draw)
    lottery_draw.append(choice(get_most_repeated_powerballs(
        get_count_dictionary(get_all_powerballs()))))
    return lottery_draw


winning_list = get_winning_numbers()
count = get_count_dictionary(winning_list)
numbers = get_most_repeated_nums(count)
draw = get_draw(numbers)
print(draw)
