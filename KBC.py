questions = [
  ["1. Who developed Python Programming Language?","Wick van Rossum","Rasmus Lerdorf",
   "Guido van Rossum","Niene Stom",3
  ],
  ["2. Which type of Programming does Python support?","object-oriented programming",
   "structured programming","functional programming","all of the mentioned",4
  ],
  ["3. Is Python case sensitive when dealing with identifiers?","no","yes","machine dependent",
  "none of the mentioned",2
  ],
  ["4. Which of the following is the correct extension of the Python file?",".python",".pl",
   ".py",".p",3
  ],
  ["5. Is Python code compiled or interpreted?","Python code is both compiled and interpreted",
   "Python code is neither compiled nor interpreted","Python code is only compiled",
   "Python code is only interpreted",1
  ],
  ["6. All keywords in Python are in _________","Capitalized","lower case","UPPER CASE",
   "None of the mentioned",4
  ],
  ["7. What will be the value of the these Python expression? 4 + 3 % 5","7","2","4","1",1
  ],
  ["8. Which of the following is used to define a block of code in Python language?",
   "Indentation","Key","Brackets","All of the mentioned",1
  ],
  ["9. Which keyword is used for function in Python language?","Function","def","Fun","Define",2
  ],
  ["10. Which of the following character is used to give single-line comments in Python?",
   "//","#","!","/*",2
  ],
  ["11. Which of the following is true for variable names in Python?",
   "underscore and ampersand are the only two special characters allowed","unlimited length",
   "all private members must have leading and trailing underscores","none of the mentioned",2
  ],
  ["12.Python supports the creation of anonymous functions at runtime using a construct called",
  "pi","anonymous","lambda","none of the mentioned",3
  ],
  ["13. What is the order of precedence in python?",
  "Exponential, Parentheses, Multiplication, Division, Addition, Subtraction",
  "Exponential, Parentheses, Division, Multiplication, Addition, Subtraction",
  "Parentheses, Exponential, Multiplication, Division, Subtraction, Addition",
  "Parentheses, Exponential, Multiplication, Division, Addition, Subtraction",4
  ],
  ["14. What does pip stand for python?","Pip Installs Python","Pip Installs Packages",
   "Preferred Installer Program","All of the mentioned",3
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,320000,500000,720000,5000000,10000000]
# money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}\n")
  print(f"I. {question[1]}          II. {question[2]} ")
  print(f"III. {question[3]}       IV. {question[4]}\n")
  reply = int(input("Enter your answer (1-4) or  0 to quit:" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == (question[-1])):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 13):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")

