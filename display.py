

def add_time(arr, val):
    if val == '0' :
        arr[0]+="+---+"
        arr[1]+="|   |"
        arr[2]+="|   |"
        arr[3]+="+   +"
        arr[4]+="|   |"
        arr[5]+="|   |"
        arr[6]+="+---+"
    
    elif val == '1' :
        arr[0]+="    +"
        arr[1]+="    |"
        arr[2]+="    |"
        arr[3]+="    +"
        arr[4]+="    |"
        arr[5]+="    |"
        arr[6]+="    +"
    
    if val == '2' :
        arr[0]+="+---+"
        arr[1]+="    |"
        arr[2]+="    |"
        arr[3]+="+---+"
        arr[4]+="|    "
        arr[5]+="|    "
        arr[6]+="+---+"
    
    if val == '3' :
        arr[0]+="+---+"
        arr[1]+="    |"
        arr[2]+="    |"
        arr[3]+="+---+"
        arr[4]+="    |"
        arr[5]+="    |"
        arr[6]+="+---+"
    
    if val == '4' :
        arr[0]+="+   +"
        arr[1]+="|   |"
        arr[2]+="|   |"
        arr[3]+="+---+"
        arr[4]+="    |"
        arr[5]+="    |"
        arr[6]+="    +"
    
    if val == '5' :
        arr[0]+="+---+"
        arr[1]+="|    "
        arr[2]+="|    "
        arr[3]+="+---+"
        arr[4]+="    |"
        arr[5]+="    |"
        arr[6]+="+---+"
    
    if val == '6' :
        arr[0]+="+---+"
        arr[1]+="|    "
        arr[2]+="|    "
        arr[3]+="+---+"
        arr[4]+="|   |"
        arr[5]+="|   |"
        arr[6]+="+---+"
    
    if val == '7' :
        arr[0]+="+---+"
        arr[1]+="    |"
        arr[2]+="    |"
        arr[3]+="    +"
        arr[4]+="    |"
        arr[5]+="    |"
        arr[6]+="    +"
    
    if val == '8' :
        arr[0]+="+---+"
        arr[1]+="|   |"
        arr[2]+="|   |"
        arr[3]+="+---+"
        arr[4]+="|   |"
        arr[5]+="|   |"
        arr[6]+="+---+"
        
    if val == '9' :
        arr[0]+="+---+"
        arr[1]+="|   |"
        arr[2]+="|   |"
        arr[3]+="+---+"
        arr[4]+="    |"
        arr[5]+="    |"
        arr[6]+="+---+"
    
    if val == ':' :
        arr[0]+=" "
        arr[1]+=" "
        arr[2]+="o"
        arr[3]+=" "
        arr[4]+="o"
        arr[5]+=" "
        arr[6]+=" "
    

while True:
    line = input()

    if line == "end":
        break
    arr = [""]*7
    for i in line:
        add_time(arr,i)
        for j in range(len(arr)):
            arr[j] += "  "

    for j in range(len(arr)):
        arr[j] = arr[j][:-2]

    for i in arr:
        print(i)
    print("\n")

print("end")