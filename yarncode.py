import re
import requests

# Enter your Ravelry.com username
username = 'username'
# Enter your Ravelry.com password
password = 'password'

# Defines the Project and Yarn classes
class Project:
    def __init__(self, name):
        self.name = name
        self.url = ''
        self.skeins = 0
        self.yarn = []
        
    def __repr__(self):
        return '%s: Url: %s, Skeins: %s, Yarn: %s' % (self.name, self.url, self.skeins, self.yarn)
        
    def createyarns(self, yarndicts):
        yarnlist = []
        for dict in yarndicts:
            self.yarn = Yarn()
            self.yarn.url = dict['url']
            self.yarn.name = '%s by %s' % (dict['name'], dict['brand'])
            yarnlist.append(self.yarn)
        return yarnlist
    
class Yarn:
    def __init__(self):
        self.name = ''
        self.url = ''      
        self.yardage = 0

    def __str__(self):
        return '%s: Yardage: %s, Yarn Url: %s' % (self.name, self.yardage, self.url)        
    def __repr__(self):
        return '%s: Yardage: %s, Yarn Url: %s' % (self.name, self.yardage, self.url)   
        
# Creates instances of the Project and Yarn classes, and populates with project.name, project.url, project.yarn.name, project.yarn.url
projectdatafile = open('projectdata.txt', 'r')
projectdata = eval(projectdatafile.read())    
list_of_projects = []
for project_name, project_data in projectdata.iteritems():
    project = Project(project_name)
    project.url = project_data['url']
    project.yarn = project.createyarns(project_data['yarns'])
    list_of_projects.append(project)
            
    
# Webscrapes the project data and returns it in html form
def projectdata(project_url):
    login_url = 'https://www.ravelry.com/account/login'
    auth = {'user[login]': username, 'user[password]': password}
    session_info = requests.session()
    login_response = session_info.post(login_url, data=auth)
    project_response = session_info.get(project_url)
    project_response = project_response.text.encode('utf-8')
    return project_response
    
# Searches the html of projectdata for the yarn urls and yardage per yarn, and returns a list of [[url1, yardage1], [url2, yardage2], etc]
def yardage(project_html):
    yarnurl_list = re.findall('\>Yarn\<.*?\<\/a\>', project_html, flags=re.DOTALL)
    yarnurl_list = re.findall('http.+?(?:(?!").)*', str(yarnurl_list))
    yardage_list = re.findall('skeins\ \=.*?(?:(?!yards).)*', project_html, flags=re.DOTALL)
    yardage_list = re.findall('\d+\.\d+', str(yardage_list))
    both_list = [[yarnurl_list[i], float(yardage_list[i])] for i in range(len(yardage_list))]
    return both_list    

# Assigns project.yarn.yardage
for project in list_of_projects:
    urlandyardage = yardage(projectdata(project.url))
    for yarn in project.yarn:
        for sublist in urlandyardage:
            if yarn.url == sublist[0]:
                yarn.yardage = sublist[1]
        

# Determines the total length of yarn used over all projects
totalyards = 0
for project in list_of_projects:
    for yarn in project.yarn:
        totalyards += yarn.yardage
                 
# Prints out the final information
interesting_distances = {'moon': 420388320, 'len_africa': 8748906, 'bos_to_nyc': 387200, 'baseball_perimeter': 120}
print "\nIn %d projects, you have used a total of %s yards of yarn!" % (len(list_of_projects), totalyards)
print "\nThat is: \n %f trips to the moon! \n %f journeys down the length of Africa!\n %f drives from Boston to New York City! \n %f times around the perimeter of a baseball diamond!" % (round(totalyards / interesting_distances['moon'], 6), round(totalyards / interesting_distances['len_africa'], 6), round(totalyards / interesting_distances['bos_to_nyc'], 6), round(totalyards / interesting_distances['baseball_perimeter'], 6))
     
projectdatafile.close()
