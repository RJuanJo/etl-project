import pandas as pd

def combine_datasets(dataset1, dataset2, dataset3):
    # List of columns we want to keep in the combination
    merge_columns = ['url', 'id', 'name', 'stars', 'numberOfGuests', 'address', 'roomType',
                     'location', 'reviews', 'pricing', 'isAvailable', 'photos', 'primaryHost',
                     'additionalHosts', 'isHostedBySuperhost', 'calendar', 'occupancyPercentage']
    merged_df = pd.merge(dataset1, dataset2, on=merge_columns, how='outer')
    merged_df = pd.merge(merged_df, dataset3, on=merge_columns, how='outer')
    merged_df.to_csv('data\dataApi.csv', index=False)
    print("Shape of the resulting DataFrame:", merged_df.shape)
    return merged_df

dataset1 = pd.read_csv('data\dataBl.csv')
dataset2 = pd.read_csv('data\dataBC.csv')
dataset3 = pd.read_csv('data\dataJT.csv')

combine_datasets(dataset1, dataset2, dataset3)
 