import urllib2, json
import requests

# Imports raw JSON data from the ravelry API
jsondata = urllib2.urlopen('http://api.ravelry.com/projects/becdot/progress.json?key=30820525c938d7eab6c933ce8dbe9c3ff1ee57b8&status=in-progress+hibernating+finished+frogged&notes=true')
rawdata = json.load(jsondata)

# Creates a dictionary with user details and exports it to the file userdata.txt
user_details = {}
for k, v in rawdata['user'].iteritems():
    user_details[k] = v
userdata = open('ravelryuserdata.txt', 'w')
userdata.write('%s\n' % repr(user_details))

# Creates a dictionary with project details (each project is a key, with sub-dicts of project information)
# and exports it to the file projectdata.txt
project_details = {}
for project in rawdata['projects']:
    for k, v in project.iteritems():
        project_details[project['name']] = project 
projectdata = open('ravelryprojectdata.txt', 'w')
projectdata.write('%s\n' % repr(project_details))    
        


login_url = 'https://www.ravelry.com/account/login'
yarn_url = 'http://www.ravelry.com/yarns/library/brown-sheep-lambs-pride-bulky'
auth = {'user[login]': 'becdot', 'user[password]': 'becca21'}
session_info = requests.session()
login_response = session_info.post(login_url, data=auth)
yarn_response = session_info.get(yarn_url)
yarn_response = yarn_response.text.encode('utf-8')

projectdata = open('ravelryprojectdata.txt', 'w')
yarnscrapedata = open('yarnscrapedata.txt', 'w')
projectdata.write('%s\n' % repr(project_details))
yarnscrapedata.write('%s\n' % yarn_response)


jsondata.close()
userdata.close()
projectdata.close()
yarnscrapedata.close()