# ENGINE SETUP
data = {"21": [77012.22, 6417.69, 2951.87, 42.1696], "24": [84134.34, 7011.20, 3224.86, 46.0694], "27": [91992.70, 7666.06, 3526.07, 50.3724], "30": [100665.30, 8388.78, 3858.49, 55.1213]}
tma = {"0": 0.000, "3": 0.033, "6": 0.066, "9": 0.099 }

def salaryEngine(data, id, tma, rate, net):
    biweekly = data[id][2]
    biweeklyTMA = (data[id][0] / 26) + (data[id][2] * tma[rate])
    #biweeklyTMA = (data[id][2]) + (data[id][2] * tma[rate]) ## This is (quoted biweekly); using (quoted annual / 26).
    annual = data[id][0]
    annualTMA = biweeklyTMA * 26
    annualNet = annualTMA * net
    biweeklyNet = biweekly * net
    print("\n")
    print("# {} + {}%".format(id, rate))
    print("Biweekly + TMA: ${:.2f}".format(biweeklyTMA))
    print("Annual + TMA: ${:.2f}".format(annualTMA))
    print("Biweekly + TMA + Net: ${:.2f}".format(biweeklyNet))
    print("Annual + TMA + Net: ${:.2f}".format(annualNet))

# RUN
id = "27" # 21 / 24 / 27/ 30
rate = "3" # 0 / 3 / 6 / 9
net = (0.655)
salaryEngine(data, id, tma, rate, net)
salaryEngine(data, "27", tma, "9", net)
salaryEngine(data, "30", tma, "9", net)