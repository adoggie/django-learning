

# 你必须护送一个强大的魔戒回城研究。
# 我们的目标是要逃脱，不是打仗。有更多食人魔潜伏在周围的山脉！
# 让士兵把农民围在里面！
# 我们给你两个函数来帮助你：

# 
# 第一个参数'士兵'应该是你的士兵阵列。
# 
def findSoldierOffset(soldiers, i):
    soldier = soldiers[i]
    angle = i * 360 / len(soldiers)
    return radialToCartesian(5, angle)

# 这个函数做数学运算来确定一个战士应该站的位置。
def radialToCartesian(radius, degrees):
    radians = Math.PI / 180 * degrees
    xOffset = radius * Math.cos(radians)
    yOffset = radius * Math.sin(radians)
    return {"x": xOffset, "y": yOffset}

peasant = hero.findByType("peasant")[0]

# Use findByType to get an array of your soldiers.
while True:
    # 
    soldiers = hero.findByType("soldier")
    # 找到士兵的位置。
    index = 0 
    while index < len(soldiers):
        pos = findSoldierOffset(soldiers,index)
        soldier = soldiers[index]
        newpos = {'x':pos['x']+peasant.pos.x,'y':pos['y']+peasant.pos.y}
        hero.command( soldier ,'move',newpos )
        index+=1
    # Add the offset.x and offset.y to the peasant's pos.x and pos.y

    # 命令士兵移动到新位置。

    # 英雄应跟上农民！
    hero.move({"x": hero.pos.x + 0.2, "y": hero.pos.y})
