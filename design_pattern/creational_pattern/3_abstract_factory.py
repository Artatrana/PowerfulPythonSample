# Abstract Factory: Creates families of related objects without specifying their concrete classes.
# For example, a furniture factory can produce matching sets of chairs, tables, and sofas in a specific style
# (modern or classic), ensuring all items belong to the same family.

# # Abstract Factory: Provide an interface to create a family of related objects without specifying their concrete classes
# If Factory Method = one product,
# then Abstract Factory = multiple related products.
# When you need Abstract Factory
# Objects come in groups that must work together
# You need to ensure compatibility between them
# Switching the whole family will be easy

# Let see the implementation of Button and checkboxes for Both Window and MAC

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Window family implementation

class WindowsButton(Button):
    def render(self):
        print("Render Windows Button")

class WindowsCheckbox(Checkbox):
    def render(self):
        print("Render Windows Checkbox")

# Mac family implementation
class MacButton(Button):
    def render(self):
        print("Render Mac Button")

class MacCheckbox(Checkbox):
    def render(self):
        print("Render Mac Checkbox")

# Abstract Factory interface
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete factories (families)
class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Client code decoupled

def render_ui(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

# Usage
factory = WindowsUIFactory()
render_ui(factory)

factory = MacUIFactory()
render_ui(factory)

