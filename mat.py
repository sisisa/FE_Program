import math
import matplotlib.pyplot as plt

def parse(s):
    return [(x[0], int(x[1:])) for x in s.split()]

class Marker:
    def __init__(self):
        self.x, self.y, self.angle = 0, 0, 0
        plt.xlim(-320, 320)
        plt.ylim(-240, 240)
        
    def forward(self, val):
        rad = math.radians(self.angle)
        dx = val * math.cos(rad)
        dy = val * math.sin(rad)
        x1, y1, x2, y2 = self.x, self.y, self.x + dx, self.y + dy
        plt.plot([x1, x2], [y1, y2], color='black', linewidth=2)
        self.x, self.y = x2, 2
        
    def turn(self, val):
        self.angle = (self.angle + val) % 360
        
    def show(self):
        plt.show()
        
    
def draw(s):
    insts = parse(s)
    marker = Marker()
    stack = []
    opno = 0
    while opno < len(insts):
        print(stack)
        code, val = insts[opno]
        if code == 'F':
            marker.forward(val)
        elif code == 'T':
            marker.turn(val)
        elif code == 'R':
            stack.append({'opno': opno, 'rest': val})
        elif code == 'E':
            if stack[-1]['rest'] > 1:
                opno = stack[-1]['opno']
                stack[-1]['rest'] -= 1
            else:
                stack.pop()
        opno += 1
    marker.show()
    
print(draw('F10'))