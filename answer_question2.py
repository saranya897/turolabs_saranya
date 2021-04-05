s1 = str(input("first string"))
s2 = str(input("seconda string"))
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
if s1 == s2:
    print("equal")
else:
    for i in s1:
        for j in s2:
            if j in special:
                j.replace(e)
                if s1[j] != s2[j]:
                    flag = 1
                    break
            if j in special:
                j.replace(f)
                if s1[j] != s2[j]:
                    flag = 1
                    break
    if flag == 0:
        print("match")

    # lst1 = []
    # lst2 = []
    # for i in s1:
    #     lst1.append(i)
    # for i in s2:
    #     lst2.append(i)
    # print(lst2, lst1)
