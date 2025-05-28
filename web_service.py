from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from googletrans import Translator
import pyttsx3 as p
import requests

import feedparser

KEY = "387770587bb24811b93124938252305"

def get_israel_news():
    feed = feedparser.parse("https://www.ynet.co.il/Integration/StoryRss2.xml")
    return feed.entries[:5]


def get_weather(city):

    url = f"http://api.weatherapi.com/v1/current.json?key={KEY}&q={city}&lang=he"
    res = requests.get(url).json()
    country = res['location']['country']
    temp_c = res['current']['temp_c']
    feelslike_c = res['current']['feelslike_c']
    condition = res['current']['condition']['text']
    text = f"the weather is {city} {country} is {condition}, {temp_c} Celsius but it feel like {feelslike_c}"
    return text 

def get_time(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={KEY}&q={city}&lang=he"
    res = requests.get(url).json()
    country = res['location']['country']
    time = res['location']['localtime']
    hour, minutes = map(int, time.split(" ")[1].split(":"))
    period  ='PM' if hour > 12 else 'AM' 
    hour = hour -12 if hour > 12  else hour
    text = f"the time in {city}, {country} is {hour}:{minutes:02d}  {period}"
    return text


class translate():
    def __init__(self):
        self.translator = Translator()

    def get_translate(self, word):
        try:
            result = self.translator.translate(word, src='en', dest='he')
            return result.text
        except Exception as e:
            print("exeption: ", e)
            return None


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button/i')
        enter.click()
 
        try:
            content = self.driver.find_element(By.ID, "mw-content-text")
            paragraphs = content.find_elements(By.CSS_SELECTOR, "p")
            text = ""
            for p in paragraphs:
                if p.text.strip():
                    text = p.text.strip()
                    return text[:500]
             
        except Exception as e:
            print("Exception: "+e)


class youtube_play():
    def __init__(self):
         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
              #  chrome_options = Options()
                
    def get_play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query="+query)
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
