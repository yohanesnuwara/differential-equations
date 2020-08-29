def rmse(y_exact, y_calc):
  return(np.sqrt(np.sum(((y_exact - y_calc)**2) / len(y_calc))))

def errorabs(y_exact, y_calc):
  return((np.abs(y_exact - y_calc) / y_exact) * 100)
