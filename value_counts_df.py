
import pandas as pd
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt                         
import seaborn as sns   


def vcdf(original_dataframe):
    
    '''This function outputs a dataframe with 
    counts of the unique values for each  column
    from the input dataframe (function argument). 
    The counts are given for each column of the 
    input dataframe - in the output a column with
    unique values is paired with another column
    with the counts for the unique values'''

    df_dict = dict()

    for i in original_dataframe.columns:
        # value count series absolute
        series_value_counts = original_dataframe[i].value_counts(dropna = False)
        # value count series relative
        series_value_counts_percent = original_dataframe[i].value_counts(dropna = False, normalize = True)
        # dict key names:
        dict_value_key = series_value_counts.name+"_value"
        dict_count_key = series_value_counts.name+"_count_abs"
        dict_count_key_percent = series_value_counts.name+"_count_percent"
        # dict key values:
        df_dict[dict_value_key] = list(series_value_counts.index)
        df_dict[dict_count_key] = list(series_value_counts.values)
        df_dict[dict_count_key_percent] = list(100*series_value_counts_percent.values)

    return pd.DataFrame(OrderedDict([(key,pd.Series(values)) for key,values in df_dict.items()]))

# Example:
dftest = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
test_vcdf = vcdf(dftest)
writer = pd.ExcelWriter('test_file.xlsx')
test_vcdf.to_excel(writer,'nice test')
writer.save()

