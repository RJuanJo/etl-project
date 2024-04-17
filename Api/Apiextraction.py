import requests
import csv
import os

folder_path = 'data'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def save_data_to_csv(url, token, csv_filename):
    response = requests.get(url, params={"token": token})
    if response.status_code == 200:
        data = response.json()
        full_path = os.path.join(folder_path, csv_filename)
        
        with open(full_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        print(f"The data has been successfully saved to '{full_path}'.")
    else:
        print("Error:", response.status_code)

save_data_to_csv("https://api.apify.com/v2/datasets/xblAhnLzFKh5s3upE/items", "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf", "dataBL.csv")
save_data_to_csv("https://api.apify.com/v2/datasets/hgh9xbDJVMbo14z3H/items", "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf", "dataBC.csv")
save_data_to_csv("https://api.apify.com/v2/datasets/GnngHjfOFgZ4OEWP8/items", "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf", "dataJT.csv")
