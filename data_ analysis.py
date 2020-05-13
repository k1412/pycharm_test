import re
import matplotlib.pyplot as plt

pattern = "^[\D]*(\d{1,3})[\D]*(\d\.[\d]*)[\D]*(\d\.[\d]*).*"
# with open("data/cnn_result_batch32_size128_00005.txt", mode='r') as f:
with open("data/cnn_result.txt", mode='r') as f:
    lines = f.readlines()
    epoch = []
    train_loss = []
    accuracy = []
    for line in lines:
        line_str = line.strip('\n')
        matchObj = re.match( pattern, line_str)
        # print(line_str)
        if matchObj:
            epoch.append(int(matchObj.group(1)))
            train_loss.append(float(matchObj.group(2)))
            accuracy.append(float(matchObj.group(3)))

print(accuracy)
# plt.plot(train_loss, color='red')
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(111)
ax1.set_ylim(0, 1)
ax1.plot(accuracy)
ax1.set_ylabel("accuracy")

ax2 = ax1.twinx()
ax2.set_ylim(0.7, 2)
ax2.set_ylabel("train_loss")
ax2.plot(train_loss,'r')
# plt.plot(accuracy, color='blue')
plt.show()