# Mission to Mars
CWRU Bootcamp Homework Week 12

The purpose of this project was to build a webscraper using BeautifulSoup and Splinter with Python to build a website hosted using Flask that can grab updated Mars information. The sources for the website were [NASA's Mars News Site](https://mars.nasa.gov/news/), the [Jet Propulsion Lab ('JPL') Mars & Space Image Website](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars), [Space Facts on Mars](https://space-facts.com/mars/), and the [USGS Astrogeology Website Images of Mars](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

### Webscraper

The webscraper was built using a [Jupyter Notebook](https://github.com/Lbrady1025/web-scraping-challenge/mission_to_mars.ipynb). The libraries used were BeautifulSoup, Splinter, and Pandas. The scraper goes out to the above-referenced websites, navigates through the pages, and saves certain information as variables that can then be later displayed on the webpage.

### Flask App

The scraper from the Jupyter Notebook was then converted into a [Python app](https://github.com/Lbrady1025/web-scraping-challenge/scrape_mars.py) that contained a function of the scraper. This app was then added to the a [Flask app](https://github.com/Lbrady1025/web-scraping-challenge/app.py) that contains a root route and a route that runs the scraper app so that the end user can scrape for new Mars data on demand.

### Webpage

The front end of the website was built with Bootstrap using the render template function of Flask. The page displays a header with a button that can be used to run the webscraper, and the latest news headline from the NASA Mars News site:

![Header and Latest Headline](/screenshots/website_header.PNG)

Next, the page displays the latest featured image from the JPL site, and a table of facts scraped about Mars:

![JPL Image and Facts Table](/screenshots/featured_photo_facts.PNG)

Finally, the page displays the hemispheres of Mars gathered from the USGS Astrogeology website:

![First Hemisphere](/screenshots/hemisphere_one.PNG)

![All Hemispheres from Mobile View](/screenshots/hemisphere_all.PNG)
