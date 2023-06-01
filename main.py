import random
import gym
import fh_ac_ai_gym
from Task.Propositions import *

#Create Gym environment
env = gym.make('Wumpus-v0') 
env.reset()

#Define the possible actions
REVERSE_ACTION_DICT= {0: "WALK", 1:"TURNLEFT", 2:"TURNRIGHT", 3:"GRAB", 4: "SHOOT", 5:"CLIMB"}
POSSIBLE_ACTIONS = {v: k for k, v in REVERSE_ACTION_DICT.items()}


"""
#Tell the agent the initial state
observation, reward, done, info= env.step(POSSIBLE_ACTIONS["TURNLEFT"])
env.render()


# Create an agent with your class or functions
KBA = KnowledgebasedAgent("FC")
KBA.TELL(observation) #Tell the agent the initial state
KBA.ASK("W21") #Ask if KB entails W21
 

observation, reward, done, info= env.step(POSSIBLE_ACTIONS["WALK"])
env.render()
KBA.TELL(observation)
KBA.ASK("W21") #FC: False , R: True

#continuesly step through the environment make entailments based on the observations
# ... 



"""
# you can also use the agent to make decisions based on a policy
#(not relevant for the assignment)

for i in range(1000):
    print("Iteration: ", i)
    
    action = random.choice([0,1,2,3,4,5])
    observation, reward, done, info= env.step(action)
    print(observation)
    if done:
        if reward[0] == -1000:
            print("AGENT DIED")
        elif reward[0] == 1000:
            print("AGENT GETS THE GOLD AND RETURNED SAFE")
        else: 
            print(reward)
        print("\nFINAL RESULT: ")
        env.render()
        observation = env.reset()
        break;

    print()
