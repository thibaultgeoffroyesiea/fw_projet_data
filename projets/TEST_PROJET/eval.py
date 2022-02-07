import sys
import pandas as pd
import os


df = pd.read_csv(sys.argv[1])


result_df = pd.DataFrame()

result_df["prediction"] = [1,2,3,4,5]


result_df.to_csv(sys.argv[0] + "result.csv")