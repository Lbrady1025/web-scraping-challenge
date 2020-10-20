#Dependencies
import pandas as pd 
from splinter import Browser
from bs4 import BeautifulSoup
import requests

def scrape():
    #Set up path for browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Open URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #Grab latest headline
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div',class_='image_and_description_container').find('div',class_='content_title').find('a').text
    news_p = soup.find(class_='article_teaser_body').text

    #Navigate to JPL Mars featuered image
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(jpl_url)
    browser.find_by_id('full_image').click()

    #Navigate to image page
    browser.find_link_by_partial_text('more info').click()

    #Get to fullsize image
    browser.find_link_by_partial_href('/spaceimages/images').click()

    #Scrape image URL
    featured_image_url = browser.url

    #Get Mars facts with Pandas
    facts_url = 'https://space-facts.com/mars/'

    tables = pd.read_html(facts_url)

    #Slice off other tables
    df = tables[0]

    df = df.rename({'0':'Description','1':'Mars'})

    df.reset_index()

    #Convert to HTML
    facts_table = df.to_html()

    #Get Mars hemisphere pictures
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemi_url)
    soup = BeautifulSoup(browser.html)  

    img_title = []
    title = soup.find_all('h3')
    for x in title:
        img_title.append(x.text)

    images = []
    counter=0
    for x in img_title:
        browser.find_by_css('img.thumb')[counter].click()
        images.append(browser.find_by_text('Sample')['href'])
        counter = counter+1
        browser.back()

    hemisphere_image_urls = []
    counter=0
    for x in title:
        hemisphere_image_urls.append({'title':img_title[counter],'img_url':images[counter]})
        counter = counter + 1

    browser.quit()
    
    return {'headline':news_title,'article_detail':news_p,'feat_img':featured_image_url,'table':facts_table,'hemisphere_imgs':hemisphere_image_urls}