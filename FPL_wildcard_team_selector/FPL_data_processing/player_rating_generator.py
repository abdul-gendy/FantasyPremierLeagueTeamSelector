import pandas as pd
from .utilities import set_range_one_to_ten


def calculate_players_scores_weighted_avg_sum(players_info, weights):
    '''
    takes in a DataFrame containing all the players info and stats, and a list containing all the weights that will be used in the 
    weighted sum. Adds a column called Algorithm Score to the existing Dataframe which is the final score out of 10 given to each player

    Parameters:
        players_info (DataFrame): DataFrame containing all the players info that was read from the main fantasy premier league API
        weights (list): list containing the weights of [form, ROI, ptspergame, ict, ep_next, future games score] in that order
    '''
    columns_to_normalize = ['form','points_per_game','ict_index','ep_next','ROI','future games attacking ease','npxG', 'xA']
    set_range_one_to_ten(players_info, columns_to_normalize)

    #npxG, xA, form, pointspergame, ict_index, Future Games Score
    sum_of_weights = weights[0] + weights[1] + weights[2] + weights[3] + weights[4] + weights[5]
    players_info.loc[:,'Algorithm Score'] = ((players_info['npxG'].multiply(weights[0])) 
                                        + (players_info['xA'].multiply(weights[1])) 
                                        + (players_info['form'].multiply(weights[2]))
                                        + (players_info['points_per_game'].multiply(weights[3]))
                                        + (players_info['ict_index'].multiply(weights[4]))                          
                                        + (players_info['future games attacking ease'].multiply(weights[5]))) / sum_of_weights                       
    players_info.sort_values(by='Algorithm Score', inplace = True, ascending=False) 