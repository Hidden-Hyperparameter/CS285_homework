# Structure of the whole training process of Model-based learning (without SAC)

For each iteration:

1. Use current policy to sample trajectories, add to replay buffer
2. Update statistics of the replay buffer, used in the dynamic model to normalize inputs
3. Train the dynamic model for several epochs:
    - random sample a dataset from the replay buffer, for each epoch and each model in ensemble.
4. Evaluate the model. In this part, let the model plan based on the learnt dynamics.