#!/usr/bin/python

import sys
import os

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class markdown:
    def __init__(self, id: int, title: str, solution: str, difficulty: str):
        self.id = id
        self.title = title
        self.solution = solution
        self.difficulty = difficulty

    def __str__(self):
        return f"|{self.id}|{self.title}|{self.solution}|{self.difficulty}|"

    def __repr__(self):
        return f"|{self.id}|{self.title}|{self.solution}|{self.difficulty}|"


def create_markdown(newline: str):
    filename = "README.md"

    path = os.path.join("", filename)

    file = open(path, "r")

    return_string = ""
    lines = file.readlines()
    lines.append(newline)

    return_string += "".join(lines[:8])
    markdown_arr = []

    for line in lines[8:]:
        line_arr = line.split("|")

        # Object Values
        mid = int(line_arr[1].strip())
        link = line_arr[2].strip()
        file_path = line_arr[3].strip()
        difficulty = line_arr[4].strip()

        markdown_obj = markdown(mid, link, file_path, difficulty)
        markdown_arr.append(markdown_obj)

    markdown_arr.sort(key=lambda x: x.id)

    return_string += "\n".join([str(x) for x in markdown_arr])
    return_string += "\n"

    file = open(path, "w")
    file.write(return_string)
    file.close()


if __name__ == "__main__":

    link = sys.argv[1]

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path=r"../chromedriver.exe", options=options)

    driver.get(link)

    title = (
        WebDriverWait(driver, 10)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[1]',
                )
            )
        )
        .text
    )

    diff = (
        WebDriverWait(driver, 10)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div',
                )
            )
        )
        .text
    )
    if diff == "Easy":
        sDiff = ":zap:"
    elif diff == "Medium":
        sDiff = ":zap: :zap:"
    else:
        sDiff = ":zap: :zap: :zap:"

    number = title.split(".")[0].strip()
    title = title.split(".")[1].strip()

    file = "".join(title.split())

    driver.close()

    file = "_".join([x.lower() for x in title.split()])
    inputfile = file + ".py"

    path = os.path.join("Algorithms/", diff)

    newline = f"|{number}|[{title}]({link})|[Python](./{path}/{inputfile})|{sDiff}|"

    if not os.path.exists(os.path.join(path, inputfile)):
        with open(os.path.join(path, inputfile), "w"):
            pass

    create_markdown(newline)
