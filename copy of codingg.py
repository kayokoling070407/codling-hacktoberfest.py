counter = 0
score = 0
total_num_of_qn = 5

  
print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 5


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 12 + 2?")
  print("   a) 10")
  print("   b) 24")
  print("   c) 14")
  print("   d) 6")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not subtraction."
    score -=1
  elif answer == "b":
    output = "Wrong. This is not multiplication."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is not division."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two hydrogen atoms")
  print("   c) one hydrogen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. If so, then it will be written as H and H - two hydrogen atoms."
    score -=1
  elif answer == "c":
    output = "Wrong. Clearly the number 2 in the formulae must mean something?"
    score -=1
    
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a non-metal?")
  print("   a) 2,1")
  print("   b) 2,8,3")
  print("   c) 2,8,8,2")
  print("   d) 2,7")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
 
 

counter +=1
tracker = 0

while tracker !=1:
  print("Q"+str(counter)+") "+ "Which correctly represents a plant cell in a leaf")
  print("   a) have cell wall, does not have nucleas")
  print("   b) have a vacuole, have flagella")
  print("   c) have large-central vacoule, have chloroplast")
  print("   d) have nucleas, does not have chloroplast")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - nucleas in needed for activity control in the cell"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - does the plant cell need to move?"
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    score +=1
    
  elif answer == "d":
    output = "Wrong.  Think again - does the plant cell in a leaf need to make plants?"
    tracker =1
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
 
 
 
counter +=1
tracker = 0

while tracker !=1:
  print("Q"+str(counter)+") "+ "find 'x' if 2(x+1)-3(x+5)")
  print("   a) 19")
  print("   b) -20")
  print("   c) -6")
  print("   d) have nucleas, does not have chloroplast")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - did you miss out someting?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - did you caluculate correctly?"
    score -=1
  elif answer == "c":
    output = "Wrong. Think again - did you convert the '+' and "-" signs correctly?"
    score +=1
    
  elif answer == "d":
    output = "Yes. Well done!"
    tracker =1
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()  
  
 
  
print("End of quiz!")
  
