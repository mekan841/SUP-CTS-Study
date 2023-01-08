#####################################################################################################################################
#######PREAMBLE#######
#####################################################################################################################################

#Hash this if not using Colab authenticate link to google drive and upload files
from google.colab import auth
import gspread
from google.auth import default
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)
from google.colab import drive 
drive.mount('/content/gdrive')

#hash this if do not need to upload files
from google.colab import files
uploaded = files.upload()

#import relevant libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg

#####################################################################################################################################
#######ANALYSIS#######
#####################################################################################################################################

#Read data
supdf=pd.read_csv('/content/Data Comparison of Outcomes SUP CTS Study.csv')

#Create comparison groups
supdf_prefeb20 = supdf[supdf['Pre Feb 2020'] == "Y"]
supdf_postfeb20 = supdf[supdf['Pre Feb 2020'] == "N"]

#######POST OPERATIVE STAY ANALYSIS#######
#PostOP Stay Descriptive Stats
print("Pre Feb 2020\n",supdf_prefeb20['Postoperative stay in days'].describe())
print("\n")
print("Post Feb 2020\n",supdf_postfeb20['Postoperative stay in days'].describe())
print("\n")

#PostOP Stay TTest for difference of means
postop_stay_summary = pg.ttest(x=supdf_prefeb20['Postoperative stay in days'], y=supdf_postfeb20['Postoperative stay in days'])
print("There is no statistically signficant difference in the postop stays\n")
postop_stay_summary

#######180 DAY MORTALITY ANALYSIS#######
#180D Mortality Descriptive Stats
print("180 Day Mortality Breakdown")
mortality_crosstab = pd.crosstab(supdf['180D Mortality'], supdf['Pre Feb 2020'])
mortality_crosstab

#180D Mortality Fisher Exact Test for difference in nominal proportions
mortality_oddsratio, mortality_pvalue = stats.fisher_exact(mortality_crosstab)

#######UGIB ANALYSIS#######
#UGIB Descriptive Stats
print("UGIB Breakdown")
ugib_crosstab = pd.crosstab(supdf['UGIB'], supdf['Pre Feb 2020'])
ugib_crosstab

#UGIB Fisher Exact Test for difference in nominal proportions
ugib_oddsratio, ugib_pvalue = stats.fisher_exact(ugib_crosstab)

#######OGD ANALYSIS#######
#OGD Descriptive Stats
print("OGD Breakdown")
ogd_crosstab = pd.crosstab(supdf['OGD'], supdf['Pre Feb 2020'])
ogd_crosstab

#OGD Fisher Exact Test for difference in nominal proportions
ogd_oddsratio, ogd_pvalue = stats.fisher_exact(ogd_crosstab)

#######DEEP STERNAL WOUND INFECTION ANALYSIS#######
#Deep Sternal Wound Infection Descriptive Stats
print("Deep Sternal Wound Infection")
dswi_crosstab = pd.crosstab(supdf['Deep sternal wound infection'], supdf['Pre Feb 2020'])
dswi_crosstab

#DSW Infection Fisher Exact Test for difference in nominal proportions
dswi_oddsratio, dswi_pvalue = stats.fisher_exact(dswi_crosstab)

#Print All Results

print("There is no statistically signficant difference in the postop stays\n")
print(postop_stay_summary)
print('\n')


if mortality_pvalue < 0.05:
  print("The mortality proportions are statistically significantly different with a pvalue of", "%.3f" % mortality_pvalue, "and an odds ratio of", "%.3f" % mortality_oddsratio )
else:
  print("The mortality proportions are NOT statistically significantly different with a pvalue of", "%.3f" % mortality_pvalue, "and an odds ratio of", "%.3f" % mortality_oddsratio )

if ((mortality_pvalue*5 <0.05) and (mortality_pvalue < 0.05)):
  print("The results are still statistically significant after applying a Bonferonni Correction to adjust for the multiple analyses giving a pvalue of", "%.3f" % (mortality_pvalue*5))
else:
  print()
print('\n')

if ugib_pvalue < 0.05:
  print("The UGIB proportions are statistically significantly different with a pvalue of", "%.3f" % ugib_pvalue, "and an odds ratio of", "%.3f" % ugib_oddsratio )
else:
  print("The UGIB proportions are NOT statistically significantly different with a pvalue of", "%.3f" % ugib_pvalue, "and an odds ratio of", "%.3f" % ugib_oddsratio )

if ((ugib_pvalue*5 <0.05) and (ugib_pvalue < 0.05)):
  print("The results are still statistically significant after applying a Bonferonni Correction to adjust for the multiple analyses giving a pvalue of", "%.3f" % (ugib_pvalue*5))
else:
  print()
print('\n')

if ogd_pvalue < 0.05:
  print("The OGD proportions are statistically significantly different with a pvalue of", "%.3f" % ogd_pvalue, "and an odds ratio of", "%.3f" % ogd_oddsratio )
else:
  print("The OGD proportions are NOT statistically significantly different with a pvalue of", "%.3f" % ogd_pvalue, "and an odds ratio of", "%.3f" % ogd_oddsratio )

if ((ogd_pvalue*5 <0.05) and (ogd_pvalue < 0.05)):
  print("The results are still statistically significant after applying a Bonferonni Correction to adjust for the multiple analyses giving a pvalue of", "%.3f" % (ogd_pvalue*5))
else:
  print()
print('\n')

if dswi_pvalue < 0.05:
  print("The Deep Sternal Wound Infection proportions are statistically significantly different with a pvalue of", "%.3f" % dswi_pvalue, "and an odds ratio of", "%.3f" % dswi_oddsratio )
else:
  print("The Deep Sternal Wound Infection proportions are NOT statistically significantly different with a pvalue of", "%.3f" % dswi_pvalue, "and an odds ratio of", "%.3f" % dswi_oddsratio )

if ((dswi_pvalue*5 <0.05) and (dswi_pvalue < 0.05)):
  print("The results are still statistically significant after applying a Bonferonni Correction to adjust for the multiple analyses giving a pvalue of", "%.3f" % (dswi_pvalue*5))
else:
  print()
print('\n')
