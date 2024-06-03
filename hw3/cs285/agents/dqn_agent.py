from typing import Sequence, Callable, Tuple, Optional

import torch
from torch import nn

import numpy as np

import cs285.infrastructure.pytorch_util as ptu


class DQNAgent(nn.Module):
    def __init__(
        self,
        observation_shape: Sequence[int],
        num_actions: int,
        make_critic: Callable[[Tuple[int, ...], int], nn.Module],
        make_optimizer: Callable[[torch.nn.ParameterList], torch.optim.Optimizer],
        make_lr_schedule: Callable[
            [torch.optim.Optimizer], torch.optim.lr_scheduler._LRScheduler
        ],
        discount: float,
        target_update_period: int,
        use_double_q: bool = False,
        clip_grad_norm: Optional[float] = None,
    ):
        super().__init__()

        self.critic = make_critic(observation_shape, num_actions)
        self.target_critic = make_critic(observation_shape, num_actions)
        self.critic_optimizer = make_optimizer(self.critic.parameters())
        self.lr_scheduler = make_lr_schedule(self.critic_optimizer)

        self.observation_shape = observation_shape
        self.num_actions = num_actions
        self.discount = discount
        self.target_update_period = target_update_period
        self.clip_grad_norm = clip_grad_norm
        self.use_double_q = use_double_q

        self.critic_loss = nn.MSELoss()

        self.update_target_critic()

        print('Agent details:')
        print(self.__dict__)

    def get_action(self, observation: np.ndarray, epsilon: float = 0.02) -> int:
        """
        Used for evaluation.
        """
        observation = ptu.from_numpy(np.asarray(observation))[None]

        # TODO(student): get the action from the critic using an epsilon-greedy strategy
        result = self.critic(observation)

        # def full_print(var,name):
        #     print(name,var)
        #     print(name+'.shape',var.shape)
        # full_print(observation,'observation') # observation: batched input, [batch_size,obs_size]
        # full_print(result,'result') # result: batched, [batch_size,num_actions]
        action = torch.argmax(result,dim=-1) \
            if torch.rand([1]).item()>epsilon else torch.randint(0,self.num_actions,size=result.shape[0:1])
        return ptu.to_numpy(action).squeeze(0).item()

    def update_critic(
        self,
        obs: torch.Tensor,
        action: torch.Tensor,
        reward: torch.Tensor,
        next_obs: torch.Tensor,
        done: torch.Tensor,
    ) -> dict:
        """Update the DQN critic, and return stats for logging."""
        (batch_size,) = reward.shape
        def full_print(var,name):
            print(name,var)
            print(name+'.shape',var.shape)
        # full_print(obs,'obs') # [batch,ob_dim]
        # full_print(action,'action') # [batch]
        # full_print(reward,'reward') # [batch]
        # full_print(next_obs,'next_obs') # [batch,ob_dim]

        # Compute target values
        with torch.no_grad():
            # TODO(student): compute target values

            if self.use_double_q:
                next_qa_values = torch.argmax(self.critic(next_obs),dim=-1)
                next_q_values = self.target_critic(next_obs)[torch.arange(0,next_obs.shape[0]),next_qa_values.to(torch.long)]
            else:
                next_action = ...
                next_qa_values = self.target_critic(next_obs)
                next_q_values = torch.max(next_qa_values,dim=-1).values
            target_values = reward + self.discount * next_q_values * (1-done.float())

        # TODO(student): train the critic with the target values
        qa_values = ...
        q_values = self.critic(obs)[torch.arange(0,obs.shape[0]),action.to(torch.long)]
        loss = torch.nn.functional.mse_loss(q_values,target_values)


        self.critic_optimizer.zero_grad()
        loss.backward()
        grad_norm = torch.nn.utils.clip_grad.clip_grad_norm_(
            self.critic.parameters(), self.clip_grad_norm or float("inf")
        )
        self.critic_optimizer.step()

        self.lr_scheduler.step()

        return {
            "critic_loss": loss.item(),
            "q_values": q_values.mean().item(),
            "target_values": target_values.mean().item(),
            "grad_norm": grad_norm.item(),
        }

    def update_target_critic(self):
        self.target_critic.load_state_dict(self.critic.state_dict())

    def update(
        self,
        obs: torch.Tensor,
        action: torch.Tensor,
        reward: torch.Tensor,
        next_obs: torch.Tensor,
        done: torch.Tensor,
        step: int,
    ) -> dict:
        """
        Update the DQN agent, including both the critic and target.
        """
        # TODO(student): update the critic, and the target if needed
        critic_stats = self.update_critic(
            obs=obs,
            action=action,
            reward=reward,
            next_obs=next_obs,
            done=done
        )
        if step%(self.target_update_period)==0:
            self.update_target_critic()

        return critic_stats
