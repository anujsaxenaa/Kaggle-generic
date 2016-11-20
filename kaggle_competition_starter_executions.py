import pandas as pd
import imp
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

kf = imp.load_source('kaggle_functions','/Users/Anuj/Desktop/Kaggle/functions/kaggle_functions.py')

path = '/Users/Anuj/Desktop/Kaggle/'
os.chdir(path)

competition_name = 'santander-product-recommendation' # as stated in the competition url
list_of_downloadable_files = ['sample_submission.csv.zip','test_ver2.csv.zip','train_ver2.csv.zip']

# Create Folders
kf.create_folders(competition_name)

# Download Data
kaggle_df = kf.download_kaggle_competition_data(competition_name,list_of_downloadable_files)
kaggle_df['files_path'] = competition_name+'/data/compressed_files/'+kaggle_df.files

# Uncomperss Data
kaggle_df.apply(lambda x:kf.uncompress_kaggle_competition_data(x['files_path'],x['competition_name']+'/data/'),axis=1)
print 'finished'
