#import requests
import pandas as pd

#content = requests.get("https://pythonhow.com/media/data/sampledata.txt")
content = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
content_2 = content * 2
content_2.to_csv("files/exercise073_x_2.txt", index=None)