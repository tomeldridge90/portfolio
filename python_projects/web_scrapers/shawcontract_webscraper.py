"""
This script is intended to scrape the Shaw Contract website to download
pictures of tiles along with some data about the images
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium import webdriver
import time
import re

browser = webdriver.Firefox()