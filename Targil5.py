#שנה את תרגיל 4, אם נתקלת במילה הקטנה מ4 אותיות צא מהלולאה

list1=['hello','phyton','pen', 'world of coding']
i=0
while i < len(list1):
    if len(list1[i])<4:
        break
    x=list1[i].upper()
    print (x)
    i+=1
