# My Experiment

As mentioned in my notes, I think that using a random ensemble member each timestamp is more reasonable. In the code below

```python
for i in range(self.ensemble_size):
    next_obs.append(self.get_dynamics_predictions(
        # i
        torch.randint(0,self.ensemble_size-1,(1,)).item()
        ,obs[i],acs))
```

If we use `i`, then this is the traditional algorithm; however, using this random number may lead to better performance. I will list the results here.

## Problem 2

Old Method avg return: -48.69

My Method avg return: -31.30

## Problem 3,4,5,6

See [report.md](../report.md)