import argparse


def get_args():
    parse = argparse.ArgumentParser()

    # subtask graph
    parse.add_argument('--game_name', default='mining',    help='MazeEnv/')
    parse.add_argument('--graph_param', default='train_1', help='difficulty of subtask graph')
    parse.add_argument('--seed', default=1, type=int,  help='random seed')
    parse.add_argument('--nsteps', type=int, default=70, help='the steps to update the network')  
    # ubtask graph



    parse.add_argument('--gamma', type=float, default=0.99, help='the discount factor of RL')
    parse.add_argument('--actor-lr', type=float, default=1e-3, help='learning rate of the algorithm')
    parse.add_argument('--critic-lr', type=float, default=1e-2, help='learning rate of the algorithm')
    parse.add_argument('--num-episodes', type=int, default=1000, help='the number of episodes')
    parse.add_argument('--hidden-dim', type=int, default=128, help='the hidden dim')
    parse.add_argument('--lmbda', type=float, default=0.95, help='the hidden dim')
    parse.add_argument('--epochs', type=int, default=10, help='the hidden dim')
    parse.add_argument('--eps', type=float, default=0.2, help='the hidden dim')

    # actor_lr = 1e-3
    # critic_lr = 1e-2
    # num_episodes = 500
    # hidden_dim = 128
    # gamma = 0.98
    # lmbda = 0.95
    # epochs = 10
    # eps = 0.2

    args = parse.parse_args()


    return args