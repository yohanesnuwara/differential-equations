def rungekutta4(x1, x2, y0, h):
  """
  Runge-Kutta 4th order method to solve ODE at domain x [x1,x2] 
  
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
  a = 0.5
  b = 0.5
  alpha = 1
  beta = 1

  x_rk4 = []
  y_rk4 = []

  for i in x:
    x_rk4.append(float(i))
    y_rk4.append(float(y))

    f1 = dfdx(i, y)
    k1 = h * f1

    f2 = dfdx((i + 0.5 * h), (y + 0.5 * k1))
    k2 = h * f2

    f3 = dfdx((i + 0.5 * h), (y + 0.5 * k2))
    k3 = h * f3

    f4 = dfdx((i + h), (y + k3))
    k4 = h * f4
    
    y = y + (k1 / 6) + (k2 / 3) + (k3 / 3) + (k4 / 6)

  return(x_rk4, y_rk4)
