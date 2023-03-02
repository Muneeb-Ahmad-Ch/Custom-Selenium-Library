from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
import string
import random
from datetime import datetime
import undetected_chromedriver as uc
import pathlib
import os
import pickle

#############
# constants #
#############
# update url here :
BASE_URL = 'https://www.google.com/'
#######################

#######################
# getting current path of script
PATH = os.path.dirname(os.path.realpath(__file__))
UTIL_PATH = r'utils\\'  # to be used to store files like cookies etc
########################


#############
# Functions #
#############


def get_current_datetime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("(%H:%M:%S %d-%m-%Y)")
    return dt_string
