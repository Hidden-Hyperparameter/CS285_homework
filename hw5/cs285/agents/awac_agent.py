from typing import Callable, Optional, Sequence, Tuple, List
import torch
from torch import nn


from cs285.agents.dqn_agent import DQNAgent


class AWACAgent(DQNAgent):
    def __init__(
        self,
        observation_shape: Sequence[int],
        num_actions: int,
        make_actor: Callable[[Tuple[int, ...], int], nn.Module],
        make_actor_optimizer: Callable[[torch.nn.ParameterList], torch.optim.Optimizer],
        temperature: float,
        **kwargs,
    ):
        super().__init__(observation_shape=observation_shape, num_actions=num_actions, **kwargs)

        self.actor = make_actor(observation_shape, num_actions)
        self.actor_optimizer = make_actor_optimizer(self.actor.parameters())
        self.temperature = temperature

    def compute_critic_loss(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
        rewards: torch.Tensor,
        next_observations: torch.Tensor,
        dones: torch.Tensor,
    ):
        with torch.no_grad():
            # TODO(student): compute the actor distribution, then use it to compute E[Q(s, a)]
            # Ea′ ∼π [Qϕk−1 (s′ , a′ )])
            batch_size = next_observations.shape[0]
            
            probs = self.actor(next_observations).probs # [128,5]
            next_qa_values = torch.sum(
                probs*self.target_critic(next_observations),dim=-1
            )

            # Use the actor to compute a critic backup

            next_qs = next_qa_values

            # TODO(student): Compute the TD target
            target_values = rewards + next_qs * (1-dones.float()) * self.discount

        
        # TODO(student): Compute Q(s, a) and loss similar to DQN
        qa_values = self.critic(observations)
        q_values = qa_values[torch.arange(0,actions.shape[0]),actions]
        assert q_values.shape == target_values.shape

        loss = torch.nn.functional.mse_loss(q_values,target_values)

        return (
            loss,
            {
                "critic_loss": loss.item(),
                "q_values": q_values.mean().item(),
                "target_values": target_values.mean().item(),
            },
            {
                "qa_values": qa_values,
                "q_values": q_values,
            },
        )

    def compute_advantage(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
        action_dist: Optional[torch.distributions.Categorical] = None,
    ):
        # TODO(student): compute the advantage of the actions compared to E[Q(s, a)]
        with torch.no_grad():
            qa_values = self.target_critic(observations)
            q_values = qa_values[torch.arange(0,observations.shape[0]),actions]
            probs = 0
            if action_dist is not None:
                probs = action_dist.probs
            else:
                raise NotADirectoryError()
            values = torch.sum(probs*qa_values,dim=-1)

            advantages = q_values - values
        return advantages

    def update_actor(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
    ):
        # TODO(student): update the actor using AWAC
        distrs = self.actor(observations)
        loss = -(torch.log(distrs.probs[torch.arange(0,actions.shape[0]),actions])*torch.exp(self.temperature*self.compute_advantage(
            observations=observations,
            actions=actions,
            action_dist=distrs
        ))).mean(dim=0) # Use MEAN for MLE training! (or tune hyperparam by self) # Use temperature

        self.actor_optimizer.zero_grad()
        loss.backward()
        self.actor_optimizer.step()
        assert any([True for layer in self.actor.logits_net if hasattr(layer,'weight')])
        if any([layer.weight.isnan().any() for layer in self.actor.logits_net if hasattr(layer,'weight')]):
            raise UnicodeTranslateError()

        return loss.item()

    def update(self, observations: torch.Tensor, actions: torch.Tensor, rewards: torch.Tensor, next_observations: torch.Tensor, dones: torch.Tensor, step: int):
        metrics = super().update(observations, actions, rewards, next_observations, dones, step)

        # Update the actor.
        actor_loss = self.update_actor(observations, actions)
        metrics["actor_loss"] = actor_loss

        return metrics
