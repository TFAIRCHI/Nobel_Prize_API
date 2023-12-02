import requests
import pandas as pd
from matplotlib import pyplot as plt
import sys

try:
    r = requests.request("GET",'https://api.nobelprize.org/2.1/laureates')
except:
    print('Error in requesting data from the API')
    sys.exit()

if __name__ == ('__main__'):    
    flat = r.json()

    Prize = pd.json_normalize(flat['laureates'],record_path=['nobelPrizes'],meta=['id','gender',['fullName','se'],['familyName','se']])

    Prize = Prize.sort_values(by='awardYear',ascending=True)

    prz_amt_year_gender = Prize.groupby(['awardYear','gender'],as_index=False)['prizeAmount'].sum()

    # List out columns
    year = prz_amt_year_gender['awardYear']
    amount = prz_amt_year_gender['prizeAmount']
    gender = prz_amt_year_gender['gender']

    # Build Charts
    plt.rcParams.update({'font.size':22})
    """Prize Amount Over The Years"""
    fig = plt.figure(figsize=(40,10))
    plt.xlabel('Year').set_fontsize(13.00)
    plt.ylabel('Amount Paid Out').set_fontsize(13.00)
    plt.title('Nobel Prizes Over The Years').set_fontsize(13.00)
    plt.bar(year,amount)
    plt.savefig("PrizePaidOut.pdf",format="pdf",bbox_inches="tight")

    plt.clf()
    """Prize Amount Over The Years"""
    fig = plt.figure(figsize=(15,15))
    plt.xlabel('Gender').set_fontsize(16.00)
    plt.ylabel('Amount Paid Out').set_fontsize(16.00)
    plt.title(f'Nobel Prizes By Gender')
    plt.bar(gender,amount)
    plt.savefig("PrizeByGender.pdf",format="pdf",bbox_inches="tight")
