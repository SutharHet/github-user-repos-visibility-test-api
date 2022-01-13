import requests
from pprint import pprint

def display(repos_data):
  for item in repos_data:
    pprint(item[0] + ' : ' + item[1] + ' : ' + item[2])

def get_repos_data(user_repos):
  repos_data = []
  for repos in user_repos:
    repos_data.append([repos['name'],repos['visibility'],str(repos['stargazers_count']) + ' stars'])
  display(repos_data)

def list_repos(user_name):
  user_repos_req = requests.get('https://api.github.com/users/{}/repos'.format(user_name))
  user_repos = []
  if len(user_repos_req.json()) == 0:
    print('User {} has no repositories.')
    quit()
  get_repos_data(user_repos_req.json())

def user_follow(user_dict):
  following_count = user_dict['following']
  follower_count = user_dict['followers']
  print('following : ' + str(following_count))
  print('followers : ' + str(follower_count))

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
      user_follow(user_req.json())
      list_repos(user_name)
      break

get_user()
