import time,active,passive
print("✨ Welcome to the Active and passive voice practice ✨")
time.sleep(2)
print("Want to practice (yes or no)")
y = input("Enter your answer (y or n):  ")
while y.lower() == "y": 
 print("     1.Active","     2.Passive",sep="\n")
 choice = int(input("Enter the choice (1 or 2) :  "))
 if choice == 1:
  time.sleep(2)
  print('''Instructions:
         1.The questions are given in active voice
         2.You are asked to enter the correct passive voice''')
  time.sleep(4)
  i = 1
  for key in active.qa_dict:
    print(f"----------------Question {i} -------------------\n")
    print(f"{key}")
    ans=input("Enter your answer(q to quit):")
    if ans.lower() == active.qa_dict[key].lower():
        print("🔥Correct answer🔥\n")
    elif ans.lower() == "q":
        print("💐Thank you for using💐\n")
        break
    else:
        print("❌Wrong answer❌\n")
        print(f"The correct answer is : {active.qa_dict[key]}\n")
    i +=1
 elif choice == 2:
    time.sleep(2)
    print('''Instructions:
         1.The questions are given in passive voice
         2.You are asked to enter the correct active voice''')
    time.sleep(4)
    i = 1
    for key in passive.reversed_qa_dict:
        print(f"----------------Question {i} -------------------\n")
        print(f"{key}")
        ans=input("Enter your answer(q to quit):")
        if ans.lower() == passive.reversed_qa_dict[key].lower():
            print("🔥Correct answer🔥\n")
        elif ans.lower() == "q":
            print("💐Thank you for using💐\n")
            break
        else:
            print("❌Wrong answer❌\n")
            print(f"The correct answer is : {passive.reversed_qa_dict[key]}\n")
        i +=1
 else:
    print("!!SORRY!!","Kindly enter correct choice",sep="\n")
 y = input("Want to practice more (yes - y or no - n): ")
print("💐Thank you for using💐\n")
