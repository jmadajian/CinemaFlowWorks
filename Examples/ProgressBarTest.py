from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from time import sleep


class TaskSupplier(object):
    """
    A placeholder object for the function that do the real work.
    Not really required, but I like using class to keep namespaces clean ;-)
    """
    @staticmethod
    def do_task(callback):
        """ Does the heavy lifting/processing. Calls 'callback' when done """
        print "Processing task...."
        sleep(0.5)
        callback()


class ProgressAnimator(object):
    """
    This class handles the animation of a 'ProgressBar' instance given a list
    of functions that do the real work. Each of these functions need to accept
    a single 'callback' parameter specifying the function to call when done.
    """
    def __init__(self, progressbar, callbacks):
        self.pb = progressbar  # Reference to the progress bar  to update
        self.pb.max, self.pb.value = len(callbacks), 0
        self.callbacks = callbacks  # A list of callback functions doing work
        self.index = 0  # The index of the callback being executed
        Clock.schedule_once(lambda dt: callbacks[0](self.task_complete), 0.1)

    def task_complete(self):
        """ The last called heavy worker is done. See if we have any left """
        self.index += 1
        self.pb.value = self.index
        if self.index < len(self.callbacks):
            Clock.schedule_once(
                lambda dt: self.callbacks[self.index](self.task_complete), 0.1)



class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'


        # We add 2 buttons to demonstrate the generic nature of the
        # ProgressAnimator
        btn = Button(text="Start 3")
        btn.bind(on_release=lambda btn: self.trigger(3))
        self.add_widget(btn)

        btn = Button(text="Start 6")
        btn.bind(on_release=lambda btn: self.trigger(6))
        self.add_widget(btn)

        self.pb = ProgressBar()
        self.add_widget(self.pb)

    def trigger(self, number):
        """ Start the list of tasks """
        # The tasklist can be any list of functions. The only requirement is
        # that each accepts 1 parameter - callback to call when done
        task_list = [TaskSupplier.do_task for num in xrange(0, number)]
        ProgressAnimator(self.pb, task_list)



class TestApp(App):
    def build(self):
        return MainMenu()
 
if __name__ == "__main__":
    TestApp().run()

