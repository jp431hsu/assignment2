import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ncbi_url = "https://www.ncbi.nlm.nih.gov/pubmed/?term=endotoxin" #the url to visit
response = urllib.request.urlopen(ncbi_url, context=ssl._create_unverified_context()) #opening the webpage
html = response.read() #grab from stream, put into html variable reading html
soup = BeautifulSoup(html, "html.parser") #cuts up html attributes
print('\n' + '\n' + 'printing the contents of soup:' + '\n' + '\n')
print(soup)

ncbi_list = []
titles = []
print('\n' + '\n' + 'We are searching for research articles on the topic of ENDOTOXIN.' '\n' + '\n' + 'They will be collected in a LIST')
for link in soup.find_all('div', attrs={"class":"rslt"}):
    for src in link.find_all('a'):
        if src.text != 'Similar articles' and src.text != 'Free Article' and src.text != 'Free PMC Article':
            titles.append(src.text)
            temp = (src['href'])
            temp = str(temp)
            temp = 'https://www.pubmed.gov' + temp
            ncbi_list.append(temp)               
        else:
            continue
    for item in ncbi_list:
        for char in item: 
            if char == '?':
                ncbi_list.remove(item)
set(ncbi_list)


i = 0
while i < len(ncbi_list):
    print(ncbi_list[i] + '\n' + titles[i] + '\n\n')
    i += 1

#for ttl, link in titles, ncbi_list:
#    print(ttl + '\n' + link + '\n\n')
#    for link in ncbi_list:
#        print(link + '\n')
#    print(ttl + '\n\n')

'''for x in titles:
    print(x + '\n\n')
print(len(ncbi_list))
print('\n' + '\n' + 'Here are the links collected in The List™:' + '\n' + '\n')
print('\n\n'.join(ncbi_list))'''
