import numpy as np
import pandas as pd
from scipy.stats import beta


class NudgeEngine:

    def __init__(self, n_agents, friccion, nudge_base):
        self.n = n_agents
        self.f = friccion
        self.n_p = nudge_base

    def run_simulation(self):
        loss_av = np.random.lognormal(0.7, 0.2, self.n)
        budget = np.random.beta(5, 2, self.n)
        df = pd.DataFrame({'loss_aversion': loss_av, 'budget': budget})

        valor_base = 0.4
        p_a = np.clip((valor_base + 0.05) - (self.f / df['budget']), 0, 1)
        df['convert_A'] = np.random.binomial(1, p_a)

        efecto_nudge = self.n_p * df['loss_aversion']
        p_b = np.clip((valor_base + efecto_nudge) - (self.f / df['budget']), 0, 1)
        df['convert_B'] = np.random.binomial(1, p_b)

        return df

    def get_bayesian_analysis(self, df):

        s_a, f_a = df['convert_A'].sum(), self.n - df['convert_A'].sum()
        s_b, f_b = df['convert_B'].sum(), self.n - df['convert_B'].sum()

        samples_a = beta(1 + s_a, 1 + f_a).rvs(4000)
        samples_b = beta(1 + s_b, 1 + f_b).rvs(4000)


        prob_win = (samples_b > samples_a).mean()

        return samples_a, samples_b, prob_win