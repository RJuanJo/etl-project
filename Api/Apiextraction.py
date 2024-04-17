import requests
import csv

#URL AND TOKEN
url = "https://api.apify.com/v2/datasets/xblAhnLzFKh5s3upE/items"
token = "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf"
response = requests.get(url, params={"token": token})

if response.status_code == 200:
    data = response.json()
    csv_file = "dataBL.csv"

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"The data has been successfully saved to '{csv_file}'.")
else:
    print("Error:", response.status_code)


#URL AND TOKEN
url = "https://api.apify.com/v2/datasets/hgh9xbDJVMbo14z3H/items"
token = "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf"
response = requests.get(url, params={"token": token})

if response.status_code == 200:
    data = response.json()
    csv_file = "dataBC.csv"

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"The data has been successfully saved to '{csv_file}'.")
else:
    
    print("Error:", response.status_code)


#URL AND TOKEN
url = "https://api.apify.com/v2/datasets/GnngHjfOFgZ4OEWP8/items?"
token = "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf"
response = requests.get(url, params={"token": token})

if response.status_code == 200:
    data = response.json()
    csv_file = "dataJT.csv"

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"The data has been successfully saved to '{csv_file}'.")
else:
    print("Error:", response.status_code)


