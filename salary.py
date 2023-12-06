# ENGINE SETUP
data = {"PS27": [91992.70, 7666.06, 3526.07, 116.36, 50.3724], "IS27": [91992.70, 7666.06, 3526.07, 349.08, 50.3724], "IS30": [100665.30, 8388.78, 3858.49, 381.99, 55.1213],}

def salaryEngine(data, id, net):
    biweekly = data[id][2]
    #biweeklyTMA = (data[id][2]) + data[id][3]
    biweeklyTMA = (data[id][0] / 26) + data[id][3]
    annual = data[id][0]
    annualTMA = biweeklyTMA * 26
    annualNet = annualTMA * net
    biweeklyNet = biweekly * net
    print("\n")
    print("# {}".format(id))
    print("Biweekly + TMA: ${:.2f}".format(biweeklyTMA))
    print("Annual + TMA: ${:.2f}".format(annualTMA))
    print("Biweekly + TMA + Net: ${:.2f}".format(biweeklyNet))
    print("Annual + TMA + Net: ${:.2f}".format(annualNet))

# RUN
id = "PS27"
net = (0.655)
salaryEngine(data, id, net)
salaryEngine(data, "IS27", net)
salaryEngine(data, "IS30", net)