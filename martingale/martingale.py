""""""  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	 	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	 	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 		  		  		    	 		 		   		 		  
or edited.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	 	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	 	 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def author():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return "swang3220"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def gtid():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return 904181297  # replace with your GT ID number  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    result = False  		  	   		 	 	 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 	 	 		  		  		    	 		 		   		 		  
        result = True  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return result  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def test_code():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    win_prob = 0.4737  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # add your code here to implement the experiments

  	#Experiment 1
    figure1(win_prob)
    figure2(win_prob)
    figure3(win_prob)

    #Experiment 2
    figure4(win_prob)
    figure5(win_prob)

def figure1(win_prob):
    num_simulations = 10
    x_limit = 1001
    simulations = []

    while len(simulations) < num_simulations:
        simulations.append(strategy(win_prob))

    x_coordinates = range(x_limit)

    for index, sim in enumerate(simulations):
        plt.plot(x_coordinates, sim, label = "simulation " + str(index+1))

    plt.title("Figure 1: Simple Roulette Winnings for 10 Episodes")
    plt.xlabel("Spin #")
    plt.ylabel("Episode Winnings")
    plt.xlim([0, 300])
    plt.ylim([-256,100])
    plt.legend(loc="best")

    plt.savefig("figure1.png")
    plt.close()

def figure2(win_prob):
    x_limit = 1001
    x_coordinates = range(x_limit)

    mean, mean_plus_std, mean_minus_std = generate_mean(win_prob)
    
    plt.plot(x_coordinates, mean, label="Mean")
    plt.plot(x_coordinates, mean_plus_std, label="Mean + Std Dev")
    plt.plot(x_coordinates, mean_minus_std, label="Mean - Std Dev")

    plt.title("Figure 2: Mean Winnings Per Spin Across 1000 Episodes")
    plt.xlabel("Spin #")
    plt.ylabel("Winnings")
    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    plt.legend(loc="best")
    
    plt.savefig("figure2.png")
    plt.close()

def figure3(win_prob):
    x_limit = 1001
    x_coordinates = range(x_limit)

    median, median_plus_std, median_minus_std = generate_median(win_prob)

    plt.plot(x_coordinates, median, label="Median")
    plt.plot(x_coordinates, median_plus_std, label="Median + Std Dev")
    plt.plot(x_coordinates, median_minus_std, label="Median - Std Dev")

    plt.title("Figure 3: Median Winnings Per Spin Across 1000 Episodes")
    plt.xlabel("Spin #")
    plt.ylabel("Winnings")
    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    plt.legend(loc="best")
    
    plt.savefig("figure3.png")
    plt.close()


def figure4(win_prob):
    x_limit = 1001
    x_coordinates = range(x_limit)

    mean, mean_plus_std, mean_minus_std = generate_mean(win_prob, True)

    plt.plot(x_coordinates, mean, label="Mean")
    plt.plot(x_coordinates, mean_plus_std, label="Mean + Std Dev")
    plt.plot(x_coordinates, mean_minus_std, label="Mean - Std Dev")

    plt.title("Figure 4: Mean Winnings Per Spin Across 1000 Episodes With Capped Bankroll")
    plt.xlabel("Spin #")
    plt.ylabel("Winnings")
    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    plt.legend(loc="best")

    plt.savefig("figure4.png")
    plt.close()

def figure5(win_prob):
    x_limit = 1001
    x_coordinates = range(x_limit)

    median, median_plus_std, median_minus_std = generate_median(win_prob, True)

    plt.plot(x_coordinates, median, label="Median")
    plt.plot(x_coordinates, median_plus_std, label="Median + Std Dev")
    plt.plot(x_coordinates, median_minus_std, label="Median - Std Dev")

    plt.title("Figure 5: Median Winnings Per Spin Across 1000 Episodes With Capped Bankroll")
    plt.xlabel("Spin #")
    plt.ylabel("Winnings")
    plt.xlim([0, 300])
    plt.ylim([-256, 100])
    plt.legend(loc="best")

    plt.savefig("figure5.png")
    plt.close()

def generate_mean(win_prob, realistic = False):
    simulations = []
    num_simulations = 1000

    while len(simulations) < num_simulations:
        simulations.append(strategy(win_prob, realistic))

    mean = np.mean(simulations, axis=0)
    std = np.std(simulations, axis=0)

    mean_plus_std = np.add(mean, std)
    mean_minus_std = np.subtract(mean, std)

    return mean, mean_plus_std, mean_minus_std


def generate_median(win_prob, realistic = False):
    simulations = []
    num_simulations = 1000

    while len(simulations) < num_simulations:
        simulations.append(strategy(win_prob, realistic))

    median = np.median(simulations, axis=0)
    std = np.std(simulations, axis=0)

    median_plus_std = np.add(median, std)
    median_minus_std = np.subtract(median, std)

    return median, median_plus_std, median_minus_std

def strategy(win_prob, realistic = False):
    episode_winnings = 0
    max_number_bets = 1001
    winnings_per_spin = [0]
    max_winnings = 80
    bankroll = 256
    busted = False

    while episode_winnings < max_winnings and len(winnings_per_spin) < max_number_bets and not busted:
        won = False
        bet_amount = 1
        while not won and len(winnings_per_spin) < max_number_bets:
            if realistic:
                cash_remaining = episode_winnings + bankroll
                if cash_remaining <= 0:
                    #busted
                    episode_winnings = -bankroll
                    winnings_per_spin.append(episode_winnings)
                    busted = True
                    break
                else:
                    bet_amount = min(bet_amount, cash_remaining)
            won = get_spin_result(win_prob)
            if won:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
            winnings_per_spin.append(episode_winnings)

    #fill rest of array if episode ends early
    while len(winnings_per_spin) < max_number_bets:
        winnings_per_spin.append(episode_winnings)

    return np.array(winnings_per_spin)

if __name__ == "__main__":  		  	   		 	 	 		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	 	 		  		  		    	 		 		   		 		  
