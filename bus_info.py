class Bus:
    # 초기화
    def __init__(self, number, where):
        # self.__number = number
        self.__number = number
        self.where = where

    #버스의 정보 보여주기
    def show_info(self):
        print('{}행 {}번 버스'.format(self.where, self.__number))

    # 버스 요금
    def fee(self, money):
        self.money = money

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

b1 = Bus("100", "강남")
b2 = Bus("200", "서초")
b3 = Bus("300", "양재")


def turn_on():
    print('= 버스정보 알림 시스템입니다 =')
    while True:
        choice = int(input('\n<메뉴를 선택하세요>\n1: 목적지 선택\n2: 버스 번호 선택\n0: 종료\n\n입력 : '))
        if choice == 0:
            break
        elif choice == 1:
            while True:
                choice2 = int(input('목적지를 선택하세요\n\n1: 강남\n2: 서초\n3: 양재\n0: 뒤로가기\n\n입력 : '))
                if choice2 == 1:
                    b1.show_info()
                elif choice2 == 2:
                    b2.show_info()
                elif choice2 == 3:
                    b3.show_info()
                elif choice2 == 0:
                    break
                else:
                    print('다시 입력하세요')
                print('-----------------------')
        elif choice == 2:
            while True:
                choice2 = int(input('\n<버스 번호를 선택하세요>\n1: 100번 버스\n2: 200번 버스\n3: 300번 버스\n0: 뒤로가기\n\n입력 : '))
                if choice2 == 1:
                    b1.show_info()
                elif choice2 == 2:
                    b2.show_info()
                elif choice2 == 3:
                    b3.show_info()
                elif choice2 == 0:
                    break
                else:
                    print('다시 입력하세요')
                print('-----------------------')
        else:
            print('다시 입력하세요')
        print('-----------------------')
    print('= 종료 =')

if __name__ == '__main__':
    turn_on()