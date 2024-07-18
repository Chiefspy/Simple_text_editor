class Ball:
  def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
    self.canvas = canvas
    self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
  def move(self):
    pass
    
