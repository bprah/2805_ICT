"""
Defines the initial values of a button
"""


class ButtonModel:
    def __init__(self, label, x, y, w, h, hovercolor, defaultcolor, action=None):
        self.label = label
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hovercolor = hovercolor
        self.defaultcolor = defaultcolor
        self.action = action
        self.color = defaultcolor
