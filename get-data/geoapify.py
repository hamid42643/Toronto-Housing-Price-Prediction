import csv
import requests
import logging
import traceback
import hashlib
from config import api_key_geoapify, api_key_rapidapi


# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Dictionary to store address hashes and their coordinates
address_coords = {}

def fetch_coordinates(address):
    # Calculate the hash of the address
    address_hash = hashlib.md5(address.encode()).hexdigest()
    
    # Check if the address hash exists in the dictionary
    if address_hash in address_coords:
        print(f"Coordinates already fetched for address: {address}")
        return address_coords[address_hash]['latitude'], address_coords[address_hash]['longitude'], None
    url = "https://geoapify-platform.p.rapidapi.com/v1/geocode/search"
    querystring = {
        "apiKey": api_key_geoapify,
        "text": address,
        "lang": "en",
        "limit": "1"
    }
    headers = {
        "X-RapidAPI-Key": "fde14828b3mshf6e3fb96f616c1dp1f1597jsn9a25fc2af5f2",
        "X-RapidAPI-Host": "geoapify-platform.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code != 200:
            error_message = f"API request failed with status code {response.status_code} for address: {address}"
            logging.error(error_message)
            return None, None, error_message
        data = response.json()
        if data.get('features'):
            feature = data['features'][0]
            latitude = feature['properties']['lat']
            longitude = feature['properties']['lon']
            
            # Store the address hash and coordinates in the dictionary
            address_coords[address_hash] = {'latitude': latitude, 'longitude': longitude}
            
            return latitude, longitude, None
        else:
            error_message = f"No coordinates found for address: {address}"
            logging.error(error_message)
            return None, None, error_message
    except Exception as e:
        error_message = f"Error occurred while fetching coordinates for address: {address}. Cause: {str(e)}"
        logging.error(error_message)
        traceback.print_exc()  # Print the full traceback of the exception
        return None, None, error_message

def process_rows(rows, writer):
    for row in rows:
        latitude = row['latitude']
        longitude = row['longitude']
        street_address = row['streetAddress']
        city = row['city']
        state = row['state']
        
        # Check if latitude and longitude are missing
        if not latitude or not longitude:
            # Construct the full address
            address = f"{street_address}, {city}, {state}"
            print(f"Processing row: {address}")
            
            # Fetch coordinates for the address
            latitude, longitude, error_message = fetch_coordinates(address)
            
            # If coordinates are retrieved successfully
            if latitude and longitude:
                # Update the row with the fetched coordinates
                row['latitude'] = latitude
                row['longitude'] = longitude
                
                # Write the updated row to the output CSV file
                writer.writerow(row)
                print(f"Coordinates fetched for address: {address}")
            else:
                # Print the cause of the failure to fetch coordinates
                print(f"Failed to fetch coordinates for address: {address}. Cause: {error_message}")
        else:
            # Write the row to the output CSV file if coordinates are already present
            writer.writerow(row)
            print(f"Skipping row with existing coordinates: {street_address}, {city}, {state}")

def main():
    try:
        # Open the input CSV file
        with open('dataset.csv', mode='r') as input_file:
            reader = csv.DictReader(input_file)
            rows = list(reader)
        
        # Open the output CSV file
        with open('all_updated2.csv', mode='w', newline='') as output_file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            
            # Write the header row to the output CSV file
            writer.writeheader()
            
            # Process each row and fetch coordinates
            process_rows(rows, writer)
        
        print("Updated CSV file created: all_updated.csv")
    except FileNotFoundError as e:
        logging.error(f"File not found: {str(e)}")
        traceback.print_exc()  # Print the full traceback of the exception
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        traceback.print_exc()  # Print the full traceback of the exception

if __name__ == '__main__':
    main()