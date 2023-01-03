#!/usr/bin/env python3
import math, numpy as np, copy
from Gui_towers_of_hanoi import GUI

class Hanoi_towers(object):
    '''this class tries to simulate the game of the towers of hanoi in a simplified way'''
    def __init__(self, NN,render):

        """Declare some variables, N is the nummer of tokens"""

        self.tokens = list(range(NN, 0, -1))

        self.A = copy.deepcopy(self.tokens)
        self.B = []
        self.C = []
        self.NN = NN
        self.observation_space = 3**NN
        self.action_space = 6
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
        if self.C == self.tokens:

            Reward += 100
            self.Actual_state_print()
            self.printer("winner!!!!!!! winner!!!!!!!!!! chicken for dinner!!!!!!!!")

            state_ = self.state()
            return Reward, True
        else:
            return Reward, False
                #state, reward, done

    def state(self):
        """the function returns the current state of the Game in a Int"""
        state_ = ''
        for i in self.tokens:
            if i in self.A:
                state_ = state_ + '0'
            if i in self.B:
                state_ = state_ + '1'
            if i in self.C:
                state_ = state_ + '2'

        Ternary = int(state_)

        state_ = self.convertToDecimal(Ternary)
        return state_

    def convertToDecimal(self,N):

        if (N != 0):

            decimalNumber = 0;
            i = 0;
            remainder = 0;

            # Loop to iterate through
            # the number
            while (N != 0):
                remainder = N % 10;
                N = N // 10;

                # Computing the decimal digit
                decimalNumber += remainder * math.pow(3, i);
                i += 1;

            return int(decimalNumber)
        else:
            return 0

    def reset(self):
        self.A = copy.deepcopy(self.tokens)
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
            if self.C == self.tokens:
                # sets the counter to True so that the move count in the GUI stops
                GUI.stop_count = True
            # sends the lists of all towers and the number of discs to the GUI
            GUI.update_state(tower_a=self.A, tower_b=self.B, tower_c=self.C, num_discs=self.NN)

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