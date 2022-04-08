

# all the imports 
import requests
import os 
import shutil
import json 
from datetime import date
import pandas as pd

def get_request(url):

  r = requests.get(url)
  json_file = r.json()

  return json_file


def save_file (data, folder_name, file_name):
  '''
  input: data, a dict; folder_name, a string; file_name, a string
  output: none
  purpose: creates a folder that stores all the data in an organized way 
  '''
  
  current = os.getcwd()

  #check to see if file already exists 
  try:
    filename = (f"{file_name}.json")
    f = open(filename, "x")
    with open(filename, 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

    #write data! to file
  except:
    os.remove(f"{file_name}.json")
    filename = (f"{file_name}.json")
    f = open(filename, "x")
    with open(filename, 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
  
  #create folder 
  try:
    path = f"{current}/{folder_name}"
    os.makedirs(path)
  except:
    pass

    
  #save it 

  src = current
  dst = f"{current}/{folder_name}"

  og = os.path.join(src, filename)
  target = os.path.join(dst, filename)

  shutil.move(og, target)



NO = "https://aqs.epa.gov/data/api/sampleData/byCounty?email=vsachdev@g.hmc.edu&key=ecrukit34&param=42601&bdate=20160101&edate=20160228&state=06&county=037"
NO2 =  "https://aqs.epa.gov/data/api/sampleData/byCounty?email=vsachdev@g.hmc.edu&key=ecrukit34&param=42602&bdate=20160101&edate=20160228&state=06&county=037"
NOX = "https://aqs.epa.gov/data/api/sampleData/byCounty?email=vsachdev@g.hmc.edu&key=ecrukit34&param=42603&bdate=20160101&edate=20160228&state=06&county=037"
O3 = "https://aqs.epa.gov/data/api/sampleData/byCounty?email=vsachdev@g.hmc.edu&key=ecrukit34&param=44201&bdate=20160101&edate=20160228&state=06&county=037"
# PM = https://aqs.epa.gov/data/api/sampleData/byCounty?email=vsachdev@g.hmc.edu&key=ecrukit34&param=81101&bdate=20160101&edate=20160228&state=06&county=037"

list_of_vocs = [("NO",NO),("NO2",NO2), ("NOX", NOX), ("O3" ,O3)]

folder_name = "CA_LA_NORTH"
for t in list_of_vocs:
  r = requests.get(t[-1])
  data = r.json()['Data']

  save_file (data, folder_name, t[0])







