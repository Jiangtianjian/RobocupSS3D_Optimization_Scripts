# -*- coding:utf-8 -*-
import os
import operator
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
import sys

import argparse

arg = argparse.ArgumentParser(description="Train Result")

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir,'Train_process/results')

def main(args):
    # os.chdir('./Train_process')
    iter_num = args.Inum
    pop_num = args.Pnum

    filename = ''
    data_dic = {}
    max_values = []
    mean_values = []

    notFound = 0
    defaultFlag = True
    for gen in range(1,iter_num):
        max_gen_value = 0.0
        sum_gen_value = 0.0
        mean_gen_value = 0.0
        count = 0
        for population in range(1, pop_num):
            filename = 'value_' + str(gen) + '_i_' + str(population) + '.txt'
            count += 1
            fpath = os.path.join(path, filename)
            try:
                f = open(fpath, 'r')
            except FileNotFoundError:
                notFound += 1
                if notFound > 100:
                    if defaultFlag == True:
                        defaultFlag = False
                        print("{} Unable to find!".format(fpath))
            else:
                try:
                    data = f.readline()
                    data_dic[filename.replace('value_','params_')] = float(data)
                    sum_gen_value += float(data)
                    if float(data) > max_gen_value:
                        max_gen_value = float(data)
                except Exception as e:
                    print(e)
                finally:
                    f.close()
        max_values.append(max_gen_value)
        mean_gen_value = sum_gen_value / count
        mean_values.append(mean_gen_value)

    # os.chdir('..')
    length = len(data_dic)
    print(length)
    sorted_dic = sorted(data_dic.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_dic)

    max_x = range(1, len(max_values)+1)
    mean_x = range(1, len(mean_values)+1)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(max_x, max_values,'--', color='r',  dashes=(4, 3), linewidth=2, label="Maximum value in every generation")
    ax1.plot(mean_x, mean_values, color='b', linewidth=2, label="Average value in every generation")
    ax1.set_xlabel("Generations", fontsize=15)
    ax1.set_ylabel("value", fontsize=15)
    ax1.set_xlim(1, iter_num)
    ax1.legend(fontsize=12)
    plt.savefig('./EvolutionCure.png')
    ax1.tick_params(axis = 'both', labelsize=12)

    plt.show()
    print(sorted_dic[:16])
    filePath=str(sorted_dic[0][0])
    filePath='cp Train_process/params/'+filePath+' ./value' + " Train_process"
    os.system(filePath)
    #print(filePath)
    #print(mean_values)
    #print(max_values)

if __name__ == '__main__':
    arg.add_argument('--Inum','-i', default=21, type=int, help='iternum迭代次数')
    arg.add_argument('--Pnum','-p', default=16, type=int, help='population种群数')
    args = arg.parse_args()
    main(args)


