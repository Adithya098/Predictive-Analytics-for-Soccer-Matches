import requests
from bs4 import BeautifulSoup
import cloudscraper


def send_request(url):
    response = requests.get(url)
    status_code = response.status_code
    response_text = None
    if status_code == 200:
        response_text = response.text
    else:
        scraper = cloudscraper.create_scraper()
        response_text = scraper.get(url).text
        
    soup = BeautifulSoup(response_text, 'html.parser')
    return soup

def find_teams(soup):
    team = soup.find_all('span', class_='mc-summary__team-name u-hide-phablet')
    return {
        "home_team": team[0].text,
        "attack_team": team[1].text
        }

def find_attributes(soup):
# Find all <em> tags with a title attribute
    em_tags = soup.find_all('em', title=True)
    # Initialize a dictionary to store the mappings
    mappings = {}

    for em_tag in em_tags:
        title_value = em_tag['title']
        # Assuming the <span> tag immediately follows the <em> tag
        next_sibling = em_tag.find_next_sibling()
        
        # Extracting text from the next sibling if it's a <span> tag
        if next_sibling and next_sibling.name == 'span':
            span_text = next_sibling.get_text()
            mappings[title_value] = span_text
        
    return mappings

