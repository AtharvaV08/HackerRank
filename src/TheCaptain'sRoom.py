k = int(input())
k_grp_size = list(map(int, input().split()))
sorted_k_grp_size = sorted(k_grp_size)

unique_room_no = set() # unique room no. list
room_appear_twice = set() # room no. which appear more than once
                                                        # QUESTIONS TO ASK
for captains_room in sorted_k_grp_size:                 # HOW DOES THIS LOOP WORK
    if captains_room in unique_room_no:
        room_appear_twice.add(captains_room)
    else:
        unique_room_no.add(captains_room)

captains_room_no = unique_room_no.difference(room_appear_twice)
print(*captains_room_no)                        # '*' is used to unpack any iterable eg: set, list, str
                                                # and print the no or name on the same line using space
                                                # with * eg: 1 2 3
                                                # without * eg: {1, 2, 3}