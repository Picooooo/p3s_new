import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_all_experiments(log_folder, env_name):
    dir = os.listdir(log_folder)
    list_folder = []
    df = pd.DataFrame()
    newpath = ''

    for d in dir:
        list_folder.append(d)

    num_experiments = len(list_folder)
    for i in range(num_experiments):
        newpath = log_folder + '/' + list_folder[i] + '/progress.csv'
        df.insert(i,i,pd.read_csv(newpath)['return-average'][:1000])

    mean = []
    std = []
    x = []
    epoch = df.shape[0]
    for i in range(epoch):
        x.append(i*1000)
        mean.append(df.iloc[i].sum()/num_experiments)
        std.append(np.std(df.iloc[i]))

    ci = 1.96 * np.array(std)/np.sqrt(epoch)
    name = str(env_name)
    plt.plot(x, mean, label="P3S-TD3")
    plt.xlabel("Number of steps")
    plt.ylabel("Score")
    plt.title(name)
    plt.fill_between(x, (mean-ci), (mean+ci), color='blue', alpha=0.1)
    plt.legend()
    plt.savefig("./results/" + name)

def plot_one_experiments(log_folder, env_name, seed):
    log_file = log_folder + 'iter' + str(seed)
    df = pd.DataFrame()
    
    newpath = log_file + '/progress.csv'
    df.insert(0, 0, pd.read_csv(newpath)['return-average'][:1000])

    mean = []
    std = []
    x = []
    epoch = df.shape[0]
    for i in range(epoch):
        x.append(i*1000)
        mean.append(df.iloc[i].sum()/1)
        std.append(np.std(df.iloc[i]))

    ci = 1.96 * np.array(std)/np.sqrt(epoch)
    name = str(env_name)
    plt.plot(x, mean, label="P3S-td3-new")
    plt.xlabel("Number of steps")
    plt.ylabel("Score")
    plt.title(name)
    plt.fill_between(x, (mean-ci), (mean+ci), color='blue', alpha=0.1)
    plt.legend()
    plt.savefig("./results/" + name + "/" + str(seed))
