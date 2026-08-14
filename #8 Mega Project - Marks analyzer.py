import numpy as np


marks = np.random.randint(1,101, size = (100,5))         # Random marks

def result():                                                   # result
    for studentno, studentmarks in enumerate(marks, start = 1):
        print(f"Student {studentno}: {studentmarks}")

average = np.mean(marks, axis = 1)

def averageresult():
    for averageno, averagemarks in enumerate(average, start = 1):  # avg result
        
        print(f"Student {averageno}: {averagemarks}")

def topscore():                                       # top scorer
    topscore = np.max(marks)  
    print(topscore)

def lowestscore():                                      # lowest score
    lowscore = np.min(marks)                
    print(lowscore)

def topper():                                           # topper
    topper = np.argmax(average)
    topperindex = topper + 1
    print(f"Student: {topperindex} has scored the highest marks")
    print(average[topper])

def passfail():                                                             # passfail
    passfail = average > 33
    print(passfail)

    for passfailno, status in enumerate(passfail, start = 1):
        if status == True:
            status = "Pass"
        elif status == False:
            status = "Fail" 

        
        print(f"Student {passfailno}: {status}")


def schoolaverage():                                            # school avg
    schoolaverage = np.mean(average)
    print(f"The school average is {schoolaverage}")


def lowestscorer():                                                         # lowest scorer
    lowestscorer = np.argmin(average)
    lowestscorerindex = lowestscorer + 1
    print(f"Student: {lowestscorerindex} has scored the lowest marks")
    print(average[lowestscorer])

def firstdivision():                                            # first division
    firstdivision = average >= 70

    for firstdivisionno, firstdivisionstatus in enumerate(firstdivision, start = 1):
        
        print(f"Student {firstdivisionno}: {firstdivisionstatus}")

def median():                                               # median
    median = np.median(average)
    print(f"The median of school is: {median}")

def standarddeviation():                                                    # std deviation
    stddeviation = np.std(average)
    print(f"The standard deviation of school is: {stddeviation}")

def avgpersubject():                                                            # avg per subject
    avgpersubject = np.mean(marks, axis = 0)
    print(avgpersubject)

def hardestsub():                                                           # hardest subject
    _average = np.mean(marks, axis = 0)
    hardestsub = np.argmin(_average)
    
    print("Subject:",hardestsub + 1, "Was the hardest subject")
                           
def easiestsub():                                                                   # easiest subject
    _average = np.mean(marks, axis = 0)
    easiestsub = np.argmax(_average)
    
    print("Subject:",easiestsub + 1, "Was the easiest subject")

def grade():                                                                # grade finder

    gradeA = average >= 90
    gradeB = (average >= 70) & (average < 90)
    gradeC = (average >= 50) & (average < 70)
    gradeD = (average >= 33) & (average < 50)
    gradeF = average < 33 
    countA = np.count_nonzero(gradeA)
    countB = np.count_nonzero(gradeB)
    countC = np.count_nonzero(gradeC)
    countD = np.count_nonzero(gradeD)
    countF = np.count_nonzero(gradeF)

    print("Grade A :",countA) 
    print("Grade B :",countB) 
    print("Grade C :",countC) 
    print("Grade D :",countD) 
    print("Grade F :",countF) 

grade()




# THE END, WE CAN CALL ANY FUNCTION
