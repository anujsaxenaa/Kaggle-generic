import requests
import pandas as pd
import bs4
import os
import wget
from subprocess import call

kaggle_url = 'https://www.kaggle.com'

download_data = lambda x:call(['wget','-x','-c','--load-cookies','kaggle.com_cookies.txt','-P',x['competition_name']+'/data/compressed_files','-nH','--cut-dirs=5',x['full_download_link'],'--no-check-certificate'])

folders = ['data/compressed_files','code','submissions']


def create_folders(competition_name):
    call(['mkdir','-p',competition_name+'/'+folders[0]])
    call(['mkdir','-p',competition_name+'/'+folders[1]])
    call(['mkdir','-p',competition_name+'/'+folders[2]])
    return None


def download_kaggle_competition_data(competition_name,list_of_downloadable_files):
    competition_url = kaggle_url+'/c/'+competition_name
    print 'downloading data for the competition:', competition_url
    r = requests.get(competition_url+'/data')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    fdf = pd.DataFrame(list_of_downloadable_files,columns=['files'])
    fdf['competition_name'] = competition_name
    fdf['download_link'] = fdf.files.map(lambda x:[ i['href'] for i in soup.find_all('a', { 'name': x }, href=True) ][0])
    fdf['full_download_link'] = fdf.download_link.map(lambda x:kaggle_url+x)
    fdf.apply(download_data,axis=1)
    print 'finished'
    return fdf


def uncompress_kaggle_competition_data(file_path,store_location):

    if file_path.endswith('.csv') is not True:

        if file_path.endswith('.zip'):
            call(['unzip',file_path,'-d',store_location])

        elif x.endswith('.gz') or file_path.endswith('tar'):
            call(['gzip',file_path])

        else:
            print 'new format found'

    else:
        print 'already uncompressed'
    return None
