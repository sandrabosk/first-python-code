''' Create three dictionaries: lloyd, alice, and tyler.

Give each dictionary the keys "name", "homework", "quizzes", and "tests".

Have the "name" key be the name of the student (that is, lloyd's name should be "Lloyd") 
and the other keys should be an empty list for now. '''


lloyd = {
  "name": "Lloyd",
  "homework": [],
  "quizzes": [],
  "tests": []
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

''' Below your code, create a list called students that contains lloyd, alice, and tyler. '''
students = [lloyd, alice, tyler]

''' for each student in your students list, print out that student's data, as follows:

print the student's name
print the student's homework
print the student's quizzes
print the student's tests '''

for student in students:
  print "student name: %s" %student["name"]
  print "homework scores: %s" %student["homework"]
  print "quizzes scores: %s" %student["quizzes"]
  print "test scores: %s" %student["tests"]
  print


''' Write a function average that takes a list of numbers and returns the average:
    
    1. Define a function called average that has one argument, numbers.
    2. Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
    3. Like the example above, use float() to convert total and store the result in total.
    4. Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
    5. Return that result.
    '''

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

''' Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average. Define a function called get_average that takes one argument called student. Make a variable homework that stores the average() of student["homework"]. Repeat the above step for "quizzes" and "tests". Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%. '''

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
                
    total = homework *.1 + quizzes * .3 + tests * .6
    return total
  
''' Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.
    
    Inside your function, test score using a chain of if: / elif: / else: statements, like so:
    If score is 90 or above: return "A"
    Else if score is 80 or above: return "B"
    Else if score is 70 or above: return "C"
    Else if score is 60 or above: return "D"
    Otherwise: return "F"
    Finally, test your function!
    
    Print the resulting letter grade with print. Call the get_letter_grade function and 
    pass in get_average(lloyd).'''

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

print get_average(lloyd)
