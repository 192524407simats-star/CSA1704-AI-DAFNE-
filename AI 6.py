room = {'A': 1, 'B': 1}
position = 'A'

while 1 in room.values():
    if room[position] == 1:
        print(position, "is dirty. Cleaning...")
        room[position] = 0
    else:
        print(position, "is clean.")

    position = 'B' if position == 'A' else 'A'

print("Both rooms are clean.")