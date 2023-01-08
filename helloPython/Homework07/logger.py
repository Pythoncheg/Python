import model

def write_data(value):
    with open("helloPython/Homework07/base.txt", 'a') as file1:
        file1.write(value)
        file1.write('\n')
    with open("helloPython/Homework07/base.scv", 'a') as file2:
        file2.write(value)
        file2.write('\n')