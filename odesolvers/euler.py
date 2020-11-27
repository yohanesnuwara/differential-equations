def euler(x1, x2, y0, h):
  """
  Euler method to solve ODE at domain x [x1,x2] 
  
  x1: the lowest x in domain
  x2: the upper x in domain
  y0: y at initial condition (x0 = 0)
  h: stepsize
  """
  import numpy as np

  # initial condition
  y = y0

  # time array from timesteps
  x = np.arange(x1, x2+h, h)

  x_euler = []
  y_euler = []

  for i in x:
    x_euler.append(float(i))
    y_euler.append(float(y))

    f = dfdx(i, y)
    y = y + h * f

  return(x_euler, y_euler)
