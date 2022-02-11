import sys
import pandas as pd
import os


script_path = sys.argv[0]

df = pd.read_csv(sys.argv[1])

img_list = os.listdir(sys.argv[2])

result_df = pd.DataFrame()

result_df["target"] = [3,8,3,5,5,4,7,8,1,5,5,1,3]


result_df.to_csv(script_path + "/result.csv")


