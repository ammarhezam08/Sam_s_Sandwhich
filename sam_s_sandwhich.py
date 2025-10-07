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

def bread_selection():
    bread_list=["White","Brown","Italian","Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list[count])
        count +=1
    bread_selected=int(input("Which bread did you want? Enter a number: "))
    return bread_list[bread_selected-1] #returns back a string

def cheese_selection():
    cheese_list=["Cheddar","Mozarrella","Feta","Gouda"]
    count=0
    print("We have the following types of cheese:")
    while count < len(cheese_list):
        print(count+1," ",cheese_list[count])
        count +=1
    cheese_selected=int(input("Which type of cheese did you choose? Enter a number: "))
    return cheese_list[cheese_selected-1]

def meat_selection():
    meats_list=["Beef","Chicken","Goat","Lamb"]
    count=0
    print("We have the following types of meats:")
    while count < len(meats_list):
        print(count+1," ",meats_list[count])
        count +=1
    meat_selected=int(input("Which type of meat did you choose? Enter a number: "))
    return meats_list[meat_selected-1]

def salad_selection():
    vegetable_list=["Lettuce","Tomato","Cucumber","Onions"]
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
    
#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection() #creating a variable that calls up the bread function and returns their choice
cheese_choice=cheese_selection()
meat_choice=meat_selection()
salad_choice=salad_selection()
first_name = force_name("Enter your first name")
print(f"Your selected bread: {bread_choice}")
print(f"Your selected cheese: {cheese_choice}")
print(f"Your selected meat: {meat_choice}")
print(f"Your selected vegetables: {salad_choice}")