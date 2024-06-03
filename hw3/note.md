# Bug

I forget to use `done` in the dqn `update_critic` function. If `done`, then the trajectory is end, and `next_ob` is actually the next trajectory. In this situation, the target should just be `r`, without the q value for next observation (which isn't even from the same trajectory!)