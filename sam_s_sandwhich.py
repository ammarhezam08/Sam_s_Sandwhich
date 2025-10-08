import datetime

#The purpose of this function is to enter in a valid number
def force_number(message,lower,upper):
    while True: #infinite loop that keeps repeating until a valid number is entered
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                return num #returning back a valid number within a range
            else:
                print(f"Incorrect, {num}, please enter in a number between {lower}-{upper}")
        except:
            print("Error, please enter in a number and not a text")

#This program will allow the user to enter in a name
def force_name(message,lower,upper):
    while True: #this is an infinite loop that will only break if only a valid name is entered
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            print("The name is valid")
            break #this loop breaks if the above conditions are met
        else:
            print("Invalid name")
    return name #a valid name is returned to the variable that called the function

first_name = force_name("Enter your first name",2,20)

#The purpose of this function is to enter in a valid number
def force_phonenumber(message,lower,upper):
    while True: #infinite loop that keeps repeating until a valid number is entered
        cell=str(input(message))
        if len(cell)>=lower and len(cell)<=upper and cell.isnumeric():
            return cell #returning back a valid number within a range
        else:
            print(f"Incorrect, {cell}, please enter in a number between {lower}-{upper}")

phone_number = force_phonenumber("Enter in your phone number",8,12)

def bread_selection():
    bread_list=["White","Brown","Italian","Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list[count])
        count +=1
    bread_selected=force_number("Which bread did you want? Enter a number: ",1,len(bread_list))
    return bread_list[bread_selected-1] #returns back a string

def cheese_selection():
    cheese_list=["Cheddar","Mozarrella","Feta","Gouda"]
    count=0
    print("We have the following types of cheese:")
    while count < len(cheese_list):
        print(count+1," ",cheese_list[count])
        count +=1
    cheese_selected=force_number("Which type of cheese did you choose? Enter a number: ",1,len(cheese_list))
    return cheese_list[cheese_selected-1]

def meat_selection():
    meats_list=["Beef","Chicken","Goat","Lamb"]
    count=0
    print("We have the following types of meats:")
    while count < len(meats_list):
        print(count+1," ",meats_list[count])
        count +=1
    meat_selected=force_number("Which type of meat did you choose? Enter a number: ",1,len(meats_list))
    return meats_list[meat_selected-1]

def salad_selection():
    vegetable_list=["Lettuce","Tomato","Cucumber","Onions","No salad"]
    count=0
    print("We have the following types of vegetables:")
    while count < len(vegetable_list):
        print(count+1," ",vegetable_list[count])
        count +=1
    print ("Press ENTER when you have finsished choosing your salads")
    salads_added = "" #Set to nothing
    salad_type = " " #adds an wmpty string
    
    while salad_type != "": 
        salad_type = input("what number salad do you want? \n1-Lettuce \n2-Tomato \n3-Cucumber \n4-Onions")
        if salad_type != "": #if you don't press to enter it will prompt you to enter a prompt
            salad_type = int(salad_type)
            salads_added = salads_added + " " + vegetable_list[salad_type-1]
    return salads_added.strip()

def dressings_selection():
    dressings_list=["Mayonnaise","Mustard","Aioli","Hummus","Ranch dressing","No dressing"]
    count=0
    print("We have the following types of dressings:")
    while count < len(dressings_list):
        print(count+1," ",dressings_list[count])
        count +=1
    dressing_selected=force_number("Which type of meat did you choose? Enter a number: ",1,len(dressings_list))
    return dressings_list[dressing_selected-1]

def sandwich_order():
    sandwhich_order = []

    sandwhich_order.append(first_name)
    sandwhich_order.append(phone_number)
    sandwhich_order.append(bread_choice)
    sandwhich_order.append(meat_choice)
    sandwhich_order.append(cheese_choice)
    sandwhich_order.append(salad_choice)
    sandwhich_order.append(dressing_choice)
    output_text_file(sandwhich_order)

def output_text_file(sandwhich_order):
    date_time=datetime.datetime.now()
    outFile=open("Sandwich_Shop.txt","a")
    print("***Your sandwich order***")
    outFile.write(f"\nDate of order is {date_time}")
    for order in sandwhich_order:
        print(order)
        outFile.write(f"\n{order}")
    print("***End of order***")
    outFile.close()
    
#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection() #creating a variable that calls up the bread function and returns their choice
cheese_choice=cheese_selection()
meat_choice=meat_selection()
salad_choice=salad_selection()
dressing_choice=dressings_selection()
order=output_text_file()
print(first_name)
print(phone_number)

print(f"Your selected bread: {bread_choice}")
print(f"Your selected cheese: {cheese_choice}")
print(f"Your selected meat: {meat_choice}")
print(f"Your selected vegetables: {salad_choice}")
print(f"Your selected dressing: {dressing_choice}")
print(order)

