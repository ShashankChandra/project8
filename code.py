import random
import plotly.figure_factory as ff
import plotly.express as px
import statistics
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
data_result = df["reading score"].tolist()

mean = statistics.mean(data_result)
standarddevi = statistics.stdev(data_result)
mode = statistics.mode(data_result)
median = statistics.median(data_result)

#fig = px.line(x = dice_result, y = count)
print(mean)
print(standarddevi)
print(mode)
print(median)

firstStandardDeviStart,firstStandardDeviEnd = mean-standarddevi, mean+standarddevi
secondStandardDeviStart,secondStandardDeviEnd = mean-(standarddevi*2), mean+(standarddevi*2)
thirdStandardDeviStart,thirdStandardDeviEnd = mean-(standarddevi*3), mean+(standarddevi*3)

listOfDataInFirst = [result for result in data_result if result > firstStandardDeviStart and result < firstStandardDeviEnd]
listOfDataInSecond = [result for result in data_result if result > secondStandardDeviStart and result < secondStandardDeviEnd]
listOfDataInThird = [result for result in data_result if result > thirdStandardDeviStart and result < thirdStandardDeviEnd]

print("{}% of data lies within first standard deviation".format(len(listOfDataInFirst)*100/len(data_result)))
print("{}% of data lies within second standard deviation".format(len(listOfDataInSecond)*100/len(data_result)))
print("{}% of data lies within third standard deviation".format(len(listOfDataInThird)*100/len(data_result)))

fig = ff.create_distplot([data_result],["result"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[firstStandardDeviStart,firstStandardDeviStart],y = [0,0.17], mode = "lines",name="Standard Deviation 1 Start"))
fig.add_trace(go.Scatter(x=[firstStandardDeviEnd,firstStandardDeviEnd],y = [0,0.17], mode = "lines",name="Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[secondStandardDeviStart,secondStandardDeviStart],y = [0,0.17], mode = "lines",name="Standard Deviation 2 Start"))
fig.add_trace(go.Scatter(x=[secondStandardDeviEnd,secondStandardDeviEnd],y = [0,0.17], mode = "lines",name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[thirdStandardDeviStart,thirdStandardDeviStart],y = [0,0.17], mode = "lines",name="Standard Deviation 3 Start"))
fig.add_trace(go.Scatter(x=[thirdStandardDeviEnd,thirdStandardDeviEnd],y = [0,0.17], mode = "lines",name="Standard Deviation 3 End"))
fig.show()