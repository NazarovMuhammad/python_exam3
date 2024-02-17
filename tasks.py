### 1 Question
# Write a program to determine whether a given year is a leap year 
# Напишите программу, чтобы определить, является ли данный год високосным 
# Барномаи нависед, то муайян кунед, ки соли додашуда соли кабиса аст.










# ### 2 Question
# Given a string consisting of words separated by spaces. Determine how many words there are in it. 
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. 
# Сатре дода мешавад, ки аз калимаҳои бо фосила ҷудошуда иборат аст. Муайян кунед, ки дар он чанд калима мавҷуд аст. 

    # a = input()
    # cnt = 1
    # for i in a:
    #     if i == " ":
    #         cnt+=1
            
# print(cnt) 










# ### 3 Question
# Write program to print yesterday, today, tomorrow / Напишите программу для печати вчера, сегодня, завтра. 
# Барномаи нависед, то дирӯз, имрӯз, фардоро чоп куна

    # from datetime import datetime,timedelta
    # a = datetime.now()
    # b = timedelta(days=+1)
    # c = timedelta(days=-1)
    # print(a)
    # print(a+c)
    # print(a+b)










# ### 4 Question
# Write a program to subtract five days from the current date 
# Напишите программу, которая вычитает пять дней из текущей даты.
# ```
# Input: 17.02.2024
# Output: 12.02.2024


    # from datetime import datetime,timedelta
    # a = datetime.now()
    # b = timedelta(days=-5)
    
    # print(a)
    # print(a+b)









# ### 7 Question
# Write a program to read the first n lines of a file 
# # Напишите программу для чтения первых n строк файла
    # n = int(input())
    # with open("teext.txt", "r") as f:
    #     for i in range(n):     
    #         print(f.readline())
    







a = input().split()
c = "9999"
d = "0"
for i in a:
    if i < c:
        c = i  
        continue 
    if i > d:
        d = i
    
print(abs(int(c)-int(d)))  
   
           
    