from pip._vendor.distlib.compat import raw_input
tasks = []
ans=True
while ans:
    print ("""
    1.Add task
    2.view all tasks
    0.Exit/Quit
    ===============
    """)
    ans=raw_input("choose option : ")
    if ans=="1":
        new_task = input("enter the task : ")
        tasks.append(new_task)
        print("\n task Added")
    elif ans=="2":
        for task in tasks:
            print("task name: ", task)

    elif ans=="0":
      print("\n Goodbye")
      ans = 0