import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Preset variables
zipcode = '10010'
cvs = r"https://www.cvs.com/content/safer-communities-locate"
cvs_url = r"http://www.cvssavingscentral.com/storelocator/SaferCommunities.aspx?zipcode="
table_id = "cphGlobal_cphDefault_cphSeasonal_gvStoreList"


# Function to parse through webpage
def pullPageData(url, zip, tabletag):
    print(url)
    url = url + zipcode
    page = requests.get(url)
    # Check page load
    if page.status_code == 200:
        # print(page.content)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', id=tabletag)
        # print(table)
        df = pd.read_html(str(table))[0]
        print(df)
        output_csv = os.path.join(os.getcwd(), 'output.csv')
        df.to_csv(output_csv, index=False, header=False)
    else:
        print('Page not loaded correctly. Status Code: ' + str(page.status_code))


pullPageData(cvs_url, zipcode, table_id)