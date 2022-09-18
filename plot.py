import matplotlib.pyplot as plt
from utils import moving_average




def plot(return_list, env_name):
	episodes_list = list(range(len(return_list)))
	plt.plot(episodes_list, return_list)
	plt.xlabel('Episodes')
	plt.ylabel('Returns')
	plt.title('PPO on {}'.format(env_name))
	plt.show()

	mv_return = moving_average(return_list, 9)
	plt.plot(episodes_list, mv_return)
	plt.xlabel('Episodes')
	plt.ylabel('Returns')
	plt.title('PPO on {}'.format(env_name))
	plt.show()