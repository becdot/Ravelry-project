import urllib2, json
import requests

#f = urllib2.urlopen('http://api.ravelry.com/projects/becdot/progress.json?key=30820525c938d7eab6c933ce8dbe9c3ff1ee57b8&status=in-progress+hibernating+finished+frogged&notes=true')
#rawdata = json.load(f)
#
#user_details = {}
#for k, v in rawdata['user'].iteritems():
#    user_details[k] = v
#for k, v in user_details.iteritems(): print k, ':', v
#
#project_details = {}
#for project in rawdata['projects']:
#    for k, v in project.iteritems():
#        project_details[project['name']] = project       
#for k, v in project_details.iteritems(): print k, ':', v, '\n'

login_url = 'https://www.ravelry.com/account/login'
yarn_url = 'http://www.ravelry.com/yarns/library/brown-sheep-lambs-pride-bulky'
auth = {'user[login]': 'becdot', 'user[password]': 'becca21'}
session_info = requests.session()
login_response = session_info.post(login_url, data=auth)
yarn_response = session_info.get(yarn_url)

print yarn_response.text




#f.close()