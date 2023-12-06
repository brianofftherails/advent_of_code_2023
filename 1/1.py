#!/bin/env python3

import re

def convert_and_sum(text):
    number_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Replace written numbers with their numerical equivalents
    for word, number in number_map.items():
        text = text.replace(word, number)

    # Extract all numbers from the string
    numbers = re.findall(r'\d', text)

    if numbers:
        return int(numbers[0]) + int(numbers[-1])
    else:
        return 0

def main():
    #part1()
    part2()

def part1():
    fp = open("input.txt", "r")
    lines = fp.readlines()
    sum = 0
    for line in lines:
        sum += convert_and_sum(line)
    # for line in lines:
    #     line_arr = [*line]
    #     numbers = [char for char in line_arr if char.isnumeric()]
    #     val = int(numbers[0]+numbers[-1])
    #     # print(f"Found {val} for {line}")
    #     sum += val
    # # sum(map([[*line] for line in fp.readlines()], int))
    print(f"Sum: {sum}")
    fp.close()

def part2():
    numbers = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5",
               "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "zero" : "0"}
    fp = open("input.txt", "r")
    lines = fp.readlines()
    sum = 0
    for line in lines:
        oldline = line
        for key, value in numbers.items():
            line = line.replace(key, value)
        line_arr = [*line]
        num = [char for char in line_arr if char.isnumeric()]
        val = int(num[0]+num[-1])
        print(f"Found {val} for {line} (originally {oldline[:-1]})")
        sum += val
    # sum(map([[*line] for line in fp.readlines()], int))
    print(f"Sum: {sum}")
    fp.close()

if __name__ == "__main__":
    main()