import pygame
from src.input_actions import Action


class InputMapper:
    def __init__(self, bindings: dict[Action, set[int]]):
        """
        bindings:
            Action -> set of pygame key constants
        """
        self.bindings = bindings

    def is_pressed(self, action: Action) -> bool:
        """
        Continuous input (hold key).
        """
        keys = pygame.key.get_pressed()
        return any(keys[key] for key in self.bindings[action])

    def is_triggered(self, event: pygame.event.Event, action: Action) -> bool:
        """
        Discrete input (KEYDOWN).
        """
        return (
            event.type == pygame.KEYDOWN
            and event.key in self.bindings[action]
        )
