# -*- coding: utf-8 -*-
import json
from collections import Counter
from decimal import Decimal
import numpy as np
import matplotlib as plt
from matplotlib.backends.backend_pdf import PdfPages

tweets = []


for line in open('rawdata.txt'):
  try:
    tweets.append(json.loads(line))
  except:
    pass
#data allocation
tweet = tweets[0]
timezone = [tweet['user']['time_zone'] for tweet in tweets]
hashtags1 = [(T['entities']['hashtags'][0]['text'] if len(T['entities']['hashtags']) >= 1 else None) for T in tweets]
hashtags2 = [(T['entities']['hashtags'][1]['text'] if len(T['entities']['hashtags']) >= 2 else None) for T in tweets]
hashtags3 = [(T['entities']['hashtags'][2]['text'] if len(T['entities']['hashtags']) >= 3 else None) for T in tweets]
time = [tweet['created_at'] for tweet in tweets]
allhash = hashtags1 + hashtags2 + hashtags3
#retweet = [(T['retweeted_status'] if len(T['retweeted_status']) >= 1 else None) for T in tweets]
language = [tweet['user']['lang'] for T in tweets]

pp = PdfPages('analysis.pdf')
#data for charts
#timzone data processing and chart
tzresult = Counter(timezone)
plottz = tzresult.items()
labelstz, sizestz = zip(*plottz)
arrysizestz= numpy.array(sizestz)
totaltz=numpy.array(sum(Decimal(i) for i in sizestz))
percentsizestz= (arrysizestz * 100) /totaltz
#pichart for timezone
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = labelstz
sizes = percentsizestz
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig(pp, format='pdf')


#time
timeresult = Counter(time)
plottime = timeresult.items()
labelstime, sizestime = zip(*plottime)
arrysizestime= numpy.array(sizestime)
totaltime=numpy.array(sum(Decimal(i) for i in sizestime))
cumsizestime= np.cumsum(arrysizestime)
#scatter chart for time

plt.savefig(pp, format='pdf')

#hashtags
hshresult = Counter(allhash)
labelshsh, sizeshsh = zip(*plothsh)
arrysizeshsh= numpy.array(sizeshsh)
totalhsh=numpy.array(sum(Decimal(i) for i in sizeshsh))
percentsizeshsh= (arrysizeshsh * 100) /totalhsh
#pichart for timezone
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = labelshsh
sizes = percentsizeshsh
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig(pp, format='pdf')

#language
langresult = Counter(language)
labelslang, sizeslang = zip(*plotlang)
arrysizeslang= numpy.array(sizeslang)
totallang=numpy.array(sum(Decimal(i) for i in sizeslang))
percentsizeslang= (arrysizeslang * 100) /totallang
#pichart for timezone
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = labelslang
sizes = percentsizeslang
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig(pp, format='pdf')

pp.close()
