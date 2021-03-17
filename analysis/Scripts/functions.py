import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    
#Method Chain 1 (load data, rename columns, drop unneeded columns)
    df1 = (
    pd.read_csv(url_or_path_to_csv_file)
    .rename(columns={"instant":"Instant", "dteday":"Date", "season":"Season", "mnth":"Month", "hr":"Hour", "weekday":"Day of Week", "workingday":"Workday?", "holiday":"Holiday?", "casual":"Casual Users", "registered":"Registered User", "cnt":"Total Users", "weathersit":"Weather Situation", "temp":"Temperature", "atemp":"Feeling Temperature", "hum":"Humidity", "windspeed":"Wind Speed"})
    .drop(columns=['Humidity'])   
    )
 

    #Method Chain 2 (Editing columns to be more descriptive)
    df2 = (
    df1      
    .assign(Casual_Ratio = df1['Casual Users'] / df1['Total Users'])
    .assign(Average_temperature= (df1['Feeling Temperature'] +  df1['Temperature']) / 2)       
    )
    df2['Month'] = df1['Month'].replace([1,2,3,4,5,6,7,8,9,10,11,12], ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    df2['Holiday?'] = df1['Holiday?'].replace([0,1], [False, True])                                                   
    df2['Workday?'] = df1['Workday?'].replace([0,1], [False, True])
    df2['Day of Week'] = df1['Day of Week'].replace([1,2,3,4,5,6,0], ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    df2['Weather Situation'] = df1['Weather Situation'].replace([1,2,3,4], ['Sunny','Cloudy','Light Precipitation','Heavy Precipitation'])
    df2['Season'] = df1['Season'].replace([1,2,3,4], ['Winter','Spring','Summer','Fall'])
    df2["Temperature"] = 41 * df1["Temperature"]
    df2["Feeling Temperature"] = 50 * df1["Feeling Temperature"]
    df2["Wind Speed"] = 67 * df1["Wind Speed"]
    return df2