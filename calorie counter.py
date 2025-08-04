from colorama import Fore, Style, init

lines = ["Welcome to your Fitness Tracker — your journey to a healthier you starts now!"]

import time
import sys
import os

for line in lines:         
    for x in line:         
        print(Fore.BLUE + x, end='')   
        sys.stdout.flush()
        time.sleep(0.03)         
    print('')
    

time.sleep(1)
 
print('')
print('')

lines = ["Enter your name to continue"]
for line in lines:         
    for x in line:         
        print(Fore.WHITE+ x, end='')   
        sys.stdout.flush()
        time.sleep(0.03)         
    print('')

time.sleep(1)

print('')
    
name = input(Fore.RED+"Name : ")

os.system('cls')

print(Fore.WHITE + 'Hii '+name+', This program is designed to help you take control of your fitness journey.')
print('By calculating how many calories you should burn each day based on your body, ')
print('goals, and timeline, it gives you a clear path to reach your target weight.')
print('Whether you\'re aiming to slim down, tone up, or just stay healthy, this tool')
print('will guide you step by step. Let\'s get started and make your goals a reality!')

print('')
print('')
x= input('Press enter to continue ....')

os.system('cls')

lines = ["Please Enter your Details"]
for line in lines:         
    for x in line:         
        print(Fore.WHITE+ x, end='')   
        sys.stdout.flush()
        time.sleep(0.03)         
    print('')
    
time.sleep(0.3)
print('')

age = int(input(Fore.GREEN+'Age : '))

while age>90 or age<10:
    print('')
    print('Enter a valid Age')
    print('')
    age = int(input(Fore.YELLOW+'Age : '))
    


print('')

height = int(input(Fore.YELLOW+'Height(in cm) : '))
print('')

gender= input(Fore.WHITE+'Gender(M/F) : ')
print('')

CW = float(input(Fore.GREEN+"Current Weight(in KGs) : "))
print('')

TW = float(input(Fore.YELLOW+"Target Weight(in KGs) : "))
print('')

while CW == TW:
    print('')
    print('Current Weight can\'t be equal to the Target Weight')
    print('')
    CW = int(input(Fore.GREEN+"Current Weight(in KGs) : "))
    print('')
    TW = int(input(Fore.YELLOW+"Target Weight(in KGs) : "))
    print('')
    


print(Fore.GREEN+'       Active level')
print(Fore.WHITE+'1) Sedentary - little to no exercise')
print(Fore.WHITE+'2) Lightly Active - exercise 1-3 days per week')
print(Fore.WHITE+'3) Moderately Active - 3-5 days per week')
print(Fore.WHITE+'4) Very Active- 6-7 days per week')
print('')
AL = int(input(Fore.WHITE+"Your Active Level (1/2/3/4) : "))

print('')

days = int(input(Fore.YELLOW+"Number of Days to Achieve it : "))
print('')

os.system('cls')

lines = ["Thank You Very much for the information "]
for line in lines:         
    for x in line:         
        print(Fore.WHITE+ x, end='')   
        sys.stdout.flush()
        time.sleep(0.03)         
    print('')

