enemies = 1

def increment():
    # modify global variable
    global enemies
    enemies += 1
    print(enemies)

increment()