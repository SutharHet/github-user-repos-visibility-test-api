import requests
from pprint import pprint

def display(repos_visbility):
  for item in repos_visbility:
    pprint(item[0] + ' : ' + item[1])

def view_repos_visibility(user_repos):
  repos_visibility = []
  for repos in user_repos:
    repos_visibility.append([repos['name'],repos['visibility']])
  display(repos_visibility)

def list_repos(user_name):
  user_repos_req = requests.get('https://api.github.com/users/{}/repos'.format(user_name))
  user_repos = []
  if len(user_repos_req.json()) == 0:
    print('User {} has no repositories.')
    quit()
  for item in user_repos_req.json():
    user_repos.append(item)
  view_repos_visibility(user_repos)

def get_user():
  while True:
    print('Enter GitHub UserName whos repository visibility you want to see.')
    user_name = input('User Name : ')
    print()
    user_req = requests.get('https://api.github.com/users/' + user_name) # 'message': 'Not Found'
    user_dict = dict(user_req.json())
    if 'message' in user_dict.keys():
      print('This UserName Does not exist.')
      continue
    else:
      list_repos(user_name)
      break

get_user()