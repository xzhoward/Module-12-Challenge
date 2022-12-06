### 10.3.3 Scrape Mars Data: The News
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Path to chromedriver (macOS users only)
# !which chromedriver

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
#url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
# add the find element, find(where to look, key word = give it a name)
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

## JPL Space Images Featured Image
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

### 10.3.5 Scrape Mars Data: Mars Facts
## Mars Facts
# Create a data frame with space facts
df = pd.read_html('http://space-facts.com/mars/')[0]
df.head()

# df.columns=['Description', 'Mars']
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# view as html code
df.to_html()

# close the browser
browser.quit()

