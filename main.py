import gym
import numpy as np

env = gym.make('CartPole-v1', render_mode="human")

state = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    
    result = env.step(action)
    
    if len(result) == 5:
        state, reward, terminated, truncated, info = result
        done = terminated or truncated
    else:
        state, reward, done, info = result

    env.render()

    if done:
        state = env.reset()

env.close()
