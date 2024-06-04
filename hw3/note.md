# Algorithm Summary

## DQN
For each step:

1. **Sample Data**: Use exploration policy to select action based on the current observation.
2. **Add Data**: Step the environment with the selected action, get reward and next observation. Stop if done. Add the transition to the replay buffer.
3. **Train Agent**: Sample a batch from replay buffer, update the agent:
    1. Update the critic based on backup equation.
    2. Update the target critic periodically or with momentum.
4. **Evaluate the model**: for each step, choose argmax of Q function as action.

## SAC
For each step:

1. **Sample Data**: Use exploration policy (or random policy) to select action based on the current observation.
2. **Add Data**: Step the environment with the selected action, get reward and next observation. Stop if done. Add the transition to the replay buffer.
3. **Train Agent**: Sample a batch from replay buffer, update the agent:
    1. Update the critic several times (but usually 1) based on backup equation.
    2. Update the actor based on the critic (or target critic). See the pdf file for details.
    3. Update the target critic periodically or with momentum.
4. **Evaluate the model**: for each step, use the actor to take action.


# Bug

I forget to use `done` in the dqn `update_critic` function. If `done`, then the trajectory is end, and `next_ob` is actually the next trajectory. In this situation, the target should just be `r`, without the q value for next observation (which isn't even from the same trajectory!)
