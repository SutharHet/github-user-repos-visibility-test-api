import requests
from pprint import pprint
import os
from dateutil.parser import parse

clear = lambda : os.system('cls')

headers = {
  "token" : "kdmXpmwSCrxHVrhYcxIOJTSuVaKLHUzZ" 
}

class weather:
  def __init__(self):
    self.datasets = {}
    self.startdate = ''
    self.enddate = ''
    self.limit = 25
    self.city_id = ''
    self.datatypes = {}
    self.weather_data = {}
    self.sort_field = ''
    self.sort_order = 'asc'

  def dataset(self, dataset_id):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets"
    req = requests.get(url, headers=headers)

    datasets = req.json()['results']
    for dataset in datasets:
      if dataset_id == dataset['id']:
        self.datasets = dataset

  def dates(self, startdate, enddate):
    if self.datasets:
      maxdate = parse(self.datasets['maxdate'])
      mindate = parse(self.datasets['mindate'])

      startdate = parse(startdate)
      enddate = parse(enddate)

      if startdate <= maxdate and startdate >= mindate:
        if enddate <= maxdate and enddate >= mindate:
          if enddate >= startdate:
            self.startdate = str(startdate).split(" ")[0]
            self.enddate = str(enddate).split(" ")[0]
          else:
            print('Invelid End Date : Enddate smaller then startdate')
            quit()
        else:
          print('Invelid End Date : Enddate is out of range of dataset')
          quit()
      else:
        print('Invelid Start Date : Startdate is out of range of dataset')
        quit()
    
  def record_limit(self, limit):
    try:
      if 0 < int(limit) <= 1000:
        self.limit = limit
      else:
        print('Enter velid limit')
        quit()
    except:
      print('Entered limit is not a number')

  def sort_in_order(self, order):
    if order.lower() in ["asc","desc"]:
      self.sort_order = order.lower()
    else:
      print("Invelid order of sorting valid parameters are 'asc' or 'desc'")

  def sort_by(self, field):
    if field.lower() in ["id", "name", "mindate", "maxdate","datacoverage"]:
      self.sort_field = field.lower()
    else:
      print("Invelid field for sorting")

  def get_city_dict(self):
    limit = 1000
    offset = 1
    cities = []
    dataset_id = self.datasets['id']
    while True:
      try:
        req = requests.get(f"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?datasetid={dataset_id}&locationcategoryid=CITY&limit={limit}&offset={offset}", headers=headers)
        cities.extend(req.json()['results'])
        offset += 1000
      except:
        break
    
    city_ids = {}
    for city in cities:
      name = city['name'].split(",")[0].lower()
      city_ids[name] = city['id']
      
    return city_ids

  def location(self,city_name):
    city_ids = self.get_city_dict()
    for key in city_ids.keys():
      if city_name.lower() == key:
        self.city_id = city_ids[key]
        return

    print(f'Either enterd city is wrong or is not awailable in selected dataset')
    quit()

  def datatype(self,datatype_id):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes"
    req = requests.get(url, headers=headers)

    limit = 1000
    offset = 1
    datatypes = []
    while True:
      try:
        req = requests.get(f"https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?&limit={limit}&offset={offset}", headers=headers)
        datatypes.extend(req.json()['results'])
        offset += 1000
      except:
        break
      
    for datatype in datatypes:
      if datatype_id == datatype['id']:
        self.datatypes = datatype

  def get_data(self):
    if self.datasets['id'] and self.startdate and self.enddate:
      
      dataset_id = self.datasets['id']
      url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid={dataset_id}&startdate={self.startdate}&enddate={self.enddate}&units=metric&limit={self.limit}'
      
      if self.datatypes and self.datatypes['id']:
          datatype_id = self.datatypes['id']
          url += f'&datatypeid={datatype_id}'
      if self.city_id:
        url += f'&locationid={self.city_id}'
      if self.sort_field:
        url += f'&sortfield={self.sort_field}'
      if self.sort_order:
        url += f'&sortorder={self.sort_order}'
      # if self.station_id:
      #   url += f'&locationid={self.station_id}'
      
      try:
        req = requests.get(url, headers=headers)
        self.weather_data = req.json()['results']
      except:
        print('Error while fetching data')
        quit()
      

  def display(self):
    if self.weather_data:
      for record in self.weather_data:
        print('On Date : ' + record['date'].split('T')[0])
        print('Station Id : ' + record['station'])
        print('Type of data : ' + record['datatype'])
        print('Value : ' + str(record['value']))
        print()



weather_obj = weather()

weather_obj.dataset('GHCND')
weather_obj.dates('2022-1-23','2022-1-31')
weather_obj.record_limit(5)
# weather_obj.datatype('TAVG')
# weather_obj.location('delhi')
# weather_obj.sort_by('value')
weather_obj.sort_in_order('desc')

weather_obj.get_data()

weather_obj.display()
