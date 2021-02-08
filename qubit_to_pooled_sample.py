"""
Created on Wed Sep 23 10:05:42 2020
@author: stephen
"""

import pandas as pd
import argparse
import textwrap
import numpy as np

parser = argparse.ArgumentParser(description='pool_dna_script')

parser.add_argument('-file', metavar='-f', nargs='+', default="",
                    help= textwrap.dedent('''\
                                          path to csv qubit file'''))

parser.add_argument('-volume', metavar='-v', nargs='+', default="35",
                    help= textwrap.dedent('''\
                                          Enter the volume (microL) of the sample, defualt is 35'''))

parser.add_argument('-poolsize', metavar='-s', nargs='+', default="6",
                    help= textwrap.dedent('''\
                                          Enter the number of samples you are pooling together, default is 6'''))

parser.add_argument('-outfile', metavar='-o', nargs='+', default="colony_pool_output.csv",
                    help= textwrap.dedent('''\
                                          Enter a filename to write results to, default is colony_pool_output.csv'''))

options = parser.parse_args()

def  how_much_to_take(dataframe):
    
    dataframe.rename(columns={"Original sample conc.":"Concentration (ng/microL)"}, inplace=True)
    dataframe["Volume (microL)"] = float(options.volume[0])
    dataframe["Total DNA (ng)"] = dataframe["Concentration (ng/microL)"] * dataframe["Volume (microL)"] 
    dataframe["Inverse Concentration"] = 1/dataframe["Concentration (ng/microL)"]
    dataframe["Pool Number"] = np.nan
    dataframe["Volume of sample in pool (microL)"] = np.nan
    dataframe["DNA Contributed (ng)"]= np.nan
    
    #The first row of the Qubit output csv file is the last sample that
    #was analysed, this is counter intuitive to analysis as you would
    #expect the first row to be the first sample analysed so the next line
    #reverses the order of the rows in the Qubit output csv.
    dataframe = dataframe.iloc[::-1].reset_index(drop=True)
    
    #make sure that pool_size input is a integer
    #and the volume input is a float (e.g could have 35.5microL )
    pool_size = int(options.poolsize[0])
    vol = float(options.volume[0])
    
    #split the dataframe by the size of your pools
    #e.g if Pool size is 6 and the dataframe has 12 Qubit entries
    #this command will get the first entry of both pools and save them to a dataframe
    pool_starts = dataframe[::pool_size]
    pool_starts = pool_starts.copy()
    
    #assign values to each first entry of the pools starting from 1 to the length of 
    #the number of pools in pool_starts
    #e.g is there are two pools then they will get numbers 1 and 2
    pool_starts["Pool Number"] = [i for i in range(1,len(pool_starts)+1)]
    
    #updates the dataframe[Pool] values using the pool_starts[Pool] dataframe
    dataframe["Pool Number"] = pool_starts["Pool Number"]
    
    #forward fill the rest of the dataframe[Pool] column.
    #this will fill the NaNs from one Pool number to the next using the value
    #given to the group in pool_starts["Pool Number"] = [i for i in range(1,len(pool_starts)+1)]
    dataframe["Pool Number"].ffill(inplace=True)

    #multiply the values in the inverse_conc column with the desired Pooled sample volume
    #divided by the sum of the inverse concentration of that Pool to get how much
    #volume of each sample you will contribute to the Pooled sample
    dataframe["Volume in pool (microL)"] = dataframe["Inverse Concentration"] * vol/dataframe.groupby("Pool Number")["Inverse Concentration"].transform("sum")
    
    #calculate how much dna each sample is contributing to each Pool
    #each value should be idential within pools
    dataframe["DNA Contributed (ng)"] = dataframe["Volume in pool (microL)"] * dataframe["Concentration (ng/microL)"]

    #python indexes start at 0 which will not match the samples run
    #this line reindexes the dataframe so that it starts at 1 for readability
    dataframe.index= np.arange(1,(len(dataframe)+1))
    dataframe["Sample Number"] = dataframe.index

    headers= ["Pool Number","Volume (microL)","Concentration (ng/microL)","TotalDNA (ng)","Inverse Concentration","Sample Number","Volume in pool (microL)","DNA Contributed (ng)"]

    print(dataframe[headers])
    print("Saving output to file: %s" % options.outfile[0])
    with open(options.outfile[0], 'w') as output_file:
        dataframe.to_csv(output_file, columns= headers, sep=',', encoding='utf-8', index=False)

df = pd.read_csv(options.file[0])
how_much_to_take(df)

