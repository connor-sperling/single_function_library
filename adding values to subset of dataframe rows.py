import os
import pandas as pd
import numpy as np

path = 'C:\\Users\\csperling\\OneDrive - MaxLinear, Inc\\Documents\\projects\\keystone\\testing\\DVT\\OTX\\HV\\eye_performance\\211209_PN78_new_HV_driver_config'
fn = 'PN-78_HV_OTX_mode11_DVT_eye_performance_2021-12-10_08-17-35.csv'
fi = 'C:\\Users\\csperling\\Downloads\\forwork.csv'

di = pd.read_csv(fi)
d  = pd.read_csv(os.path.join(path, fn))

d.loc[d.Source == 'Trace', 'RLM']= di.RLM.tolist()

d.to_csv(os.path.join(path, 'new_{}'.format(fn)))