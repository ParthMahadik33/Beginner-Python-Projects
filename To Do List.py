tasks=[]

# function to add tasks
def addtasks():
   while True: 
    x=input("Enter Task: ")
    tasks.append(x)
    print(f'Your task "{x}" has been added')
    print("EXit ? yes/no")
    if input().lower()=="yes":
      break
   
      
    
    

# function to view all tasks
def viewtasks():
    if not tasks:
      print("No tasks are added")
    i=1
    print("Your Tasks")
    for task in tasks:
    
     print(f"{i}: ",task)
     i=i+1
    input("Press Enter to exit....") 


# function to remove task
def removetask():
   z=int(input("Enter the index number of the task you want to remove: \n"))
   tasks.pop(z-1)

while True:
   #creating menu
   print("1: Add Tasks")
   print("2: View Tasks")
   print("3: Remove Tasks")
   print("4: Exit")
   
   try:
    y=int(input())
    if y==1:
     
     addtasks()
    elif y==2:
     viewtasks()
    elif y==3:
     removetask()
    elif y==4:
     print("Thanks for using the app !")
     break  
    else:
     print("Invalid option")  
     
   except ValueError:
     print("Invalid Input please enter a number")
     
      
                  
