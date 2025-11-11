def approximate_pi(n_terms):
  terms = []
  for i in range(n_terms):
    term = ((-1)**i)/(2*i+1)
    terms.append(term)
  return 4*sum(terms)
