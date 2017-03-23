# -*- coding: utf-8 -*-
import json
from collections import Counter
from decimal import Decimal
import numpy as np
import matplotlib as plt
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *

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
arrysizestz= np.array(sizestz)
totaltz=np.array(sum(Decimal(i) for i in sizestz))
percentsizestz= (arrysizestz * 100) /totaltz
labels = labelstz
sizes = percentsizestz
figure(figsize=(8,8))
ax = axes([0.1, 0.1, 0.8, 0.8])
pie(sizes, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
title('Timezone', bbox={'facecolor':'0.8', 'pad':5})
savefig(pp, format='pdf')


#time
# timeresult = Counter(time)
# plottime = timeresult.items()
# labelstime, sizestime = zip(*plottime)
# arrysizestime= np.array(sizestime)
# totaltime=np.array(sum(Decimal(i) for i in sizestime))
# cumsizestime= np.cumsum(arrysizestime)
# scatter(labelstime, cumsizestime, s=20, c='b', marker='o', cmap=None, norm=None,
#         vmin=None, vmax=None, alpha=None, linewidths=None,
#         verts=None, **kwargs)
# #scatter chart for time
#
# plt.savefig(pp, format='pdf')

#hashtags
hshresult = Counter(allhash)
plothsh = hshresult.items()
labelshsh, sizeshsh = zip(*plothsh)
arrysizeshsh= np.array(sizeshsh)
totalhsh=np.array(sum(Decimal(i) for i in sizeshsh))
percentsizeshsh= (arrysizeshsh * 100) /totalhsh
#pichart for timezone
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = labelshsh
sizes = percentsizeshsh
figure(figsize=(8,8))
ax = axes([0.1, 0.1, 0.8, 0.8])
pie(sizes, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                 # Equal aspect ratio ensures that pie is drawn as a circle.
title('Hashtags', bbox={'facecolor':'0.8', 'pad':5})
savefig(pp, format='pdf')

#language
langresult = Counter(language)
plotlang = langresult.items()
labelslang, sizeslang = zip(*plotlang)
arrysizeslang= np.array(sizeslang)
totallang=np.array(sum(Decimal(i) for i in sizeslang))
percentsizeslang= (arrysizeslang * 100) /totallang
#pichart for timezone
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = labelslang
sizes = percentsizeslang
figure(figsize=(8,8))
ax = axes([0.1, 0.1, 0.8, 0.8])
pie(sizes, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
title('Language', bbox={'facecolor':'0.8', 'pad':5})
savefig(pp, format='pdf')
pp.close()
