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
  