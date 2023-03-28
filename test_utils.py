import utils as u
import matplotlib.pyplot as plt

def test_get_portfolio_return():
    d_weights = {'IEI': 0.6, 'VOO': 0.4}
    df_pf = u.get_portfolio_return(d_weights)
    df_pf.plot()
    plt.show()
# test_get_portfolio_return()

def test_calc_historical_var():
    d_weights = {'IEI': 0.1, 'VOO': 0.9}
    l_conf_levels = [0.99, 0.95]
    print(u.calc_historical_var(d_weights, l_conf_levels))
test_calc_historical_var()
