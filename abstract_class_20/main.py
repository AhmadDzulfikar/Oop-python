# Membuat abstract class
# abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod    # @ = decorator
    def click(self):
        pass
    
class PushButton(Button):
    def click(self):
        print('push button click')

class RadioButton(Button):
    def click(self):
        print('this is radio button')

tombol1 = PushButton()
tombol1.click()

tombol2 = RadioButton()
tombol2.click()
