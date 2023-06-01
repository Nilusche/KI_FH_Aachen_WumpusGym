from gym.envs.registration import register

register(
        id='Wumpus-v0',
        entry_point='fh_ac_ai_gym.wumpus:WumpusWorldEnv',
        )

