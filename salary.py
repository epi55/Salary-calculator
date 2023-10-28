# ENGINE SETUP
def varEngine(annual, tma):
    biweekly = (annual / 26) + tma
    annualTMA = biweekly * 26
    biweeklyNet = biweekly * net
    print("###############\n# Annual: ${:.2f}\n# TMA: ${:.2f}\n#\n# Annual (with TMA): ${:.2f}\n# Biweekly (with TMA): ${:.2f}\n###############".format(annual, tma, annualTMA, biweekly))
    print("# Biweekly (net): ${:.2f}\n###############".format(biweeklyNet))

# RUN
annual = 0
tma = 0
net = 0.655
varEngine(annual, tma)
