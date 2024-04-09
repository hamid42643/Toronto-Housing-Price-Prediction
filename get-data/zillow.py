import requests
import csv
from config import api_key_rapidapi

def fetch_zillow_data(zillow_uris, output_file):
    url = "https://zillow69.p.rapidapi.com/searchByUrl"
    headers = {
        "X-RapidAPI-Key": api_key_rapidapi,
        "X-RapidAPI-Host": "zillow69.p.rapidapi.com"
    }

    # Open the CSV file in write mode
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['isShowcaseListing', 'longitude', 'timeOnZillow', 'zestimate', 'daysOnZillow', 'zpid',
                         'taxAssessedValue', 'isUnmappable', 'priceForHDP', 'dateSold', 'state', 'isFeatured',
                         'isPremierBuilder', 'isPreforeclosureAuction', 'lotAreaValue', 'isNonOwnerOccupied',
                         'homeStatus', 'latitude', 'lotAreaUnit', 'bedrooms', 'zipcode', 'homeStatusForHDP',
                         'isZillowOwned', 'shouldHighlight', 'homeType', 'bathrooms', 'rentZestimate', 'price',
                         'city', 'streetAddress', 'country', 'currency', 'listing_sub_type', 'livingArea'])
        
        for zillow_uri in zillow_uris:
            print("fetching data for: ", zillow_uri)
            for page in range(1, 21):
                print("fetching data for page: ", page)
                querystring = {
                    "url": zillow_uri,
                    "page": str(page)
                }
                
                try:
                    response = requests.get(url, headers=headers, params=querystring)
                    response.raise_for_status()  # Raise an exception for unsuccessful requests
                    data = response.json()
                    
                    if 'props' in data and isinstance(data['props'], list):
                        for home in data['props']:
                            row = [
                                home.get('isShowcaseListing', ''),
                                home.get('longitude', ''),
                                home.get('timeOnZillow', ''),
                                home.get('zestimate', ''),
                                home.get('daysOnZillow', ''),
                                home.get('zpid', ''),
                                home.get('taxAssessedValue', ''),
                                home.get('isUnmappable', ''),
                                home.get('priceForHDP', ''),
                                home.get('dateSold', ''),
                                home.get('state', ''),
                                home.get('isFeatured', ''),
                                home.get('isPremierBuilder', ''),
                                home.get('isPreforeclosureAuction', ''),
                                home.get('lotAreaValue', ''),
                                home.get('isNonOwnerOccupied', ''),
                                home.get('homeStatus', ''),
                                home.get('latitude', ''),
                                home.get('lotAreaUnit', ''),
                                home.get('bedrooms', ''),
                                home.get('zipcode', ''),
                                home.get('homeStatusForHDP', ''),
                                home.get('isZillowOwned', ''),
                                home.get('shouldHighlight', ''),
                                home.get('homeType', ''),
                                home.get('bathrooms', ''),
                                home.get('rentZestimate', ''),
                                home.get('price', ''),
                                home.get('city', ''),
                                home.get('streetAddress', ''),
                                home.get('country', ''),
                                home.get('currency', ''),
                                str(home.get('listing_sub_type', '')),
                                home.get('livingArea', '')
                            ]
                            
                            # Write the data to the CSV file
                            writer.writerow(row)
                    else:
                        print(f"Error: Invalid 'props' data for URI: {zillow_uri}, Page: {page}")
                
                except requests.exceptions.RequestException as e:
                    print(f"Error: Request failed for URI: {zillow_uri}, Page: {page}")
                    print(f"Error details: {str(e)}")
                
                except (KeyError, ValueError) as e:
                    print(f"Error: Invalid response data for URI: {zillow_uri}, Page: {page}")
                    print(f"Error details: {str(e)}")
                
                except Exception as e:
                    print(f"Error: An unexpected error occurred for URI: {zillow_uri}, Page: {page}")
                    print(f"Error details: {str(e)}")

# uris with minium price of $1 to remove houses with no price
zillow_uris = [
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22max%22%3A0%2C%22min%22%3A0%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22max%22%3A1%2C%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22max%22%3A2%2C%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22max%22%3A3%2C%22min%22%3A3%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22max%22%3A4%2C%22min%22%3A4%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22max%22%3A5%2C%22min%22%3A5%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A5%7D%7D%2C%22isListVisible%22%3Atrue%7D",
"https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-84.18210196511527%2C%22east%22%3A-76.27194571511527%2C%22south%22%3A42.073968895386706%2C%22north%22%3A46.84535485162379%7D%2C%22mapZoom%22%3A7%2C%22usersSearchTerm%22%3A%22122%20Canada%20Dr%20Vaughan%2C%20ON%20L4H0E6%22%2C%22customRegionId%22%3A%220f6d16609dX1-CR1qu8r1vywp8kr_180h0y%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A5%7D%7D%2C%22isListVisible%22%3Atrue%7D",
]



output_file = 'zillow_homes_sold.csv'
fetch_zillow_data(zillow_uris, output_file)