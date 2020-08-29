def modified_euler(x1, x2, y0, h):
  """
  Modified Euler method to solve ODE at domain x [x1,x2] 
  
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

  x_modeuler = []
  y_modeuler = []

  for i in x:
    x_modeuler.append(float(i))
    y_modeuler.append(float(y))

    f1 = dfdx(i, y)
    k1 = h * f1

    f2 = dfdx((i + alpha * h), (y + beta * k1))
    k2 = h * f2
    
    y = y + (a * k1) + (b * k2)

  return(x_modeuler, y_modeuler)
