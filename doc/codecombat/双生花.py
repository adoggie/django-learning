

# 如果花匠受伤了,双生花会缩小！

def summonSoldiers():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")

# 定义函数:commandSoldiers
def commandSoldiers():
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == 'soldier':
            enemy = friend.findNearestEnemy()
            if enemy:
                hero.command(friend,'attack',enemy)
    
# 定义函数:pickUpNearestCoin
def pickUpNearestCoin():
    
    coin = hero.findNearestItem()
    if coin:
        # hero.command(peasant,'move',coin.pos)
        hero.moveXY(coin.pos.x,coin.pos.y)

peasant = hero.findByType("peasant",hero.findFriends())[0]
while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()
