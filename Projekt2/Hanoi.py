'''====================== '''
#                 Class
'''====================== '''

class hanoi:

    def __init__(self):
        self.tower_A = []
        self.tower_B = []
        self.tower_C = []
        self.tower_start = []
        self.number_disc = 3
        self.start(self.number_disc)

    def start(self, number_disc):
        number_disc = range(self.number_disc)

        for i in number_disc:
            self.tower_A.append(i+1)
            self.tower_start.append(i+1)

        self.tower_A.reverse()
        self.tower_start.reverse()

        self.print_state()

        self.run()

    def run(self):

        while True:
            self.move()
            if self.tower_C == self.tower_start:
                print('#########')
                print('You Won!')
                print('#########\n')
                break
            self.print_state()

    def move(self):

        frm, to = self.user_input()

        frm,to = self.conv_alpha2tower(frm,to)

        rule_check =self.check_rules(frm, to)

        if rule_check:
             to.append(frm.pop())


    def check_rules(self,frm, to):

        if frm:
            # From rod is not empty
            if to:
                # To rod is not empty
                if frm[-1]  < to[-1]:
                    return True
                else:
                    self.print_error('Wrong move')

            else:
                    return True

        else:
            self.print_error('Wrong move')

    def print_error(self, txt):
        print(txt)

    def conv_alpha2tower(self,frm,to):

        if frm == 'A':
             frm = self.tower_A

        if frm == 'B':
            frm = self.tower_B

        if frm == 'C':
            frm = self.tower_C

        if to == 'A':
            to = self.tower_A

        if to == 'B':
            to = self.tower_B

        if to == 'C':
            to = self.tower_C

        return frm, to

    def user_input(self):

        while True:
            print('------------------------------------------------------------------------------')
            frm = input('From which rod should the next disc be moved?\n')
            check_input = self.check_input(frm)
            if check_input:
                to = input('To which rod should the disc be moved?\n')
                print('------------------------------------------------------------------------------')
                check_input = self.check_input(to)
                if check_input:
                    break

        return frm, to

    def check_input(self, inp):
        rod = ['A', 'B', 'C']
        if inp == 'esc':
            exit()

        if inp in rod:
            return True
        else:
            print('Invalid input! Please try again...')

    def print_state(self):
        print('#########\n')
        print(self.tower_A)
        print(self.tower_B)
        print(self.tower_C)
        print('#########\n')

x=hanoi()


