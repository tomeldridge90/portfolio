#python to do list
import shelve

print('Enter your name:\n')
user = input()

def mainPage():
    shelfFile = shelve.open('toDoListData')
    print('--------To do list--------\n')
    if user in list(shelfFile.keys()) and len(shelfFile[user])>0:
        print('Welcome back ' + user + '\n')
        for task, desc in shelfFile[user].items():
            print(task +'\n' + '\t' + desc)
        print('\n--------------------------\n')
        print('Select an option: \n\nCreate[1]\nEdit[2]\nDelete[3]\nExit[4]')
    else:
        shelfFile[user] = {}
        print('Welcome ' + user +', a list To Do list has been created for you but is currently empty')
        print('\n--------------------------\n')
        print('Select an option: \n\nCreate[1]\nExit[4]')
    shelfFile.close()

def createTask():
    success = False
    while success == False:
        shelfFile = shelve.open('toDoListData')
        taskList = shelfFile[user]
        print('Enter the title of the new task: ')
        title = input()
        print('Enter the description of the new task: ')
        desc = input()
        if title in taskList:
            print('A task with this title already exists, enter a new title\n')
            shelfFile.close()
            continue
        else:
            taskList[title] = desc
            shelfFile[user] = taskList
            shelfFile.close()
            success = True

def editTask():
    success = False
    while success == False:
        shelfFile = shelve.open('toDoListData')
        taskList = shelfFile[user]
        print('Enter the title of the task you would like to edit: ')
        title = input()
        oldtitle = title
        olddesc = taskList[oldtitle]
        if oldtitle not in taskList:
            print('There is no task with this title in your to do list')
            shelfFile.close()
            continue
        else:
            print('Edit the title?[y or n]')
            choice = input()
            if choice == 'y':
                print('Enter the new title of the task')
                del taskList[oldtitle]
                title = input()
            print('Edit the description?[y or n]')
            choice = input()
            if choice == 'y':
                print('Enter the new description of the task')
                desc = input()
                taskList[title] = desc
            else:
                taskList[title] = olddesc
            shelfFile[user] = taskList
            shelfFile.close()
            success = True

def deleteTask():
    success = False
    while success == False:
        shelfFile = shelve.open('toDoListData')
        taskList = shelfFile[user]
        print('Enter the title of the task you would like to delete(enter c to cancel): ')
        deltask = input()
        if deltask not in taskList and deltask != 'c':
            print('There is no task with this title in your to do list')
            shelfFile.close()
            continue
        elif deltask =='c':
            shelfFile.close()
            success = True
        else:
            del taskList[deltask]
            shelfFile[user] = taskList
            print('The task has been deleted')
            shelfFile.close()
            success = True

def exitApp():
    print('\nClosing To Do list........')
    quit()

while True:
    mainPage()
    menuOption = input()
    if str(menuOption) in ('Create','1'):
        createTask()
        continue
    elif str(menuOption) in ('Edit','2'):
        editTask()
        continue
    elif str(menuOption) in ('Delete','3'):
        deleteTask()
        continue
    elif str(menuOption) in ('Exit','4'):
        exitApp()
    else:
        print('Please select an option from the menu')
        continue




