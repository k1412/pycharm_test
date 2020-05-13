import re
import matplotlib.pyplot as plt

pattern = r"^[\D]*(\d{1,3})[\D]*(\d\.[\d]*)[\D]*(\d\.[\d]*)$"
with open("../data/cnn_result.txt", mode='r') as f:
    lines = f.readlines()
    epoch = []
    train_loss = []
    accuracy = []
    for line in lines:
        line_str = line.strip('\n')
        matchObj = re.match( pattern, line_str)
        # print(line_str)
        epoch.append(int(matchObj.group(1)))
        train_loss.append(float(matchObj.group(2)))
        accuracy.append(float(matchObj.group(3)))

print(accuracy)
plt.plot(accuracy)
plt.show()