#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:14:54 2025

@author: can
"""

#%% simulations.py

# import necessary libraries
from random import randint
from typing import List


def galton(num_bins: int, num_balls: int) -> List[int]:
    """
    simulates data for a galton board

    Parameters
    ----------
    num_bins : int
        number of bins that the galton board should have.
    num_balls : int
        number of balls that are used as input to the galton board.

    Returns
    -------
    bins : list
        list with sum of balls falling within each of the "num_bins" bins.

    """
    # create the number of bins
    bins = [0] * (num_bins + 1)
    # for each ball
    for _ in range(num_balls):
        pos = 0
        # go over each bin
        for _ in range(num_bins):
            # flip a coin whether ball is in current bin
            coin_flip = randint(0, 1)
            # if yes, increase bin-counter by 1
            if coin_flip == 1:
                pos += 1
        # save final result
        bins[pos] = bins[pos] + 1

    return bins