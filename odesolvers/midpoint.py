def midpoint(x1, x2, y0, h):
  """
  Midpoint method to solve ODE at domain x [x1,x2] 
  
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
  a = 0
  b = 1
  alpha = 0.5
  beta = 0.5

  x_midpoint = []
  y_midpoint = []

  for i in x:
    x_midpoint.append(float(i))
    y_midpoint.append(float(y))

    f1 = dfdx(i, y)
    k1 = h * f1

    f2 = dfdx((i + alpha * h), (y + beta * k1))
    k2 = h * f2
    
    y = y + (a * k1) + (b * k2)

  return(x_midpoint, y_midpoint)
