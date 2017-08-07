import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Total Repositoriess: ", r.status_code)

response_dict = r.json()

print("total Repositories:", response_dict['total_count'])

items_dicts = response_dict['items']

print("Repositories items returned :", len(items_dicts))

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

names = []
stars = []
multi_Description = []

for item in items_dicts:
    names.append(item['name'])
    single_Description = {
        'value': item['stargazers_count'],
        'xlink': item['html_url'],
        'label' : str(item['description'])

    }
    multi_Description.append(single_Description)





my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most Popular Python Project on GitHub"
chart.x_labels = names
chart.add('',multi_Description)
chart.render_to_file('Most_Starred_Python_on_GitHub.svg')
