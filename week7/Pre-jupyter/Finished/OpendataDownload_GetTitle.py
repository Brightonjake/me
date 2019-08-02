from urllib import request
url = "https://itt.abs.gov.au/itt/r.jsp?RegionSummary&region=118021569&dataset=ABS_REGIONAL_ASGS2016&geoconcept=ASGS_2016&measure=MEASURE&datasetASGS=ABS_REGIONAL_ASGS2016&datasetLGA=ABS_REGIONAL_LGA2018&regionLGA=LGA_2018&regionASGS=ASGS_2016"
html = request.urlopen(url).read().decode('utf8')
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('title')

content=title.string
content.split(":")
print (content.split(":")[0])


