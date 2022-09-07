print('press 1 :list \n press 2:set\n press 3:tuple\n press 4: dictionary\n press 5: exit')
ch=int(input("enter your choice\n"))
if ch==1:
    print('enter elements of your list')
    l1=list(eval(input()))
    print('your list is \n',l1)
    print('choice for list operations are \n press 1: add single elemnt \n press 2: delete a specific element by index value\n press 3: to remove list')
    ch1=int(input(' enter your choice for list operation : '))
    if ch1==1:
        print('enter the element yo want to add')
        l1.append(input())
        print(l1)
    elif ch1==2:
        print('enter index value of element you want to remove')
        l1.pop(int(input()))
        print(l1)
    elif ch1==3:
        l1.clear()
        print('now your list is empty')
    else:
        print('wrong')
        
elif ch==2:
    print('enter the elements in set')
    s1=set(eval(input('enter elements you want to add')))
    s2=set(eval(input('enter elements you want to add')))
    print('your set is \n', s1)
    print('your set is \n', s2)
    print('press 1: add single element\n press 2: discard element\n press 3:union of set\n press 4: intersection of set\n press 5:difference\n press 6: symmetric difference ')
    ch2=int(input('enter your choice for set operations\n '))
    if ch2==1:
        print('enter element which you want to add')
        t1.add(input())
        print(t1)
    elif ch2==2:
        print('enter the element which you want to discard')
        t1.remove(input())
        print(t1)
    elif ch2==3:
        print('union of sets are' ,s1|s2)
    elif ch2==4:
        print('intersection of sets are', s1&s2)
    elif ch2==5:
        print('after removing common elements output from s1 is',s1-s2)
    else:
        print('after removing common elements union of set is',s1^s2)
elif ch==3:
    t1=tuple(eval(input('enter values for tuple: ')))
    print(t1)
    print('press \n 1: for addition\npress 2: for deletion')
    ch3=int(input('enter number of your choice: '))
    if ch3==1:
        print('tuple is immutable so we have to convert it into list')
        l1=list(t1)
        l1.append(int(input('enter value you wnat to add\n')))
        t1=tuple(l1)
        print('your updated tuple is', t1)
    elif ch3==2:
        print('for deletion \n press 1: by value\n press 2: by index value\n press 3: clear all elements')
        ch3_1=int(input('enter your choice\n'))
        if ch3_1==1:
            l1=list(t1)
            l1.remove(int(input('enter value you want to remove\n')))
            t1=tuple(l1)
            print(t1)
        elif ch3_1==2:
            l1=list(t1)
            l1.pop(int(input('enter index value you want to remove\n')))
            t1=tuple(l1)
            print(t1)
        else:
            l1=list(t1)
            l1.clear(int(input(' remove all elemnts\n')))
            t1=tuple(l1)
            print(t1)
elif ch==4:
    a=int(input('enter no of key value pairs: '))
    b=dict(input('enter a key and value: ').split()for i in range(a))
    print(b)
    print('press 1: For addition\n press 2: To access elements\n press 3: To delete')
    ch4_1=int(input('enter your choice for dictionary operations\n'))
    if ch4_1==1:
        #for i in range (1,n):
            key=input('enter key: ')
            value=input('enter value: ')
            b[key]=value
            print('your dictionary is',b)
    elif ch4_1==2:
        print('types for accessing data are\n press 1: or keys\n press 2: for values\n press 3: for all value and key')
        ch4_1_1=int(input('enter your choice to access: '))
        if ch4_1_1==1:
            print(b.keys())
        elif ch4_1_1==2:
            print(b.values())
        else:
            print(b.items())
    else:
        b.popitem()
        print(b)
else:
    print('exit')





