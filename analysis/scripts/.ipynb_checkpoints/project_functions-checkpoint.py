import pandas as pd
import numpy as np
import os

def load_and_process(curr_dir):
    path = autopath(curr_dir)
    df1 = (
        #Rename and sort by Episode date, reported date, and then age group.
        pd.read_csv(path)
        .rename(columns={"Client Gender" : "Gender"})
        
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

def load_and_process_direct_path(curr_dir): #our tableau format breaks if we use the updated method. 
    df1 = (
        #Rename and sort by Episode date, reported date, and then age group.
        pd.read_csv(curr_dir)
        .rename(columns={"Client Gender" : "Gender"})
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

def autopath(curr_dir):
    path = (os.getcwd()
        .replace(curr_dir,"")
    )
    path = path+"\\data\\raw\\COVID19 cases Toronto.csv"
    return path
        
def simplify(df): #don't run this if your going to run date and time.
    df = df.drop(['Outbreak Associated', 'Neighbourhood Name', 'FSA', 'Outcome' , 'Currently Hospitalized', 'Currently in ICU', 'Currently Intubated' ],axis = 1)
    df.columns = ['Age_Group', 'Source_of_Infection', 'Episode_Date' , 'Reported_Date' , 'Gender', 'Outcome' , 'Ever_Hospitalized', 'Ever_in_ICU']
    df["Age_Group"] = df["Age_Group"].replace('19 and younger', "<19") 
    return df

def add_date_time(df):
    df = simplify(df)
    df['Dt_Format'] = pd.to_datetime(df.Reported_Date)
    df['Dt_Format'] = df.Dt_Format.dt.date
    df['Days_Since'] = (df['Dt_Format'][0:] - min(df['Dt_Format'])) 
    df['Days_Since'] = df['Days_Since'].dt.days
    df = df.drop(["Dt_Format"],axis = 1)
    return df

def add_date_time_no_format(df):
    df = df.rename(columns={"Reported Date" : "Reported_Date"})
    df['Dt_Format'] = pd.to_datetime(df.Reported_Date)
    df['Dt_Format'] = df.Dt_Format.dt.date
    df['Days Since'] = (df['Dt_Format'][0:] - min(df['Dt_Format'])) 
    df['Days Since'] = df['Days Since'].dt.days
    df = df.drop(["Dt_Format"],axis = 1)
    df = df.rename(columns={"Reported_Date" : "Reported Date"})
    return df

def format_tableau_save_csv(url_or_path_to_csv_file,dest):
    df = add_date_time_no_format(load_and_process_direct_path(url_or_path_to_csv_file))
    df.to_csv(dest, index = False )

def ez_format(path): #To groupmates.... Just use this. Nothing breaks if you use this. 
    return add_date_time(load_and_process(path))

#def location(df): #convert districts to longitude/latitude (WIP)