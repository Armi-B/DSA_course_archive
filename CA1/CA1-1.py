sequence = list(input())
states_rep = [0] * 1024
states_rep[0] = 1
flip = [1, 0]
current = [0,0,0,0,0,0,0,0,0,0]
ans = 0

def list_to_dec( list : list ):
    result = 0
    for i in range(len(list)):
        result += list[i] * (2 ** i)
    return result


for i in sequence:
    current[ord(i)- 97] = flip[current[ord(i)- 97]]
    ans += states_rep[list_to_dec(current)]
    for k in range(10):
        temp = current.copy()
        temp[k] = flip[temp[k]]
        ans += states_rep[list_to_dec(temp)]
    states_rep[list_to_dec(current)] += 1
    
print(ans)
    
    