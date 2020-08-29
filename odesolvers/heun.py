def heun(x1, x2, y0, h, iteration):
  """
  Iterative Heun method to solve ODE at domain x [x1,x2] 
  
  x1: the lowest x in domain (initial x0 = 0)
  x2: the upper x in domain
  y0: y at initial condition (x0 = 0)
  h: stepsize
  iteration: how many times will be iterated
  """

  # initial condition
  y = y0

  # time array from timesteps
  x = np.arange(x1, x2+h, h)

  x_heun = [x1]
  y_heun = [y0]

  for i in range(len(x)-1):

    f = dfdx(x[i], y)
    y_pred = y + h * f

    for j in range(iteration):
      corr = dfdx(x[i+1], y_pred)
      f_corr = 0.5 * (f + corr) # corrector
      y_pred = y + h * f_corr # Heun's corrected y
    
    y = y_pred

    x_heun.append(float(x[i+1]))
    y_heun.append(float(y))
  
  return(x_heun, y_heun)
