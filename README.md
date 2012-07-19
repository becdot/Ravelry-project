Ravelry-project
===============

1. Run createdata.py, which imports the JSON project data from Ravelry.com, and then writes it in dictionary form to the file projectdata.txt
2. Run yarncode.py, which:
    a. Initializes a Project and Yarn class
    b. Creates a Project class for each project in projectdata.txt, and populates it with project.name, project.url, and project.yarn which is a list of Yarn classes containing project.yarn.url and project.yarn.name
    c. Uses Python Requests to webscrape the html data of each project page
    d. Searches the html data for the total yardage of each yarn used, and assigns it to project.yarn.yardage
    e. Calculates the total number of yards used for all projects
    f. Provides interesting statistics for the length of yarn used!