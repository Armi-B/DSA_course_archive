sequence = input()
flag = False
total_num_digits = len(sequence)
for f in range(1,(total_num_digits // 2 + 1)):
    a1 = int (sequence[ 0 : f ])
    for s in range(1,(total_num_digits// 2 + 1)):
        if flag or (( f + s + max(f, s)) > total_num_digits):
            break
        a2 = int(sequence[ f : f + s ])
        a3 = a1 + a2
        ind = sequence[f + s: ].find(str(a3))
        if ind == 0:
            new_seq = sequence[f + s + len(str(a3)): ]
            new_a1 = sequence[ f : f + s ]
            new_a2 = a3
            flag = True
            while(len(new_seq) != 0):
                #حلقه را تا زمان خالی شدن متغییر ادامه میدهیم.
                new_a3 = str(int(new_a1) + int(new_a2))
                if new_seq.find( new_a3 ) == 0:
                    #بخش هایی را که قبول میشوند از رشته جدا میکنیم.
                    new_seq = new_seq[len(str(new_a3)): ]
                    new_a1 = new_a2
                    new_a2 = new_a3
                else:
                    flag = False
                    break
            if flag:
                break 
    if flag:
        print("YES")
        break
if not flag: 
    print("NO")
