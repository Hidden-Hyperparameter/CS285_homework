# Notes on Homework 5

The report is at [here](./template/hw5.pdf).

# Summary of algorithms

The main training loop of offline RL is relatively simple: load the data into replay buffer, then for each iteration pick some data out of buffer and train. The only differences are for different agents, the update process is different. These processes can be found in details in the papers.

# The bugs I have written

1. (Most important) In double Q learning, `get_action` should use argmax from **target net**, instead of current net. This, as discussed in hw3 and referred as the `bird method`, really matters here in the RND algorithm. Changing this (i.e. using the `bird method`) make the RND explore a lot further.
2. MLE training loss is negative log-likehood, instead of positive. Shame for getting this wrong AGAIN :(
3. MLE training should use average over all samples, instead of sum, in convention. (You can use sum but you then need to tune the learning rate.)
4. In IQL, the value network outputs a shape `[128,1]` value, which means that we should `flatten` before adding it into rewards or calculating expectile loss! This cost me a lot of time.