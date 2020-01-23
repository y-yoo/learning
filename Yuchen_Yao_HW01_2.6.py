print('determine a grade for a course')

import numpy as np

print('please input course number and your name!')
course_number = input('course number:')
name = input('name:')

WQ = int(input('Weighting factor of quizzes:'))
WH = int(input('Weighting factor of homework:'))
WF = int(input('Weighting factor of the final exam:'))

q = input('quizzes:')    
qlist = q.split(',')
#input all the grades and turn them into a list
qlist = [int(qlist[i]) for i in range(len(qlist))]
#translat every value inputed to int from str
AQ = np.mean(qlist)
print('Average grade of quizzes is ',AQ)


h = input('homework:')    
hlist = h.split(',')
#input all the grades and turn them into a list
hlist = [int(hlist[i]) for i in range(len(hlist))]
#translat every value inputed to int from str
AH = np.mean(hlist)
print('Average grade of homework is ',AH)


response = input('Does this course have a final grade?(yes/no)')
if response == 'yes':

    FE = int(input('input the final grade:'))
    AG = (WQ*AQ + WH*AH + WF*FE)/(WQ + WH + WF)

else:

    AG = (WQ*AQ* + WH*AH)/(WQ*WH)


print(course_number, name)
print('AG: {:.2f}%'.format(AG))

