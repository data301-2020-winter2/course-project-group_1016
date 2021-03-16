import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    

    #Method Chain 1 (load data, rename columns, drop unneeded columns)
    df1 = (
    pd.read_csv(url_or_path_to_csv_file)
    .rename(columns={"instant":"Instant", "dteday":"Date", "season":"Season", "yr":"Year of Use", "mnth":"Month", "hr":"Hour", "weekday":"Day of Week", "workingday":"Workday?", "holiday":"Holiday?", "casual":"Casual Users", "registered":"Registered User", "cnt":"Total Users", "weathersit":"Weather Situation", "temp":"Temperature", "atemp":"Feeling Temperature", "hum":"Humidity", "windspeed":"Wind Speed"})
    .drop(columns=['Year of Use'])
    )
    return df1