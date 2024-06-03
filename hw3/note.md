# Bug

I forget to use `done` in the dqn `update_critic` function. If `done`, then the trajectory is end, and `next_ob` is actually the next trajectory. In this situation, the target should just be `r`, without the q value for next observation (which isn't even from the same trajectory!)

# Unable to Import

gym.error.Error: We're Unable to find the game "MsPacman". Note: Gym no longer distributes ROMs. If you own a license to use the necessary ROMs for research purposes you can download them via `pip install gym[accept-rom-license]`. Otherwise, you should try importing "MsPacman" via the command `ale-import-roms`. If you believe this is a mistake perhaps your copy of "MsPacman" is unsupported. To check if this is the case try providing the environment variable `PYTHONWARNINGS=default::ImportWarning:ale_py.roms`. For more information see: https://github.com/mgbellemare/Arcade-Learning-Environment#rom-management