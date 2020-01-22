"""
Name:        ExSTraCS_Best_Prediction.py
Authors:     Siddharth Verma - Written in India
Contact:     ryan.j.urbanowicz@darmouth.edu
Created:     October 22, 2019
Modified:    October 22, 2019
Description: Based on a given match set, this module selects the best rule (acc to fitness) to select the phenotype prediction for ExSTraCS.

---------------------------------------------------------------------------------------------------------------------------------------------------------
ExSTraCS V2.0: Extended Supervised Tracking and Classifying System - An advanced LCS designed specifically for complex, noisy classification/data mining tasks,
such as biomedical/bioinformatics/epidemiological problem domains.  This algorithm should be well suited to any supervised learning problem involving
classification, prediction, data mining, and knowledge discovery.  This algorithm would NOT be suited to function approximation, behavioral modeling,
or other multi-step problems.  This LCS algorithm is most closely based on the "UCS" algorithm, an LCS introduced by Ester Bernado-Mansilla and
Josep Garrell-Guiu (2003) which in turn is based heavily on "XCS", an LCS introduced by Stewart Wilson (1995).

Copyright (C) 2014 Ryan Urbanowicz
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABLILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
---------------------------------------------------------------------------------------------------------------------------------------------------------
"""

class BestPrediction:
    def __init__(self, population, exploreIter):
        self.decision = None
        best_cl = population.popSet[0]
        best_fitness = 0
        for ref in population.matchSet:
            cl = population.popSet[ref]
            if cl.fitness > best_fitness:
                best_cl = cl
                best_fitness = cl.fitness

        if not cl.isTree:
            centroid = (best_cl.phenotype[0] + best_cl.phenotype[1])/2
            self.decision = centroid
        else:
            self.decision = best_cl.phenotype

    def getDecision(self):
        """ Returns prediction decision. """
        return self.decision

