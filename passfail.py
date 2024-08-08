def pass_fail(score):
   pass_marks=50
   if score>=pass_marks:
      return "Passed"
   else:
      return "Failed"

score=int(input("The score: "))
result=pass_fail(score)
print(result)
    