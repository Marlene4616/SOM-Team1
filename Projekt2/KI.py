import random, time
import numpy as np
from N_towers_of_hanoi import Hanoi_towers
from Gui_towers_of_hanoi import GUI


class KI:

    def __init__(self, NN):
        self.env = Hanoi_towers(NN, False)
        self.NN = NN  # Number of discs

    def q_learning(self, total_epochs=1001, reset=True):
        start_time = time.time()

        self.env.view_output = False

        # open existing Q-table or create a new one
        if not reset:
            q_table = np.loadtxt(f"Q_table_{self.NN}.txt")
        else:
            q_table = np.zeros([self.env.observation_space, self.env.action_space])
            print("Q-table is reset")

        alpha = 0.1  # learning rate:
        gamma = 0.6  # discount factor: determines how much importance we want to give to future rewards
        epsilon = 0.1

        epochs_before = 0

        for i in range(1, total_epochs):
            state = self.env.reset()

            epochs, penalties, reward = 0, 0, 0
            done = False

            while not done:
                if random.uniform(0, 1) < epsilon:
                    action = random.randint(0, 5)  # Explore action space

                else:
                    action = np.argmax(q_table[state])  # Exploit learned values

                next_state, reward, done = self.env.step(action)

                old_value = q_table[state, action]
                next_max = np.max(q_table[next_state])

                new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
                q_table[state, action] = new_value

                if reward == -10:
                    penalties += 1

                state = next_state
                epochs += 1

            # Calculate progress
            if round(i * 100 / total_epochs) == epochs_before + 10:
                print(round(i * 100 / total_epochs), "%")
                epochs_before = round(i * 100 / total_epochs)

        execution_time = time.time() - start_time

        print(f"Penalties: {penalties}")
        print(f"Training finished in {execution_time} seconds.\n")

        np.savetxt(f"Q_table_{self.NN}.txt", q_table)

    def show_result(self):
        self.env.view_output = True
        q_table = np.loadtxt(f"Q_table_{self.NN}.txt")

        state = self.env.reset()
        self.env.Actual_state_print()
        time.sleep(1)

        done = False

        n = 0
        while not done:
            action = np.argmax(q_table[state])  # Exploit learned values

            state, reward, done = self.env.step(action)

            n += 1
            time.sleep(1)

        print(f"Finished in {n} moves!\n")
        print(f"Optimal number of moves:{2 ** self.NN - 1}")


# Start der KI
GUI.setup(width=600, height=200)  # window size can be set manually but can also stay empty
test = KI(6)  # Number of discs

test.q_learning(1001, False)  # Number of epochs, True = new q-table & False = reuse existing q-table
test.show_result()
GUI.window.mainloop()  # GUI bleibt offen, nachdem alles durchgelaufen ist
