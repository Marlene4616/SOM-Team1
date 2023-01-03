#!/usr/bin/env python3

class Hanoi_towers(object):
    '''this class tries to simulate the game of the towers of hanoi in a simplified way'''
    def __init__(self, render):
        """Declare some variables"""
        self.A = [3, 2, 1]
        self.B = []
        self.C = []

        '''Diese Funktion sollte eingeschaltet werden, wenn ein Mensch das Spiel spielt.'''

        self.view_output = render
        #self.print_rules()


    def step(self,Input1):
        '''This function needs an input that is an integer from 1 to 6 that describes a specific movement.'''


        Reward = 0

        if Input1==0:
            source = self.A; target = self.B
        elif Input1== 1:
            source = self.A; target = self.C
        elif Input1== 2:
            source = self.B; target = self.A
        elif Input1== 3:
            source = self.B; target = self.C
        elif Input1== 4:
            source = self.C; target = self.A
        elif Input1== 5:
            source = self.C; target = self.B
        elif Input1 in ['h','H','Help','help','Hilfe','hilfe']:
            self.print_rules()

        else:
            self.printer('keine richtige Angabe')
            self.Actual_state_print()
            Reward -= 10
            state_ = self.state()
            return state_,Reward,False
                #state, reward, done

        if source: #If the list is not empty the code will be executed
            if target:
                if target[-1] > source[-1]:
                    target.append(source.pop())


                    Reward -=1


                    if Input1== 0:
                        self.A = source
                        self.B = target
                    elif Input1== 1:
                        self.A = source
                        self.C = target
                    elif Input1== 2:
                        self.B = source
                        self.A = target
                    elif Input1==3:
                        self.B = source
                        self.C = target
                    elif Input1== 4:
                        self.C = source
                        self.A = target
                    elif Input1== 5:
                        self.C = source
                        self.B = target


                    [Reward,Done]=self.if_Won(Reward)
                    self.Actual_state_print()
                    state_ = self.state()
                    return state_, Reward, Done
                    # state, reward, done

                if target[-1] < source[-1]:
                    Reward -= 10
                    self.printer('It is not possible to place a larger piece on top of another')
                    self.Actual_state_print()

                    state_ = self.state()
                    return state_, Reward, False
                    # state, reward, done
            else:
                target.append(source.pop())

                Reward -= 1

                if Input1 == 0:
                    self.A = source
                    self.B = target
                elif Input1 == 1:
                    self.A = source
                    self.C = target
                elif Input1 == 2:
                    self.B = source
                    self.A = target
                elif Input1 == 3:
                    self.B = source
                    self.C = target
                elif Input1 == 4:
                    self.C = source
                    self.A = target
                elif Input1 == 5:
                    self.C = source
                    self.B = target

                [Reward, Done] = self.if_Won(Reward)
                self.Actual_state_print()
                state_ = self.state()
                return state_, Reward, Done
                # state, reward, done
        else:
            self.printer('it is not possible to move a piece from an empty tower')
            self.Actual_state_print()
            Reward -= 10
            state_ = self.state()
            return state_,Reward,False
                #state, reward, done


    def if_Won(self,Reward):
        """the function checks if the game is over"""
        if self.C == [3,2,1]:

            Reward += 100
            self.Actual_state_print()
            self.printer("winner!!!!!!! winner!!!!!!!!!! chicken for dinner!!!!!!!!")

            state_ = self.state()
            return Reward, True
        else:
            return Reward, False
                #state, reward, done

    def state(self):
        """the function returns the current state of the Game in a Int from 1 to 27"""
        if self.A == [3, 2, 1] and self.B == [] and self.C == []: #aaa
            i =0
        elif self.A == [3, 2] and self.B == [1] and self.C == []: #baa
            i=1
        elif self.A == [3, 2] and self.B == [] and self.C == [1]: #caa
            i =2
        elif self.A == [3] and self.B == [2] and self.C == [1]: #cba
            i=3
        elif self.A == [3] and self.B == [2,1] and self.C == []: #bba
            i=4
        elif self.A == [3,1] and self.B == [2] and self.C == []: #aba
            i=5
        elif self.A == [3,1] and self.B == [] and self.C == [2]: #aca
            i=6
        elif self.A == [3] and self.B == [1] and self.C == [2]: #bca
            i=7
        elif self.A == [3] and self.B == [] and self.C == [2,1]: #ccb
            i=8
        elif self.A == [] and self.B == [3] and self.C == [2,1]: #cca
            i=9
        elif self.A == [] and self.B == [3,1] and self.C == [2]:  # bcb
            i = 10
        elif self.A == [1] and self.B == [3] and self.C == [2]:  # acb
            i = 11
        elif self.A == [1] and self.B == [3,2] and self.C == []:  # abb
            i = 12
        elif self.A == [] and self.B == [3,2,1] and self.C == []:  # bbb
            i = 13
        elif self.A == [] and self.B == [3,2] and self.C == [1]:  # cbb
            i = 14
        elif self.A == [2] and self.B == [3] and self.C == [1]:  # cab
            i = 15
        elif self.A == [2] and self.B == [3,1] and self.C == []:  # bab
            i = 16
        elif self.A == [2,1] and self.B == [3] and self.C == []:  # aab
            i = 17
        elif self.A == [2,1] and self.B == [] and self.C == [3]:  # aac
            i = 18
        elif self.A == [2] and self.B == [1] and self.C == [3]:  # bac
            i = 19
        elif self.A == [2] and self.B == [] and self.C == [3,1]:  # cac
            i = 20
        elif self.A == [] and self.B == [2] and self.C == [3,1]:  # cbc
            i = 21
        elif self.A == [] and self.B == [2] and self.C == [3,1]:  # cbc
            i = 22
        elif self.A == [] and self.B == [2,1] and self.C == [3]:  # bbc
            i = 23
        elif self.A == [1] and self.B == [2] and self.C == [3]:  # abc
            i = 24
        elif self.A == [1] and self.B == [] and self.C == [3,2]:  # acc
            i = 25
        elif self.A == [] and self.B == [1] and self.C == [3,2]:  # bcc
            i = 26
        elif self.A == [] and self.B == [] and self.C == [3,2,1]:  # ccc
            i = 27
        else:
            for i in range(10):
                print('this shouldnt happen!!! this is a BUGGGGGGGGGGG \n')


        return i

    def reset(self):
        self.A = [3, 2, 1]
        self.B = []
        self.C = []

        Reward = 0
        state_ = self.state()
        return state_
        # state, reward, done

    def printer(self,string_):
        if self.view_output == True:
            print(string_)
    def Actual_state_print(self):
        if self.view_output == True:
            print(self.A, self.B, self.C, '##############', sep='\n')

    def print_rules(self):
        if self.view_output == True:
            print('________________________________________________________')
            print('\n')
            print('         you are playing the tower of hanoi!')
            print('                     THE RULES')
            print('\n')
            print('________________________________________________________')
            print('\n', '\n', sep='\n')
            print(' +Only one disk can be moved at a time.')
            print(' +Each move consists of taking the upper \n'
                  '  disk from one of the stacks and placing it on\n'
                  '  top of another stack. In other words, a disk\n'
                  '  can only be moved if it is the uppermost disk on a stack.\n')
            print(' +No larger disk may be placed on top of a smaller disk.')
            print(' +as Input you need a number from 1 to 6 that means a specific movement.')