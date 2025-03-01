
name1 = input("Enter your name: ");
name2 = input("Enter your partner name: ");

arr1 = list(name1);
arr2 = list(name2);

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr1[i] == arr2[j]):
            arr1[i] = 0;
            arr2[j] = 0;
            break;

namearr = arr1 + arr2;

relation = 0;
for i in namearr:
    if(i != 0):
        relation = relation + 1;
print(relation);

flames = ['f', 'l', 'a', 'm', 'e', 's'];
count = 0;
while(len(flames) >= 1):
    if(len(flames) == 1):
        print(flames);
        print("terminate");
        break;
    else:
        for j in range( len(flames) ):
            count = count + 1;
            if(count == relation):
                flames = flames[j:] + flames[:j];
                del flames[0];
                count = 0;
                break;
