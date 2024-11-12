if __name__ == '__main__':
    list = []
    dict_values = {}
    for i in range(int(input())):
        name = input()
        score = float(input())
        list.append((name,score))
        dict_values[name] = score
    
    marks = sorted(set([i for i in dict_values.values()]))
    for y in range(2):
        uni_mark = marks[y]
        namelist = [student[0] for student in list if student[1] == uni_mark]
        print(namelist)

    
    
