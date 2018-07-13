
跳舞人生
—

friends = hero.findFriends()
friend = hero.findNearest(friends)

x = friend.pos.x
y = friend.pos.y
while True:
    off_x = friend.pos.x - x 
    off_y = friend.pos.y - y 
    x = friend.pos.x
    y = friend.pos.y
    
    hero.move({'x':hero.pos.x+off_x,'y':hero.pos.y+off_y})
