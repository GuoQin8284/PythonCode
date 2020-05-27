class Show_welcomeinfo(object):
    top_score=0
    @classmethod
    def show_topscore(cls,name):
        print("当前游戏最高分：",cls.top_score)
        print("获得最高分的玩家是：",name)
    def play_game(self,score):
        self.score=score
        if self.score>Show_welcomeinfo.top_score:
            Show_welcomeinfo.top_score=self.score
class Perction(object):
    def __init__(self,name):
        self.name=name

xiaoming=Perction("小明")
game=Show_welcomeinfo()

Show_welcomeinfo.show_topscore(xiaoming.name)


