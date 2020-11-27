def ralston(x1, x2, y0, h):
  """
  Ralston method to solve ODE at domain x [x1,x2] 
  
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

  # parameters
  a = 1/3
  b = 2/3
  alpha = 3/4
  beta = 3/4

  x_ralston = []
  y_ralston = []

  for i in x:
    x_ralston.append(float(i))
    y_ralston.append(float(y))

    f1 = dfdx(i, y)
    k1 = h * f1

    f2 = dfdx((i + alpha * h), (y + beta * k1))
    k2 = h * f2
    
    y = y + (a * k1) + (b * k2)

  return(x_ralston, y_ralston)
