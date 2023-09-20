import random

def RSP0(player):
    computer = random.choice(['가위', '바위', '보'])
    if computer == '가위':
        print('컴퓨터는 가위를 냈습니다.')
        if player == '가위':
            print('플레이어는 가위를 냈습니다.')
            print('무승부')
        elif player == '바위':
            print('플레이어는 바위를 냈습니다.')
            print('플레이어 승리')   
        elif player == '보':
            print('플레이어는 보를 냈습니다.')
            print('컴퓨터 승리')
    elif computer == '바위':
        print('컴퓨터는 바위를 냈습니다.')
        if player == '가위':
            print('플레이어는 가위를 냈습니다.')
            print('컴퓨터 승리')
        elif player == '바위':
            print('플레이어는 바위를 냈습니다.')
            print('무승부')
        elif player == '보':
            print('플레이어는 보를 냈습니다.')
            print('플레이어 승리')
    elif computer == '보':
        print('컴퓨터는 보를 냈습니다.')
        if player == '가위':
            print('플레이어는 가위를 냈습니다.')
            print('플레이어 승리')
        elif player == '바위':
            print('플레이어는 바위를 냈습니다.')
            print('컴퓨터 승리') 
        elif player == '보':
            print('플레이어는 보를 냈습니다.')
            print('무승부')
            
def RSP_repeat():
    player == '보'
    while player == '가위' or '바위' or '보':
        player = input('다시 시작하려면 가위 바위 보 중 하나를 입력하세요.:')
        print('\n')
        print(player)
        if player == '가위' or '바위' or '보':
            RSP0(player)
        else: quit()
        
print('가위 바위 보 게임')
print('가위 바위 보를 하는 게임 입니다.')
computer = random.choice(['가위', '바위', '보'])
player = input('가위 바위 보 중 하나를 입력하세요: ')
RSP0(player)
RSP_repeat()
