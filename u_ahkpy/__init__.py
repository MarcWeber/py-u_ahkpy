import ahkpy as ahk

stack = []

#!/usr/bin/env python
class WithWindow:
    """ make sure beamicon is in foreground """

    @staticmethod
    def current() -> ahk.Window:
        return stack[-1][0]

    def __init__(self, match):
        self.match = match

    def __enter__(self) -> ahk.Window:
        if stack and stack[1][1] == self.match:
            stack.append(stack[-1])
            return stack[-1][0]
        else:
            self.previous = ahk.windows.get_active()
            win = ahk.windows.wait(**self.match)
            win.activate()
            win.wait_active()
            print("waiting for window %s" % str(self.match))

            # win = ahk.all_windows.filter(title=self.title, match=self.match).first()
            # if not win.exists:
                # raise "no beamicon window found"
            # time.sleep(2)
            print("TODO ensure menu is gone")
            stack.append([win, self.match])
            return win

    def __exit__(self, type, value, traceback):
        del stack[-1]
        if hasattr(self, 'previous'):
            self.previous.activate()
