# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:54:12 2021

@author: phili
"""
import pandas as pd
import numpy as np

def process_data(data):
    
    #Fill empty age and fare with the mean of each
    data['Age'] = data['Age'].fillna(data['Age'].mean())
    data['Fare'] = data['Fare'].fillna(data['Fare'].mean())
    
    #Fill missing Embarked value with most common which is S
    data['Embarked'] = data['Embarked'].fillna('S')
    
    #Drop Name, Ticket and Cabin since they will not be used in my first try.
    data.drop('Name', axis=1, inplace=True)
    data.drop('Ticket', axis=1, inplace=True)
    data.drop('Cabin', axis=1, inplace=True)
    
    #changing sex into number, male = 1 and female = 0
    data['Sex'] = data['Sex'].map({'female':0, 'male':1})
    
    #changing Embarked into number, S = 0, C = 1 and Q = 2
    data['Embarked'] = data['Embarked'].map({'S':0, 'C':1, 'Q':2})
    return data

def prepare_submission(response):
    PID = np.arange(892,1310)
    df = pd.DataFrame(data=np.dstack((PID,response)).squeeze(),columns=['PassengerId', 'Survived'])
    return df
    
    
