from dopy.manager import DoManager
from os import environ
do = DoManager(None, environ["DO_API_TOKEN"], api_version=2)
a=[]
# only specific size
#for d in do.all_active_droplets():
#    if d['size_slug'] == '1gb':
#        do.destroy_droplet(d['id'])
for d in do.all_active_droplets():
    do.destroy_droplet(d['id'])
