import pygame
from typing import Callable
from config import WIDTH, HEIGHT
from ui.root.component import Component
from ui.root.keyboard_event_handler import KeyboardEventHandler


class Layout(Component, KeyboardEventHandler):
    """
    Layout is a container component that manages multiple UI components,
    handling their arrangement, updating, and rendering on the screen. This
    class also supports keyboard and mouse event handling, forwarding events
    to child components as needed.

    Attributes:
    -----------
    components : list[Component]
        A list that stores child components managed by this layout.

    Methods:
    --------
    setup_components():
        Placeholder method intended for setting up initial child components.

    update_components():
        Placeholder method intended for updating child components as needed
        during each frame.

    draw(screen: pygame.Surface):
        Updates, arranges, and renders all child components to the specified
        display surface.

    add_component(component: Component):
        Adds a new child component to the layout.

    remove_component(component: Component):
        Removes a specified component from the layout.

    remove_component_by_index(index: int):
        Removes a component from the layout by its index in
        the components list.

    handle_mouse_event(event: pygame.event.Event):
        Forwards mouse events to the layout and its child components.
    """

    def __init__(
        self,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        """
        Initializes the Layout instance, setting its size to the global WIDTH
        and HEIGHT and configuring optional event callbacks for click, hover,
        and hover-end actions.

        Parameters:
        -----------
        on_click : Callable, optional
            Callback function triggered on a click event within the layout.

        on_hover : Callable, optional
            Callback function triggered on a hover event within the layout.

        on_hover_end : Callable, optional
            Callback function triggered when a hover event ends within
            the layout.
        """
        Component.__init__(
            self,
            0,
            0,
            WIDTH,
            HEIGHT,
            on_click,
            on_hover,
            on_hover_end,
        )

        self.components: list[Component] = []
        self.setup_components()

    def setup_components(self):
        """
        Intended to be overridden by subclasses. This method is used to
        set up initial components in the layout. By default, it performs
        no action.
        """
        pass

    def update_components(self):
        """
        Intended to be overridden by subclasses. This method updates
        each frame as required for all child components. By default,
        it performs no action.
        """
        pass

    def draw(self, screen: pygame.Surface):
        """
        Renders all components in the layout to the specified screen surface.

        Parameters:
        -----------
        screen : pygame.Surface
            The Pygame surface to which components will be drawn.

        Notes:
        ------
        Before drawing, this method calls `update_components()` to ensure
        components are updated as needed. It then renders each component
        on the layout area and finally draws the layout on the screen.
        """
        self.update_components()
        for component in self.components:
            component.draw(self)
        super().draw(screen)

    def add_component(self, component: Component):
        """
        Adds a child component to the layout.

        Parameters:
        -----------
        component : Component
            The UI component to add to the layout.
        """
        self.components.append(component)

    def remove_component(self, component: Component):
        """
        Removes a specified component from the layout.

        Parameters:
        -----------
        component : Component
            The component to remove from the layout.
        """
        self.components.remove(component)

    def remove_component_by_index(self, index: int):
        """
        Removes a component from the layout by its index.

        Parameters:
        -----------
        index : int
            The index of the component to remove from the layout's
            components list.
        """
        self.components.pop(index)

    def handle_mouse_event(
        self,
        event: pygame.event.Event,
        rect: pygame.Rect = pygame.Rect(0, 0, 0, 0),
    ):
        """
        Handles mouse events for the layout and forwards them to
        child components.

        Parameters:
        -----------
        event : pygame.event.Event
            The Pygame event representing the mouse action.
        rect : pygame.Rect
            Move the Rect by the Parent Rect
        """
        super().handle_mouse_event(event)
        for component in self.components:
            component.handle_mouse_event(event, rect)

    def handle_keyboard_event(self, event: pygame.event.Event):
        for component in self.components:
            if hasattr(component, "handle_keyboard_event"):
                component.handle_keyboard_event(event)
        super().handle_keyboard_event(event)
