import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    df1 = (
        #Rename and sort by Episode date, reported date, and then age group.
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"Client Gender" : "Sex"})
        .sort_values(['Episode Date','Reported Date',"Age Group"], ascending = [1,1,1])
    )

    df2 = (
        #Drop NA, _id, and rows that do not have confirmed as a case
        df1
        .dropna()
        .drop('_id', axis = 1)
        .loc[df1["Classification"].str.contains("CONFIRMED")]
        .drop('Classification', axis = 1) #We don't need this column anymore, since we are working soley with confirmed cases.
        .reset_index(drop = True)   
    )
    
    return df2

def simplify(df):
    df = df.drop(['Outbreak Associated', 'Neighbourhood Name', 'FSA', 'Outcome' , 'Currently Hospitalized', 'Currently in ICU', 'Currently Intubated' ],axis = 1)
    df.columns = ['Age_Group', 'Source_of_Infection', 'Episode_Date' , 'Reported_Date' , 'Gender', 'Outcome' , 'Ever_Hospitalized', 'Ever_in_ICU']
    return df


