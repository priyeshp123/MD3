import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error

def extract_statements(stype,master_company_data):
    
  master = pd.DataFrame()

  for ticker in master_company_data:
    print(ticker)
    df = master_company_data[ticker][stype].T.copy()
    df['company'] = ticker
    df['industry'] = master_company_data[ticker]['industry']
    df['yahoo_sector'] = master_company_data[ticker]['yahoo_sector']
    df['gics_sector'] = master_company_data[ticker]['gics_sector']
    
    df = df.reset_index(names='st_date')
    df['st_YR'] = df['st_date'].apply(lambda x: x.split("-")[0])
    df['st_Mnth'] = df['st_date'].apply(lambda x: x.split("-")[1])

    # Taking a copy to avoid warning messages about fragmented dataframe before appending to balance_sheets
    
    X = df.copy()
    
    master = pd.concat([master,X],axis=0)
    
  master.reset_index(drop=True,inplace=True)

  return master

def remove_non_annual_data(df):
    
  df_new = pd.DataFrame()

  ticker_list = list(df['company'].unique())

  for ticker in ticker_list:
    print(ticker)
    df_company = df[df['company'] == ticker].copy()

    # Extract month and store as separate column
    
    df_company['M'] = df_company['st_date'].apply(lambda x: x.split("-")[1])
    
    # Determine the most common month for annual report for the company. Consider reports for any other month 
    # as spurious and can be deleted.
    
    mode_M = df_company['M'].mode()[0]
    df_company.drop(df_company[df_company['M'] != mode_M].index, axis=0, inplace=True)
    
    df_new = pd.concat([df_new,df_company],axis=0)
    
def chk_trend(S):
  
  S = pd.DataFrame(S)

  trend_details={}

  scaler = preprocessing.MinMaxScaler()
  scaler = scaler.fit_transform(S)* 10
  x=[1,2,3,4]

  y=[]

  for i in range(0,len(scaler)):
    y = y + list(scaler[i])

  coeff=np.polyfit(x,y,deg=1)
  f = np.poly1d(coeff)

    
  trend_details['gradient'] = coeff[0]
  trend_details['x_val'] = x
  trend_details['y_val'] = y
    
  return trend_details

  return df_new

def getTrendScore(S):

   trend_details = chk_trend(S)

   return round(trend_details['gradient'])

def show_trend(trend_details,deg=1):
 
  x = trend_details['x_val']
  y = trend_details['y_val']
  print(x)
  print(y)

  xx=np.linspace(0,5,100)

  # Linear

  deg = 1

  coeff=np.polyfit(x,y,deg)
  f = np.poly1d(coeff)
  y1 = f(x)
  y1_line=f(xx)

  y1_error = mean_squared_error(y,y1)   
  print("y1_error: %.2f" % y1_error)

  # Polynominal 1

  deg = 2
  coeff=np.polyfit(x,y,deg)
  f = np.poly1d(coeff)
  y2 = f(x)
  y2_line=f(xx)

  y2_error = mean_squared_error(y,y2)   
  print("y2_error: %.2f" % y2_error)
    
  # Polynomial 2

  deg = 3
    
  coeff=np.polyfit(x,y,deg)
  f = np.poly1d(coeff)
  y3 = f(x)
  y3_line=f(xx)

  # Polynomial 2

  deg = 3
    
  coeff=np.polyfit(x,y,deg)
  f = np.poly1d(coeff)
  y3 = f(x)
  y3_line=f(xx)

  y3_error = mean_squared_error(y,y3)   
  print("y3_error: %.2f" % y3_error)
  print(" ")

  plt.plot(xx,y1_line, c='red')
  plt.plot(xx,y2_line, c='green')
  plt.plot(xx,y3_line, c='red')
    
  plt.scatter(x,y,c="black")

  plt.show()

