import urllib2, json

# Imports raw JSON data from the ravelry API
jsondata = urllib2.urlopen('http://api.ravelry.com/projects/becdot/progress.json?key=30820525c938d7eab6c933ce8dbe9c3ff1ee57b8&status=in-progress+hibernating+finished+frogged&notes=true')
rawdata = json.load(jsondata)

# Creates a dictionary with project details (each project is a key, with sub-dicts of project information)
# and exports it to the file projectdata.txt
project_details = {}
for project in rawdata['projects']:
    for k, v in project.iteritems():
        project_details[project['name']] = project 
projectdata = open('projectdata.txt', 'w')
projectdata.write('%s\n' % repr(project_details))    
        
jsondata.close()
projectdata.close()