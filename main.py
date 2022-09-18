import gym
import torch
import numpy as np


from utils import train_on_policy_agent
from ppo import PPO
from arguments import get_args

from plot import plot



args = get_args()




device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

env_name = 'CartPole-v0'
env = gym.make(env_name)
env.seed(0)
torch.manual_seed(0)


state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

agent = PPO(args, state_dim, action_dim, device)
return_list = train_on_policy_agent(env, agent, args)

plot(return_list, env_name) 