time.sleep(1)
print('')
os.system('cls')
if CW >TW :    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WEIGHT LOSS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #
    
    
    print(Fore.CYAN + 'Awesome! ' + name + ', you’ve chosen to begin your weight loss journey.')
    print('That’s a powerful and inspiring step toward becoming healthier, more confident, and full of energy.')
    print('With the right balance of nutrition, activity, and consistency, you’ll reach your goal and feel better every day.')
    print('Let’s calculate exactly how many calories you need to burn each day to hit your target weight safely and effectively.')
    print('Ready to take control and transform your life? Let’s get started!')
    print('')
    print('')
    time.sleep(4)
    
    
    
    



    
    time.sleep(0.3)
    

    WL = CW-TW                              # WEIGHT TO LOSS
    WL = str(WL)
    days = str(days)
    print(Fore.WHITE+'You are planning to lose ',WL,'kgs within '+days+' days.')
    
    time.sleep(0.05)
    
    print('')
    
    if gender == 'M' :                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GENDER = MALE<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
    
        BMR = 10*CW +6.25*height - 5*age +5
        BMR = str(BMR)
        
         
        print('Your Basal Metabolic Rate(BMR) is '+BMR)
        BMR = float(BMR)
        
        print('')
         
    
        if AL == 1:
        
            TDEE = 1.2*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        elif AL == 2:
            
            TDEE = 1.375*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
                  
                  
        elif AL == 3:
            TDEE = 1.55*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        
        elif AL == 4:
            TDEE = 1.725*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
            
        print('')
        WL = float(WL)
        
        TOTCAL = WL*7700
        
        TOTCAL = str(TOTCAL)
        
        print('Total calories to burn : ',TOTCAL)
        
        print('')
        
        TOTCAL = float(TOTCAL)
        days = int(days)
        
        TOTCALDAY = TOTCAL/days
        TOTCALDAY = str(TOTCALDAY)
        
        
        
        print('Calories to burn per day : ',TOTCALDAY)
        TOTCALDAY = float(TOTCALDAY)
        TDEE = float(TDEE)
        print('')
        calgoal = TDEE - TOTCALDAY
        calgoal = str(calgoal)
        print(Fore.BLUE+'Daily calorie goal : ',calgoal)
        
        print('')
        lines = ["Press Enter to End the program"]
        for line in lines:
            for x in line:
                print(Fore.GREEN+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        x= input('')
        os.system('cls')
        
        lines = ["                       THANK YOU "]
        for line in lines:
            for x in line:
                print(Fore.RED+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        time.sleep(10)
        
        
    
    
        
        
        
        

    else :                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GENDER = FEMALE<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        
        
    
        BMR = 10*CW +6.25*height - 5*age-161
        BMR = str(BMR)
        
         
        print('Your Basal Metabolic Rate(BMR) is '+BMR)
        BMR = float(BMR)
        
        print('')
         
    
        if AL == 1:
        
            TDEE = 1.2*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        elif AL == 2:
            
            TDEE = 1.375*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
                  
                  
        elif AL == 3:
            TDEE = 1.55*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        
        elif AL == 4:
            TDEE = 1.725*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
            
        print('')
        WL = float(WL)
        
        TOTCAL = WL*7700
        
        TOTCAL = str(TOTCAL)
        
        print('Total calories to burn : ',TOTCAL)
        
        print('')
        
        TOTCAL = float(TOTCAL)
        days = int(days)
        
        TOTCALDAY = TOTCAL/days
        TOTCALDAY = str(TOTCALDAY)
        
        
        
        print('Calories to burn per day : ',TOTCALDAY)
        TOTCALDAY = float(TOTCALDAY)
        TDEE = float(TDEE)
        print('')
        calgoal = TDEE - TOTCALDAY
        calgoal = str(calgoal)
        print(Fore.BLUE+'Daily calorie goal : ',calgoal)
        
        print('')
        lines = ["Press Enter to End the program"]
        for line in lines:
            for x in line:
                print(Fore.GREEN+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        x= input('')
        os.system('cls')
        
        lines = ["                       THANK YOU "]
        for line in lines:
            for x in line:
                print(Fore.RED+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        time.sleep(10)
        
#####################################################################################################
#####################################################################################################
#####################################################################################################
        
        
else:    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WEIGHT GAIN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #
    
    
    
    print(Fore.YELLOW + 'Awesome! ' + name + ', you’ve chosen to begin your weight gain journey.')
    print('That’s a bold and empowering step toward building strength, confidence, and a healthier body.')
    print('With the right nutrition, training, and consistency, you’ll reach your goal and feel more energized than ever.')
    print('Let’s calculate exactly how many calories you need each day to grow stronger and reach your target weight.')
    print('Ready to bulk up the smart way? Let’s get started!')
    print('')
    print('')
    time.sleep(4)


    
    time.sleep(0.3)
    

    WL = TW-CW                              # WEIGHT TO GAIN
    WL = str(WL)
    days = str(days)
    print(Fore.WHITE+'You are planning to gain ',WL,'kgs within '+days+' days.')
    
    time.sleep(0.05)
    
    print('')
    
    if gender == 'M' :                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GENDER = MALE <<<<<<<<<<<<<<<<<<<<<<<<<<<
        
    
        BMR = 10*CW +6.25*height - 5*age +5
        BMR = str(BMR)
        
         
        print('Your Basal Metabolic Rate(BMR) is '+BMR)
        BMR = float(BMR)
        
        print('')
         
    
        if AL == 1:
        
            TDEE = 1.2*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        elif AL == 2:
            
            TDEE = 1.375*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
                  
                  
        elif AL == 3:
            TDEE = 1.55*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        
        elif AL == 4:
            TDEE = 1.725*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
            
        print('')
        WL = float(WL)
        
        TOTCAL = WL*7700
        
        TOTCAL = str(TOTCAL)
        
        print('Total calories to Gain : ',TOTCAL)
        
        print('')
        
        TOTCAL = float(TOTCAL)
        days = int(days)
        
        TOTCALDAY = TOTCAL/days
        TOTCALDAY = str(TOTCALDAY)
        
        
        
        print('Calories to gain per day : ',TOTCALDAY)
        TOTCALDAY = float(TOTCALDAY)
        TDEE = float(TDEE)
        print('')
        calgoal = TDEE + TOTCALDAY
        calgoal = str(calgoal)
        print(Fore.BLUE+'Daily calorie goal : ',calgoal)
        
        print('')
        lines = ["Press Enter to End the program"]
        for line in lines:
            for x in line:
                print(Fore.GREEN+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        x= input('')
        os.system('cls')
        
        lines = ["                       THANK YOU "]
        for line in lines:
            for x in line:
                print(Fore.RED+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        
        time.sleep(10)
        


    else :                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GENDER = FEMALE<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        
        
    
        BMR = 10*CW +6.25*height - 5*age -161
        BMR = str(BMR)
        
         
        print('Your Basal Metabolic Rate(BMR) is '+BMR)
        BMR = float(BMR)
        
        print('')
         
    
        if AL == 1:
        
            TDEE = 1.2*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        elif AL == 2:
            
            TDEE = 1.375*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
                  
                  
        elif AL == 3:
            TDEE = 1.55*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
        
        elif AL == 4:
            TDEE = 1.725*BMR
            TDEE = str(TDEE)
            print('Your Total daily energy expenditure is ',TDEE,' calories')
            
            
        print('')
        WL = float(WL)
        
        TOTCAL = WL*7700
        
        TOTCAL = str(TOTCAL)
        
        print('Total calories to Gain : ',TOTCAL)
        
        print('')
        
        TOTCAL = float(TOTCAL)
        days = int(days)
        
        TOTCALDAY = TOTCAL/days
        TOTCALDAY = str(TOTCALDAY)
        
        
        
        print('Calories to gain per day : ',TOTCALDAY)
        TOTCALDAY = float(TOTCALDAY)
        TDEE = float(TDEE)
        print('')
        calgoal = TDEE + TOTCALDAY
        calgoal = str(calgoal)
        print(Fore.BLUE+'Daily calorie goal : ',calgoal)
        
        print('')
        lines = ["Press Enter to End the program"]
        for line in lines:
            for x in line:
                print(Fore.GREEN+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
        x= input('')
        os.system('cls')
        
        lines = ["                       THANK YOU "]
        for line in lines:
            for x in line:
                print(Fore.RED+ x, end='')   
                sys.stdout.flush()
                time.sleep(0.03)         
            print('')
            
        time.sleep(10)
        
        
    
            
            
        
        
         
    

    
    
    
    
    














 













