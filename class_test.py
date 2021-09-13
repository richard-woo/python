class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, aggressivity, life_value, money):
        self.name = name  # 每一个角色都有自己的昵称;
        self.aggressivity = aggressivity  # 每一个角色都有自己的攻击力;
        self.life_value = life_value  # 每一个角色都有自己的生命值;
        self.money = money

    def attack(self,dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.aggressivity


class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性都是狗

    def __init__(self, name, breed, aggressivity, life_value):
        self.name = name  # 每一只狗都有自己的昵称;
        self.breed = breed  # 每一只狗都有自己的品种;
        self.aggressivity = aggressivity  # 每一只狗都有自己的攻击力;
        self.life_value = life_value  # 每一只狗都有自己的生命值;

    def bite(self,people):
        # 狗可以咬人，这里的狗也是一个对象。
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
        people.life_value -= self.aggressivity

class Weapon:
    def __init__(self,name, price, aggrev, life_value):
        self.name = name
        self.price = price
        self.aggrev = aggrev
        self.life_value = life_value

    def update(self, obj):  #obj就是要带这个装备的人
        obj.money -= self.price  # 用这个武器的人花钱买所以对应的钱要减少
        obj.aggressivity += self.aggrev  # 带上这个装备可以让人增加攻击
        obj.life_value += self.life_value  # 带上这个装备可以让人增加生命值

    def prick(self, obj):  # 这是该装备的主动技能,扎死对方
        obj.life_value -= 500  # 假设攻击力是500

lance = Weapon('长矛',200,6,100)
egg = Person('egon',10,1000,600)  #创造了一个实实在在的人egg
ha2 = Dog('二愣子','哈士奇',10,1000)  #创造了一只实实在在的狗ha2

#egg独自力战"二愣子"深感吃力，决定穷毕生积蓄买一把武器
if egg.money > lance.price: #如果egg的钱比装备的价格多，可以买一把长矛
    lance.update(egg) #egg花钱买了一个长矛防身，且自身属性得到了提高
    egg.weaponn = lance #egg装备上了长矛

print(egg.money,egg.life_value,egg.aggressivity)

print(ha2.life_value)
egg.attack(ha2)   #egg打了ha2一下
print(ha2.life_value)
egg.weaponn.prick(ha2) #发动武器技能
print(ha2.life_value) #ha2不敌狡猾的人类用武器取胜，血槽空了一半