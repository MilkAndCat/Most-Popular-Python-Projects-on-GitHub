import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Total Repositoriess: ", r.status_code)

response_dict=r.json()

print("total Repositories:",response_dict['total_count'])

items_dicts=response_dict['items']

print("Repositories items returned :",len(items_dicts))

'''single_item=items_dicts[0]

print("Keys store in a single Repositories: ",len(single_item))

for i, key in enumerate(sorted(single_item.keys())):
	print(i,key)'''
'''
for item in items_dicts:
	print('\nName:',item['name'])
	print('Owner:',item['owner']['login'])
	print('Stars:',item['stargazers_count'])
	print('repository url:',item['html_url'])
	print('Project Description:',item['description'])
'''

names,stars=[],[]

for item in items_dicts:
	names.append(item['name'])
	stars.append(item['stargazers_count'])

my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title="Most Popular Python Project on GitHub"
chart.x_labels=names

chart.add('',stars)
chart.render_to_file('Most_Starred_Python_on_GitHub.svg')