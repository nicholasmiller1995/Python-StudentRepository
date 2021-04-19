import socket
import sys
import json
import docx

sock = socket.create_connection(('localhost', 10000))


average = 0
search_score_start = 0
search_score_end = 0
search_exact_id = {}
Students =   {
                10 :   {
                        'Last Name' : 'Smith',
                        'First Name' : 'Adam',
                        'Score' : 88
                        },

                20 :   {
                        'Last Name' : 'Kennedy',
                        'First Name' : 'George',
                        'Score' : 78
                        },
                
                30 :   {
                        'Last Name' : 'Rio',
                        'First Name' : 'Nancy',
                        'Score' : 92
                        },
                
                40 :   {
                        'Last Name' : 'Henning',
                        'First Name' : 'Mary',
                        'Score' : 65
                        },
                
                50 :   {
                        'Last Name' : 'Rolling',
                        'First Name' : 'Karen',
                        'Score' : 90
                        },
                
                60 :   {
                        'Last Name' : 'Chen',
                        'First Name' : 'Nelson',
                        'Score' : 80
                         },

            }   


while True:
    print('--------------------------------------------')
    print("Socket Name: ",sock.family.name)
    print(' _______  __    _    __  __ ')
    print('| ____\ \/ /   / \  |  \/  |')
    print('|  _|  \  /   / _ \ | |\/| |')
    print('| |___ /  \  / ___ \| |  | |')
    print('|_____/_/\_\/_/   \_\_|  |_|')
    print(' ')
    choice = input(f'Which function would you like to do, Press 1-7 \n1 - Upload file to recive Student Information and Amount of Students:  \n2 - Statistics on Student Count in Database \n3 - Statistics on Average Student Scores in Database \n4 - Search for Users in Database using ID: \n5 - Search for Users in Database using Last Name: \n6 - Search for Users in Database using Score Range: \n7 - Quit \n--------------------------------------------\n\nInput:')

    #Upload file
    if choice == '1':
        location = input('Enter file location: ')
        try:
            doc = docx.Document(location)
            dictionary ={}
            all_paras = doc.paragraphs

            print("The number of students uploaded are",len(all_paras))
            for para in all_paras:
                line = para.text
                student_id, last_name, first_name, score = line.split(', ')
                dict_value = [last_name, first_name, int(score)]
                dictionary[int(student_id)] = dict_value

            for key, value in dictionary.items():
                print(key, ' : ', value)

            my_list = list(("upload", dictionary))
            my_json = json.dumps(my_list)
            sock.sendall(bytes(my_json, 'utf-8'))


            print('For Average Scores, input data into local client side database.\n\n')

        except:
            print('Enter a valid file location.\n\n')
    #Number of students
    elif choice == '2':
        count = len(Students.keys())

        print("The number of the Student is ", count, '\n\n' )

    #Avearge of all scores
    elif choice == '3':
        
        total_score = sum(t['Score'] for t in Students.values() if t)
        score_count = len(Students.values())
        average = total_score / score_count

        print("The average of the ovrall scores are ", average, '\n\n' )

    #ID Search
    elif choice == '4':
        
        search_exact_id = int(input("Enter the ID number: "))
    
        try:    
            info = str(Students[search_exact_id])
            print('')
            print('')
            print("Information for ID Numeber: " + str(search_exact_id) + " is ")
            print('---------------------------------------------------------------------')
            print('Id number is', search_exact_id)
            print('Information is', info, '\n\n')

        except:
            print('Enter a valid ID Number.\n\n')

    #Last Name Search
    elif choice == '5':
        
        search_exact_last_name = input("Enter the Last Name: ")

        try:
            list_values = [ key for key,val in Students.items() if val['Last Name']==(search_exact_last_name) ]
            list_val = sum(list_values)
            print('')
            print('')
            print("Information for Last Name: " + search_exact_last_name + " is " )
            print('---------------------------------------------------------------------')
            print('Id number is', list_values)
            print('Information is', str(Students[list_val]), '\n\n')

        except:
            print('Enter a valid Last Name.\n\n')
            
    #Range Button
    elif choice == '6':
        
        search_score_start = int(input("Enter the Starting Score Range: ")) 
        search_score_end = int(input("Enter the Ending Score Range: "))

        dict_temp = []
        temp = 'Score'
        res = [val[temp] for key, val in Students.items() if temp in val]
            

        print ("Scores in your range is: ")
        for n in res:
            if n >= search_score_start and n <= search_score_end:
                dict_temp.append(n)
                print (n)
        print('\n')
        

    elif choice == '7':
        break
    
    #Statement if a Number outside 1-6 is used
    else:
        print('Please select from options above.')




