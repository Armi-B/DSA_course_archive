num_tst = int(input())
for _ in range(num_tst):
    rec_time = input()
    h, m, noon = rec_time.replace(':',' ').split()
    h = int(h)
    m = int(m)
    if noon == "PM" and int(h) < 12:
        h = h + 12
    if noon == "AM" and int(h) >= 12:
        h = h - 12
    num_friends = int(input())
    friends_state = ""
    for i in range(num_friends):
        friend_time = input()
        s_h, s_m, s_noon, e_h, e_m, e_noon = friend_time.replace(':',' ').split()
        s_h = int(s_h)
        e_h = int(e_h)
        if s_noon == "PM" and int(s_h) < 12:
            s_h = s_h + 12
        if e_noon == "PM" and int(e_h) < 12:
            e_h = e_h + 12
        if s_noon == "AM" and int(s_h) >= 12:
            s_h = s_h - 12
        if e_noon == "AM" and int(e_h) >= 12:
            e_h = e_h - 12
        s_time_matched = (s_h < h or (s_h == h and int(s_m) <= m))
        e_time_matched = (e_h > h or (e_h == h and int(e_m) >= m))
        if (s_h < h or (s_h == h and int(s_m) <= m)) and (e_h > h or (e_h == h and int(e_m) >= m)):
            friends_state += "1"
        else:
            friends_state += "0"
    print(friends_state)