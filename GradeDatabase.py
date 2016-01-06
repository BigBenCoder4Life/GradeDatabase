# GradeDatabase.py
'''
Created on Dec 5, 2014
@author: Ben Kirtley
'''
def main():
    global list
    global sorted_list
    file_name = raw_input("Enter the file name:")
    option = ""
    list = parse_file(file_name)
    while option.upper() != 'X':
        option = menu()
           
def parse_file(file_name):
    return [int(line.strip()) for line in open(file_name)]       
                
def print_grades(list):
    for grade in list:
        print grade
        
def get_avg():
    total = 0
    for grade in list:
        total += grade    
    avg = total / len(list)
    return avg
    
def get_highest_grade():
    highest = 0
    for grade in list:
        if grade > highest:
            highest = grade
    return highest
           
def get_lowest_grade():
    lowest = list[0]
    for grade in list:
        if grade <= lowest:
            lowest = grade
    return lowest

def grade_overview():
    print 'Grade Overview'
    print 'Total grades: '  + str(len(list))
    print 'Average grade: ' + str(get_avg()) 
    print 'Highest grade: ' + str(get_highest_grade());
    print 'Lowest grade: '  + str(get_lowest_grade());
    
def sort_grades():
    sorted_list = list[:]
    sorted_list.sort()
    sorted_list.reverse()
    print_grades(sorted_list)
    save_file = open('sorted_grades.txt', 'w')
    for item in sorted_list:
        save_file.writelines("{}\n".format(item))
    save_file.close()
        
def menu():
    print  'A) Show all grades'
    print  'B) Get class average'
    print  'C) Get highest grade'
    print  'D) Get lowest grade'
    print  'E) Grade overview'    
    print  'F) Sort grades'
    print  'X) Exit the program'
    option = raw_input('Choose an option (A, B, C, D, E, F, or X):').upper()   
       
    if option == 'A':
        print_grades(list)
    elif option == 'B':
        print 'Average grade: ' + str(get_avg())
    elif option == 'C':
        print 'Highest grade: ' + str(get_highest_grade());
    elif option == 'D':
        print 'Lowest grade: '  + str(get_lowest_grade());
    elif option == 'E':
        grade_overview()
    elif option == 'F':
        sort_grades()
    elif option == 'X':
        return option
    else:
        print 'Invalid option. Please try again!' 
        return option
    
    return option

if __name__ == '__main__':
    main()  