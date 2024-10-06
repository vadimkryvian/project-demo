import mlrun
import pandas as pd
import numpy as np

from time import sleep

def func(context):
    df = pd.DataFrame({'col1': np.random.rand(100)})
    sleep(60)
    print(df)
    return df