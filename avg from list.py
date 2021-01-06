subjects = [{"telugu":0},{"english":0},{"hindi":0},{"maths":0},{"science":0},{"social":0}]
# print(subjects[0][0])
total = 0
for sub in subjects:
    for name in sub:
        sub[name]= int(input("enter " + name + " marks :"))
        total = total+sub[name]
for sub in subjects:
    for name in sub:
        print(name+" : "+str(sub[name]))
print("total:", total)
print("avg :", total/6)

# print(subjects)

