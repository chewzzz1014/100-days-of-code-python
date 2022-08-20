# nested list

map = [['⬜️', '⬜️', '⬜️'],
       ['⬜️', '⬜️', '⬜️'],
       ['⬜️', '⬜️', '⬜️']]

coor = int(input("Enter location in the format [column][row]: "))

# map[row][column]
map[int(coor%10)-1][int(coor/10)-1] = 'X'

for i in map:
    print(i)