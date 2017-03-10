# -*- coding: utf-8 -*


import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_graphs(listX, listY, labelX, labelY, out, t='nada'):
    fig, ax = plt.subplots()
    plt.plot(listX, listY, linewidth=3.0)

    ax.set_xlabel(labelX, fontsize='xx-large', labelpad=25, weight='semibold')
    ax.set_ylabel(labelY, fontsize='xx-large', labelpad=25, weight='semibold')

    plt.tick_params(axis='both', labelsize=20, pad=25)

    # for tick in ax.xaxis.get_ticklabels():
    #    tick.set_fontsize('x-large')
    #    tick.set_weight('bold')

    # for tick in ax.yaxis.get_ticklabels():
    #    tick.set_fontsize('x-large')
    #    tick.set_weight('bold')

    plt.tight_layout()

    if t != 'nada':
        plt.title(t, fontsize='xx-large', weight='semibold')

    plt.savefig(out)


def plot_two_graphs(listAX, listAY, listBX, listBY, labelA, labelB, labelX, labelY, out, t='nada'):
    fig, ax = plt.subplots()

    plt.plot(listAX, listAY, label=labelA, linewidth=3.0)
    plt.plot(listBX, listBY, label=labelB, linewidth=3.0)

    ax.set_xlabel(labelX, fontsize='xx-large', labelpad=25, weight='semibold')
    ax.set_ylabel(labelY, fontsize='xx-large', labelpad=25, weight='semibold')

    plt.legend()

    plt.tick_params(axis='both', labelsize=20, pad=25)

    plt.tight_layout()

    if t != 'nada':
        plt.title(t, fontsize='xx-large', weight='semibold')

    plt.savefig(out)


def plot_two_graphs_point(listAX, listAY, listBX, listBY, labelA, labelB, labelX, labelY, out, t='nada'):
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()

    plt.plot(listAX, listAY, 'o', label=labelA, linewidth=3.0)
    plt.plot(listBX, listBY, 'o', label=labelB, linewidth=3.0)

    ax.set_xlabel(labelX, fontsize='xx-large', labelpad=25, weight='semibold')
    ax.set_ylabel(labelY, fontsize='xx-large', labelpad=25, weight='semibold')

    plt.legend()

    plt.tick_params(axis='both', labelsize=20, pad=25)

    plt.tight_layout()

    if t != 'nada':
        plt.title(t, fontsize='xx-large', weight='semibold')

    plt.show()


def plot_graphs_bar_old(listX, listY, labelX, labelY, out, t='nada'):
    fig, ax = plt.subplots()

    plt.barh(listX, listY, 0.5, align='edge')

    # plt.xticks(listX)

    ax.set_xlabel(labelX, fontsize='xx-large', labelpad=25, weight='semibold')
    ax.set_ylabel(labelY, fontsize='xx-large', labelpad=25, weight='semibold')

    plt.tick_params(axis='both', labelsize=20, pad=25)

    plt.tight_layout()

    if t != 'nada':
        plt.title(t, fontsize='xx-large', weight='semibold')

    plt.savefig(out)


def plot_graphs_bar(listX, listY, labelX, labelY, out, t='nada'):
    fig, ax = plt.subplots()
    plt.rcdefaults()
    y_pos = np.arange(len(listX))
    with plt.style.context('fivethirtyeight'):
        plt.barh(y_pos, listY, 1, align='edge', alpha=0.5)
        plt.yticks(y_pos, listX, size=9)
        ax.set_xlabel(labelY)
        ax.set_ylabel(labelX)
        plt.title(t, fontsize='xx-large', weight='semibold')
    plt.savefig(out)
