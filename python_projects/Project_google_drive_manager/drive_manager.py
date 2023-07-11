#Program to help manage files in gdrive
#This script is meant as a POC
#Google module required in directory
#import pandas as pd -- if you want to display as tables in console

from Google import Create_Service

#authentication details
CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

#initiates a connection using details
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#defines class for a call off spec
class callOffSpecification():
    def __init__(self,a,b,c):
        self.file_id = a
        self.file_name = b
        self.source_folder_id = c

    def getprojectname(self):
        folder_id = self.source_folder_id[0]
        response = service.files().get(fileId =folder_id, fields = 'name').execute()
        project = response['name']
        return str(project)

#folder to copy files to
#currently static but can be altered to accept commandline args for reusability
destination_folder = ''

#root folder to sort
#currently static but can be altered to accept commandline args for reusability
#lists all files/subfolders within given folder(files whose parent is the root)
folder_id = ''
query = f"parents = '{folder_id}'"
response = service.files().list(q=query).execute()
subFolders = response.get('files')

#finds the xxxxxx Folders within the subfolders of each project
tenderFolders= []
for folder in subFolders:
    folder_id = folder['id']
    query = f"parents = '{folder_id}' and (name= '' or name= '' or name= '')"
    response = service.files().list(q=query).execute()
    subsubFolders = response.get('files')
    for folder in subsubFolders:
        tenderFolders.append(folder['id'])

#searches through each tenderdoc folder to find the xxxxxxxx
projectsAndFiles = {}
for folder in tenderFolders:
    folder_id = folder
    query = f"parents = '{folder_id}' and (name contains '' or name contains '')"
    response = service.files().list(q=query, fields='*').execute()
    response2 = service.files().get(fileId =folder_id, fields ='parents').execute()
    parentProjects = response2
    callOffSpecs = response.get('files')
    for spec in callOffSpecs:
        specN = callOffSpecification(spec['id'],spec['name'],parentProjects['parents'])
        projectname = specN.getprojectname()
        query = f"parents = '{destination_folder}' and name= '{projectname}' and trashed = false"
        response3 = service.files().list(q=query).execute()
        if response3['files'] == []:
            file_metadata = { 'name' : projectname,
                              'mimeType' : 'application/vnd.google-apps.folder',
                              'parents' : [destination_folder]
                            }
            service.files().create(body=file_metadata).execute()
            query = f"parents = '{destination_folder}' and name= '{projectname}' and trashed = false"
            response4 = service.files().list(q=query).execute()
            newFolderIds = response4.get('files')
            for ids in newFolderIds:
                newFolderId = ids['id']
            file_metadata = {'parents': [newFolderId],
                             'name': specN.file_name}
            service.files().copy(fileId=specN.file_id,body=file_metadata).execute()
        elif response3['files']!=[]:
            newFolderIds = response3.get('files')
            for ids in newFolderIds:
                newFolderId = ids['id']
            file_metadata = {'parents': [newFolderId],
                             'name': specN.file_name}
            service.files().copy(fileId=specN.file_id,body=file_metadata).execute()

            
            
    

'''
------------------------unused code im saving for reference---------------------------------

#create the destination folders for each project
projectList =[]
for project in projectsAndFiles.keys():
    projectList.append(project)
for project in projectList:
    file_metadata = { 'name' : project,
                      'mimeType' : 'application/vnd.google-apps.folder',
                      'parents' : ['']
                    }
    service.files().create(body=file_metadata).execute()
'''

'''
#get the new folder id's
folder_id = ''
query = f"parents = '{folder_id}'"
response = service.files().list(q=query).execute()
Folders = response.get('files')
newFolderIds = []
for folder in Folders:
    newFolderIds.append(folder['id'])

print(newFolderIds)
'''
'''
<<<<<use a class to solve this problem>>>>
#copy the files(one at the moment):
file_metadata = {'parents': ['']}
file = projectsAndFiles[''][0]
print(file)
service.files().copy(fileId=file,body=file_metadata).execute()


<<<<<if file size too large incorporate below>>>>>

nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')


<<<<<to display in datframe use below>>>>>

pd.set_option('display.max_columns',100)
df = pd.DataFrame(files)
print(df)
'''
