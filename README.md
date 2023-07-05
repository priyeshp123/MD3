Project: Download data from Yahoo Finance 

1. Download data from Yahoo : Stage1_Yahoo_Download_data.ipynb

   Download is prone to failure so download as 4 groups organised by 
   sector. Combine data in next step. 

   Resolve ticker format anomalies, exclude problem companies that fail to
   download and eliminate duplicates.

   List of tickers is taken from Russell 1000 companies listed on wikipedia:

   https://en.wikipedia.org/wiki/Russell_1000_Index

2. Extract Data : Stage2_Yahoo_Extract_Data.ipynb

   Combine data downloaded in groups in step 1 into a single dictionnary keyed
   on ticker symbol.

   Assign sector and industry for each company.

   Save data as pickle file. 

3. Extract Balance Sheet : Stage3_Yahoo_Extract_Balance_Sheet.ipynb

   Create data frame with balance sheet data for all companies.

   Organise columns into:

	summary, current assets, non-current assets, current_liabilites,
        non_current_liabilties, stockhoolder_equity

   Identify and remove companies with less than 4 years of data.

   Resolve issues with spurious data including TTM and other quarterly data
   included for reasons unknown.

   Check counts for null values, determine candidates for selection in data
   set. Investigate and resolve anomalies (eg. same information held in 
   different fields for different companies).

   Resolve nulls by deriving values  from other fields where possible,

   Set fields to 0 if null where it is a reasonable assumption that absence
   infers 0.

   Eliminate problem companies, industries and sectors. Keep record of removals.

   Identify and remove duplicate companies.

   Build final cut for balance sheets. Save as pickle file.
 


