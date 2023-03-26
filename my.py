import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        
        
condition =True
while(condition):
    student_info = input("enter student information in following format(name age contact number email id :")
    print("entered information"+student_info)
    
    #split
    student_info_list=student_info.split(' ')
    print("entered split up information is"+str(student_info_list))
    
    write_into_csv(student_info_list)
    condition_check=input("enter yes or no")
    if condition_check =="yes":
        condition=True
    elif condition_check=="no":
        condition=False
    
    
