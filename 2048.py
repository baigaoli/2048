# -- coding: utf-8 --
import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

def main(stdscr):
    def init():
        #重置游戏棋盘
        return "Game"

    def not_game(state):
        #画出Game Over 或Win 的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda : state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]
    def game():
        #画出当前棋盘状态
        读取用户输入得到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步
            if 游戏胜利了:
            return 'Win'
            if 游戏失败了:
            return 'Gameover'
        return 'Game'

    state_actions = {
        'Init' : init,
        'Win' : lambda : not_game('Win'),
        'Gameover' : lambda : not_game('Gameover'),
        'Game' : game
    }

    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

#阻塞+循环，直到获得用户有效输入才返回对应行为
def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

#矩阵转置
def transpose(field):
    return [list(row) for row in zip(*field)]
#矩阵逆转
def invert(field):
    return [row[::-1] for row in field]

#创建棋盘
class GameField(object):
    def __init__(self, height = 4, width = 4, win = 2048):
        self.height = height #高
        self.width = width #宽
        self.win_value = 2048 #过关分数
        self.score = 0 #当前分数
        self.highscore = 0 #最高分
        self.reset() #棋盘重置


#随机生成一个2或者4
def spawn(self):
    new_element = 4 if randrange(100) > 89 else 2
    (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
    self.field[i][j] = new_element

#重置棋盘
def reset(self):
    if self.score > self.highscore:
        self.highscore = self.score
    self.score = 0
    self.field = [[0 for i in range(self.width)] for j in range(self.height)]
    self.spawn()
    self.spawn()

#一行向左合并
def move_row_left(row):
    def tighten(row): #把零散的非零单元挤到一块
        new_row = [i for i in row if i != 0]
        new_row += [0 for i in range(len(row) - len(new_row))]
        return new_row
    def merge(row): #对邻近元素进行合并
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.append(2 * row[i])
                self.score += 2 * row[i]
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                    new_row.append(0)
                else:
                    new_row.append(row[i])
        assert len(new_row) == len(row)
        return new_row
    #先挤到一块再合并到一块
    return tighten(merge(tighten(row)))