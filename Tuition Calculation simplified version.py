'''print the welcome sentence and turn all the string into int'''
print("2019 MSU Undergraduate Tuition Calculator.\n")
tuition = ""
level = ""
snt =int()
money = int()
money2 = int()
money3 = int()
Cumoney = int()
money4 = int()
Cmoney= int()
c= int()
student=""
R= input("Resident (yes/no): ").lower()
'''start the loop for ask question'''
while True:
    ''' the options of year, collage, major and start to calculate the tuition fee'''
    level = input("Level—freshman, sophomore, junior, senior: ").lower()
        
    if level == "junior" or level == "senior":
        college = input("Enter college as business, engineering, health, sciences, or none: ")
        
        if college =="business":
            money = 226
            money3 = 8595
            Cmoney =573
        elif college == "engineering":
            money =670
            money3 =8595
            Cmoney =573
        elif college == "health":
            money =100
            money3 = 8595
            Cmoney =573
        elif college == "sciences":
            money = 100
            money3 = 8595
            Cmoney =573
        else:
            money = 0
            money3 =8325
            Cumoney = 555
        ce = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower()
        if ce =="yes":
            jm = input("Are you in the James Madison College (yes/no): ")
            money2 = 670
        else:
            money2 = 0
    if level == "freshman" or level == "sophomore":
        admitted = input("Are you admitted to the College of Engineering (yes/no): ").lower()
        if admitted =="no":
            jm = input("Are you in the James Madison College (yes/no): ")
    if level =="freshman" or level == "sophomore" or level == "junior" or level == "senior":
        c=input("Credits: ")
        
        while c.isdigit() is False or int(c)<=0 :
            
            print("Invalid input. Try again.")
            c=input("Credits: ")
            
               
        if int (c)<6:
            snt=0
        else:
            snt=5
        if level == "freshman":
                
            if 0< int(c) <=11:
                tuition = c * 482 +21+3+snt      
            elif 12<= int(c) <=18:
                tuition = 7230+29
            else:
                tuition = 7230 + (int(c)-18)*482+29
                                   
        if level == "sophomore":
            if student== "yes":
                tuition= 19883+(int(c)-18)*1325.50+29+750+670
            else:
                if 0<c<=11:
                    tuition = int(c)*494+24+snt
                elif 12<=c<=18:
                    tuition = 7410+29
                else:
                    tuition = 7410+29+(int(c)-18)*494    
            
        if level == "junior":
            if 0<int(c)<=11:
                tuition = int(c) *Cumoney+24+ snt + money + money2
            elif 12<=int(c)<=18:
                tuition = money3+29+ money+money2
            else:
                tuition =money3+29+(c-18)*555+money+money2
            
        if level == "senior":
            if 0<int(c)<=11:
                tuition = int( c) *Cmoney+24+ snt + money + money2
            elif 12<=int(c)<=18:
                tuition = money3+29+ money+money2
            else:
                tuition =money3+29+(int(c)-18)*555+money+money2       
        print("Tuition is $"+"{:0,.2f}.".format(tuition))
        
        an = input("Do you want to do another calculation (yes/no): ").lower()
        ''' repeat the question'''
        if an == "yes":
            
            R=input("Resident (yes/no): ").lower()
            
            if R == "no":
                student= input("International (yes/no): ").lower()
                
        else:
            break
        
              
    else:   
        print("Invalid input. Try again.")
         