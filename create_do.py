from dopy.manager import DoManager
from os import environ
do = DoManager(None, environ["DO_API_TOKEN"], api_version=2)
from pprint import PrettyPrinter as pp
p=pp().pprint

image = 'ubuntu-16-04-x64'
region = 'sfo2'
size = '512mb'
user_data = '''#cloud-config
chpasswd:
  list: |
    root:changemenow'''

admins = ['fletch',
          'ali',
          'yingchao',
          'yingbo',
          'adnan',
          'mark',
          'vang',
          'spare']
for name in admins:
    do.new_droplet(name, size, image, region, user_data=user_data)

# my sluuuuugs
# >>> pr([i['slug'] for i in do.all_images() if i['slug'] and '16-04' in i['slug'] and 'buntu' in i['slug'] and 'sfo2' in i['regions'] ])
# [u'ubuntu-16-04-x32', u'ubuntu-16-04-x64']

# do.all_regions, sfo2 data
#{u'available': True,
#   u'features': [u'private_networking',
#                                 u'backups',
#                                 u'ipv6',
#                                 u'metadata',
#                                 u'install_agent',
#                                 u'storage'],
#   u'name': u'San Francisco 2',
#   u'sizes': [u'512mb',
#                           u'1gb',
#                           u'2gb',
#                           u'4gb',
#                           u'8gb',
#                           u'16gb',
#                           u'm-16gb',
#                           u'32gb',
#                           u'm-32gb',
#                           u'48gb',
#                           u'm-64gb',
#                           u'64gb',
#                           u'm-128gb',
#                           u'm-224gb'],
#   u'slug': u'sfo2'}]

