'''
Health Management System:
You have 3 clients named: Harry, Rohan and Hammad. You have to manage what they are eating and what they are exercising.
Total 6 files you have to make 3 to manage their food and 3 to manage their exercise.
1 . first enter the choice if you want to view the file or you want to enter new entries in the file
2 . Select the client
3. Select if you want to enter for exercise or for diet.
'''


def getdate():
    """This function gives the current date and time

    Returns:
        current_time: What is the current date and time.time
    """
    import datetime
    current_time = datetime.datetime.now()
    return current_time


def view_harry_exercise():
    file_1 = open("harry_exercise.txt", 'rt')
    content = file_1.read()
    print(content)
    file_1.close()


def view_harry_diet():
    file_1 = open("harry_diet.txt", 'rt')
    content = file_1.read()
    print(content)
    file_1.close()


def view_rohan_exercise():
    file_1 = open("rohan_exercise.txt", 'rt')
    content = file_1.read()
    print(content)
    file_1.close()


def view_rohan_diet():
    file_1 = open('rohan_diet.txt', 'rt')
    content = file_1.read()
    print(content)
    file_1.close()


def view_hamad_exercise():
    file_1 = open("hamad_exercise.txt", 'rt')
    content = file_1.read()
    print(content)
    file_1.close()


def view_hamad_diet():
    file_1 = open('hamad_diet.txt', 'rt')
    content = file_1.read()
    print(content)
    file_1.close()


def edit_harry_exercise():
    file_1 = open('harry_exercise.txt', 'a')
    content = input('enter the exercise performed: ')
    file_1.write('[' + str(getdate()) + ']' + content + '\n')
    file_1.close()


def edit_harry_diet():
    file_1 = open('harry_diet.txt', 'a')
    content = input('enter the diet eaten: ')
    file_1.write('[' + str(getdate()) + ']' + content + '\n')
    file_1.close()


def edit_rohan_exercise():
    file_1 = open('rohan_exercise.txt', 'a')
    content = input('enter the exercise performed: ')
    file_1.write('[' + str(getdate()) + ']' + content + '\n')
    file_1.close()


def edit_rohan_diet():
    file_1 = open('rohan_diet.txt', 'a')
    content = input('enter the diet eaten: ')
    file_1.write('[' + str(getdate()) + ']' + content + '\n')
    file_1.close()


def edit_hamad_exercise():
    file_1 = open('hamad_exercise.txt', 'a')
    content = input('enter the exercise performed: ')
    file_1.write('[' + str(getdate()) + ']' + content + '\n')
    file_1.close()


def edit_hamad_diet():
    file_1 = open('hamad_diet.txt', 'a')
    content = input('enter the diet eaten: ')
    file_1.write('[' + str(getdate()) + ']' + content + '\n')
    file_1.close()


while True:
    first_choice_option = int(input(
        "Enter 1 if you want to view the files or enter 0 to enter the new entries. :"))
    second_choice_option = int(input(
        "Enter the respective key to for particular client.\n1 for Harry.\n2 for Rohan.\n3 for Hamad. :"))
    third_choice_option = int(input(
        "Enter 1 for the exercise and enter 0 for the diet. :"))

    if first_choice_option == 1:  # View the files
        if second_choice_option == 1:  # Harry

            if third_choice_option == 1:  # exercise
                view_harry_exercise()
            elif third_choice_option == 0:  # diet
                view_harry_diet()
            else:  # Wrong choice
                print("wrong input")

        elif second_choice_option == 2:  # Rohan

            if third_choice_option == 1:  # exercise
                view_rohan_exercise()
            elif third_choice_option == 0:  # diet
                view_rohan_diet()
            else:  # Wrong choice
                print("wrong input")

        elif second_choice_option == 3:  # Hamad

            if third_choice_option == 1:  # exercise
                view_hamad_exercise()
            elif third_choice_option == 0:  # diet
                view_hamad_diet()
            else:  # Wrong choice
                print("wrong input")

        else:  # Wrong choice
            print("wrong input")

    elif first_choice_option == 0:  # Edit the files

        if second_choice_option == 1:  # Harry

            if third_choice_option == 1:  # exercise
                edit_harry_exercise()
            elif third_choice_option == 0:  # diet
                edit_harry_diet()
            else:  # Wrong choice
                print("wrong input")

        elif second_choice_option == 2:  # Rohan

            if third_choice_option == 1:  # exercise
                edit_rohan_exercise()
            elif third_choice_option == 0:  # diet
                edit_rohan_diet()
            else:  # Wrong choice
                print("wrong input")

        elif second_choice_option == 3:  # Hamad
            if third_choice_option == 1:  # exercise
                edit_hamad_exercise()
            elif third_choice_option == 0:  # diet
                edit_hamad_diet()
            else:  # Wrong choice
                print("wrong input")

        else:  # Wrong choice
            print("wrong input")

    else:  # Wrong choice
        print("wrong input")
