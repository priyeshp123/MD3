import pandas as pd

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

  return df_new
