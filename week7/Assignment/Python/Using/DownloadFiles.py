import urllib.request

Area_Codes= [118021348, 118021348, 118021350, 118021564, 118021565,
 118021566, 118021567, 118021568, 118021569, 118021570]
 #From Census website

for i in Area_Codes:

    print('Beginning file download with urllib2...')

    file_url = ("https://itt.abs.gov.au/itt/query.jsp?method=GetGenericData&datasetid=ABS_REGIONAL_ASGS2016&or=MEASURE&and=ASGS_2016.{number},FREQUENCY.A&TIME_FORMAT=P1Y&periods=2013,2014,2015,2016,2017,2018&format=csv&order=original").format(number=i)
    #format URL with area codes (how to break up nicely?)

    from urllib import request
    title_url = "https://itt.abs.gov.au/itt/r.jsp?RegionSummary&region={number}&dataset=ABS_REGIONAL_ASGS2016&geoconcept=ASGS_2016&measure=MEASURE&datasetASGS=ABS_REGIONAL_ASGS2016&datasetLGA=ABS_REGIONAL_LGA2018&regionLGA=LGA_2018&regionASGS=ASGS_2016".format(number=i)
    html = request.urlopen(title_url).read().decode('utf8')
    html[:60]
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    java_title = soup.find('title')
    content=java_title.string
    title=content.split(":")[0]
    #Gets area name from website

    save_path='/Users/jbrighton/Documents/1161/me/week7/Data/{number}_{name}'.format(number=i, name=title)
    urllib.request.urlretrieve(file_url, save_path)
    #Save location with unique title