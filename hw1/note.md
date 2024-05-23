# Notes

Here is a pesudo code of the vanilla training process.

```python
path = LoadPathDataFromFile()
for step in range(TRAINING_STEPS):
    train_data = pick_n(path,TRAIN_BATCH_SIZE)
    obs = train_data['obs']
    acs = train_data['acs']
    policy.train(obs,acs)
```

Notice that in the code, nothing really is relavent with RL. This is just a DL training procedure.

Here is a pesudo code of the training process with DAGGER.

```python
buffer = Buffer()
for itr in range(tot_iters):
    if itr==0:
        path = LoadPathDataFromFile()
    else:
        # sample data from our policy
        sample_num = 0
        while sample_num < TOTAL_SAMPLES:
            new_obs = []
            new_acs = []
            new_rewards = []
            ob = env.reset()
            while True:
                ac = policy.predict(ob)
                new_obs.append(ob)
                new_acs.append(ac)
                ob, rew, done, _ = env.step(ac)
                new_rewards.append(rew)
                if done or len(new_obs) > MAX_ONCE_SAMPLES:
                    break
            sample_num += len(new_obs)
            path.add(new_obs,new_acs,new_rewards)
        # re-label actions
        for i,ob in enumerate(path.obs):
            ac = expert.predict(ob)
            path.acs[i]=ac

    buffer.add(path)
    # train
    for step in range(TRAINING_STEPS):
        train_data = pick_n(buffer,TRAIN_BATCH_SIZE)
        obs = train_data['obs']
        acs = train_data['acs']
        policy.train(obs,acs)
```