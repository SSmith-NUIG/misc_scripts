import pandas as pd
import numpy as np
import sys

#setting up test dataframe (only run this once)
#df = pd.DataFrame({"number":[1,2,3,4,5,6], "conc":[35,54,29,33,43,35], "volume":[35,35,35,35,35,35]})
#df.to_csv("colony_test.csv", index=False)
#df

def  how_much_to_take(dataframe):
    #set up the dataframes columns
    dataframe["total_dna"] = dataframe.apply(lambda row: row.conc*row.volume, axis=1)    
    dataframe["one_over_conc"] = dataframe["conc"].apply( lambda x: 1/x)
    dataframe["take"] = np.nan
    dataframe["group"] = np.nan
    
    group = 1
    
    #this loop will be edited based on how many samples there will be in each group ( possibly 5 or 6, this is TBD)
    for i in range(0, len(dataframe["number"])):

        if i%3==0:
            dataframe["group"][i] = group
            dataframe["group"][i+1] = group
            dataframe["group"][i+2] = group

            group +=1
    
    #the 35 here is the volume of final DNA tube, this may change and might be edited to a sys.argv variable
    for m in range(1, dataframe["group"].nunique()+1):
        dataframe["take"] = dataframe["one_over_conc"] * (35 / sum(dataframe.loc[dataframe['group'] == m]["one_over_conc"]))
                
    print(dataframe)

df = pd.read_csv(sys.argv[1])

how_much_to_take(df)
