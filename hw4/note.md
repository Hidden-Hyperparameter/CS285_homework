# Structure of the whole training process of Model-based learning (without SAC)

For each iteration:

1. **Sample Trajectory**: Use current policy (or random policy in the beginning) to sample trajectories, add to replay buffer
2. **Update Statistics**: Update statistics of the replay buffer, used in the dynamic model to normalize inputs
3. **Train Dynamic Model**: for each epoch:
    1. random sample a dataset from the replay buffer, for each model in ensemble.
    2. train the model using the dataset.
4. **Evaluate the model**: Let the model plan based on the learnt dynamics.

# Structure of the training process with SAC (and MBPO)

For each iteration:

1. **Sample Trajectory**: Use current policy (or random policy in the beginning) to sample trajectories, add to replay buffer **and SAC replay buffer**.
2. **Update Statistics**: Update statistics of the replay buffer, used in the dynamic model to normalize inputs
3. **Train Dynamic Model**: Train the dynamic model for several epochs:
    1. random sample a dataset from the replay buffer, for each model in ensemble.
    2. train the model using the dataset.
4. **Train SAC**: for each epoch:
    1. **Collect MBPO rollouts**: sample a starting point from replay buffer, and use the dynamic model to predict the next state, use the env to get the reward, and use SAC to get action. Continue until each rollout exceeds a given length (e.g. 10). Add these rollouts to SAC replay buffer.
    2. **Train SAC**: train the actor-critic net using samples from SAC replay buffer.
5. **Evaluate the model**: In this part, only use the SAC (actor) model to get action.

# Summary

- in the first algorithm, the dynamic model both act as dynamic predictor and planner
- in the second algorithm, the dynamic model only act as dynamic predictor, and another separate actor-critic model is used to generate action.
