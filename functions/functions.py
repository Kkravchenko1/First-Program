def Weekly_master():                                                    ##weekly calculation
     try: 
       weeklya = float(input('What is the weekly amount? '))
     except ValueError: 
       print("This is not an acceptable numerical value, please try again. ")
     else:
        weekly = float(weeklya*52)/12
        print('Borrower paid ' + str(paySchedule) + ' *52/12= ' + str(weekly) + ' Gross monthly income')

def Biweekly_master():
    try:
     biweeklya = float(input('What is the Bi-weekly amount? '))       ##bi-weekly calculation
    except ValueError: 
      print("This is not an acceptable numerical value, please try again. ")
    else: 
      biweekly = (biweeklya*26)/12
      print('Borrower paid ' + str(paySchedule) + ' *52/12= ' + str(biweekly))


def Semimonthly_master():                                              ##semi-monthly calculation 
    try:
     semimonthlya = float(input('What is the semi-monthly amount? '))
    except ValueError: 
     print("This is not an acceptable numerical value, please try again. ")
    else:
     semimonthly = (semimonthlya*26)/12
     print('Borrower paid ' + str(paySchedule) + ' *52/12= ' + str(semimonthly))

def Monthly_master():
    try:
     semimonthlya = float(input('What is the monthly amount? '))       ##monthly calculation 
    except:
     print("This is not an acceptable numerical value, please try again. ")
     semimonthly = (semimonthlya)
     print('Borrower paid '+ str(semimonthly))


def Variable_quest():                                                   ##variable income calc
    while True: 
       try:
        num2020 = float(input('Enter 2020 base earnings: '))
       except ValueError:
          print("Unacceptable character detected, please enter only numerical values. ")
       else:
        break

    while True:
        try:
         num2021 = float(input('Enter 2021 base earnings: '))
        except ValueError:
          print("Unacceptable character detected, please enter only numerical values. ")
        else: 
         break

    while True:
        try:
         num2022 = float(input('Enter 2022 year to date earnings: '))    
        except ValueError:
          print("Unacceptable character detected, please enter only numerical values. ")
        else:
         break
         
    while True:
         try:
           ytdavg = float(input('What date is posted on the check date? 1-30: '))
         except ValueError:
             print('Please try again')
         
         if ytdavg > 30:
            print('Please try using a number from 1-30.')
         else:
          break
    while True:
        try:
         ytdmave = int(input('What month is posted on the paystub? 1-12: '))      
        except ValueError:
          print("Unacceptable character detected, please enter only numerical values. ")
        else:
         break

    sum = float(num2020) + float(num2021) 
    ceBase = (float(num2020) + float(num2021)) / 24
    ceBase2 = (float(num2021)/12)
    ytdAverage = float(ytdavg)/30 + float(ytdmave) - 1
    ytdCombined = float(ytdAverage + ceBase2)
    ytdmcombined = float(ytdAverage + 12)
    ceVariable = float(num2022)/float(ytdAverage)
    
    print('The combined earnings for 2020 and 2021 are {2}'.format(num2020, num2021, sum))
    print('The 24 month average is ' + str(ceBase))
    print('The 12 month average of 2021 is ' + str(ceBase2))
    print("The year to date average is " + str(ceVariable))
    if ceVariable < ceBase2:
        print("Year to date is less than 12 month average of 2021, use year to date: " + str(ceVariable))
    else: 
        print("Year to date is more than a 12 month average, a " + str(ytdAverage) + "12 month average should be used: " + str(ytdCombined / ytdmcombined))
   




## Beginning of program


while True:
 nav1 = input ('What type of income is being used? Currently the income calc only supports salary and variable base earnings: ').lower() #deciding what type of calc to use
 if nav1 == 'salary':                                                                                                                   
     paySchedule = (input('How often is the borrower paid? (weekly/biweekly/semi-monthly/monthly?): ')).lower()
     if paySchedule == 'weekly': 
         Weekly_master();
     if paySchedule == 'biweekly':
         Biweekly_master()
     if paySchedule == 'semimonthly':
         Semimonthly_master()
     if paySchedule == 'monthly':
         Monthly_master()
 elif nav1 == 'variable':
     Variable_quest();







