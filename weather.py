import requests
from pprint import pprint
import os
from dateutil.parser import parse
clear = lambda : os.system('cls')

headers = {
  "token" : "kdmXpmwSCrxHVrhYcxIOJTSuVaKLHUzZ" 
}

def get_city_dict(dataset_id):
  limit = 1000
  offset = 1
  data = []
  while True:
    try:
      req = requests.get(f"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?datasetid={dataset_id}&locationcategoryid=CITY&limit={limit}&offset={offset}", headers=headers)
      data.extend(req.json()['results'])
      offset += 1000
    except:
      break
  
  id_dict ={}
  for element in data:
    name = element['name'].split(",")[0]
    id_dict[name.lower()] = element['id']

  return id_dict

def location(dataset_id):
  city_dict = get_city_dict(dataset_id)

  print('Enter City')
  city = input('->').lower()

  for key in city_dict.keys():
    if city in key:
      return city_dict[key]
    
  clear()
  print(f'Either enterd city is wrong or is not awailable in {dataset_id}')
  quit()

def data_limit():
  limit = input("Enter numer of record(s) (1-1000): ")
  if 0 < int(limit) <= 1000:
    return limit
  else:
    print('Enter velid limit')
    quit()

def get_data(dataset_id,startdate,enddate):
  clear()
  print('Getting city Data...')
  city_id = location(dataset_id)
  limit = data_limit()
  
  url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid={dataset_id}&locationid={city_id}&startdate={startdate}&enddate={enddate}&limit={limit}'

  req = requests.get(url, headers=headers)

  pprint(req.json())

def get_dates(dataset):
  maxdate = parse(dataset['maxdate'])
  mindate = parse(dataset['mindate'])

  print('Enter start date (YYYY-MM-DD)')
  startdate = parse(input("->"))
  print('Enter end date (YYYY-MM-DD)')
  enddate = parse(input("->"))

  if startdate <= maxdate and startdate >= mindate:
    if enddate <= maxdate and enddate >= mindate:
      if enddate >= startdate:
        startdate = str(startdate).split(" ")[0]
        enddate = str(enddate).split(" ")[0]
        get_data(dataset['id'],startdate,enddate)
      else:
        print('Invelid End Date')
    else:
      print('Invelid End Date')
  else:
    print('Invelid Start Date')
  

def dataset_desc(id):
  url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?limit=3"
  req = requests.get(url, headers=headers)

  datasets = req.json()['results']
  for dataset in datasets:
    if id == dataset['id']:
      clear()
      print(dataset['name'])
      print('Max possibal date : ' + dataset['maxdate'])
      print('Min possibal date : ' + dataset['mindate'])
      get_dates(dataset)

def datasets():
  print("Choose : ")
  print("\t1.Daily Summaries")
  print("\t2.Global Summary of the Month")
  print("\t3.Global Summary of the Year")
  print()
  choice = input("->")
  if choice in ["1","2","3"]:
    if choice == '1':
      dataset_desc('GHCND')
    elif choice == '2':
      dataset_desc('GSOM')
    else:
      dataset_desc('GSOV')
  
datasets()
