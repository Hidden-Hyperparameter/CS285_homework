# Notes 

The general structure of this homework is similar as hw1.

The main loop includes:
- sample trajectories from the environment
- train the agent

The training process of the agent includes:

- calculate Q values (corresponding to $\hat{Q}$ in our notes)
- If there is a baseline, calculate the baseline from a model.
    - baselines are computed from observations
- Use Q values, (possibly) baseline and the reward to calculate the advantage $A$.(GAE, for example, can be used here.)
- Use the advantage, observation and action to calculate the policy gradient and update parameters
    - this is the standard policy gradient algorithm, $\nabla_\theta J(\theta)=\sum \nabla_\theta \log \pi_\theta(a|s)\cdot A(a,s)$
- Update the critics using the Q values and the observations.