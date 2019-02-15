#module load_gas_asset_data.py
import pandas as pd

'''all gas asset sub-projects come 
from this original data so we use 
this to load the data everytime we 
work with this project'''

# Absolute path for the dataset:
gas_asset_path = "Gas_Asset_Data_Cleaned.csv"

col_names_common = [
    'OP_CENTER',
    'DIVISION',
    'SUBSIDIARY',
    'CLASS',
    'MATERIAL',
    'DIAMETER',
    'DECADE',
    'ALDYL_A',
    'BUSINESS_DISTRICT',
    'RISK_AREA_FT',
]

# List of columns selected for each gas model:
col_names_ed = [
    'DLS_SMR',
    'DLM_SMR',
    'WATCH_PROTECT',
    'POP_DENSITY',
    'CRITICAL_AREA',
    'LEAKS_PER_LOCATE'
]

col_names_ef = [
    'MFS_SMR',
    'MFM_SMR',
    'AFI',
    'SEISMIC_ACCEL',
    'SINK_HOLE',
    'COAL_MINE',
    'OPEN_LEAKS',
    'INDOOR_METER'
]

col_names_mf = [
    'MFS_SMR',
    'MFM_SMR',
    'AFI',
    'SEISMIC_ACCEL',
    'SINK_HOLE',
    'COAL_MINE',
    'OPEN_LEAKS',
    'INDOOR_METER'
]

col_names_cor = [
    'CP_SYSTEM_NUM',
    'AFI',
    'SEISMIC_ACCEL',
    'SINK_HOLE',
    'COAL_MINE',
    'OPEN_LEAKS',
    'INDOOR_METER',
    'CP_DAYS_DEFICIENT',
    'NUM_CP_READS'
]

col_names_io    = [
    'WATCH_PROTECT',
    'POP_DENSITY',
    'OPEN_LEAKS',
    'INDOOR_METER'
]

col_names_nf = [
    'WATCH_PROTECT',
    'AFI',
    'SEISMIC_ACCEL',
    'SINK_HOLE',
    'COAL_MINE',
    'POP_DENSITY',
    'OPEN_LEAKS',
    'INDOOR_METER'
]

col_names_of = [
    'WATCH_PROTECT',
    'AFI',
    'SEISMIC_ACCEL',
    'SINK_HOLE',
    'COAL_MINE',
    'POP_DENSITY',
    'OPEN_LEAKS',
    'INDOOR_METER'
]

col_names_oth = [
    'WATCH_PROTECT',
    'AFI',
    'SEISMIC_ACCEL',
    'SINK_HOLE',
    'COAL_MINE',
    'POP_DENSITY',
    'OPEN_LEAKS',
    'INDOOR_METER'
]


#TO BE IMPLEMENTED: INCLUDING TOWN_GAS_NAME, SYSTEM_NUM, DETAIL_F


projects = {'ed': col_names_ed, 
            'ef': col_names_ef,
            'mf': col_names_mf,
            'cor': col_names_cor,
            'io': col_names_io,
            'nf': col_names_nf,
            'of': col_names_of,
            'oth': col_names_oth}

# ed    =   Excation Damage
# ef    =   equipment failure
# mf    =   material failure
# cor   =   corrosion
# io    =   incorrect operation
# nf    =   natural forces
# of    =   outside force
# oth   =   other causes for leaks (no reported?)


#Use TOTAL_(project_key)_LEAKS as the target variable by default
def load_data(pathway = gas_asset_path, project_key = 'ed', target = 0):

    '''This function loads the dataset
    provided by Edwin in csv format
    and creates a dataframe using pandas.
    It takes two input: (1) the location
    of the file, and (2) the columns selected
    per type of propject, the default is ed,
    which stands for excavation damage columns.
    Because the format has no conflicts,
    the file can be loaded directly, if it had
    format conflicts like no UTF-8 compliant
    we would need to add this to the read_csv
    function as this is not uncommon 
    for other projects'''

    # Set target variable
    if target == 0:
        target = "TOTAL_" + project_key.upper() + "_LEAKS"
    # Make a pandas data frame from raw data:
    frame = pd.read_csv(gas_asset_path, index_col='RISK_AREA')
    # Use only columns per type of project:
    df_features = pd.get_dummies(frame[projects[project_key] + col_names_common])
    
    frame.loc[frame[target] > 0, target] = 1
    df_target = frame[target]
     
    return df_features, df_target

if __name__ == "__main__":
    load_data()
