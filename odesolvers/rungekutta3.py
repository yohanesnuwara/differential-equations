def rungekutta3(x1, x2, y0, h):
  """
  Runge-Kutta 3rd order method to solve ODE at domain x [x1,x2] 
  
  x1: the lowest x in domain
  x2: the upper x in domain
  y0: y at initial condition (x0 = 0)
  h: stepsize
  """

  # initial condition
  y = y0

  # time array from timesteps
  x = np.arange(x1, x2+h, h)

  # parameters
  a = 0.5
  b = 0.5
  alpha = 1
  beta = 1

  x_rk3 = []
  y_rk3 = []

  for i in x:
    x_rk3.append(float(i))
    y_rk3.append(float(y))

    f1 = dfdx(i, y)
    k1 = h * f1

    f2 = dfdx((i + 0.5 * h), (y + 0.5 * k1))
    k2 = h * f2

    f3 = dfdx((i + h), (y - k1 + (2 * k2)))
    k3 = h * f3
    
    y = y + (1/6)*(k1 + 4 * k2 + k3)

  return(x_rk3, y_rk3)
