from __future__ import unicode_literals
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


# Create your views here.

def index(request):
	for i in range(0,7):
		print(i)
		titles = ["BHU", "ROORKEE","HYDERABAD","INDORE","ROPAR","DELHI","BOMBAY"]
		if i == titles.index("BHU"):
			page_link = 'https://www.iitbhu.ac.in/dept/cse/people/faculty'
			page_response = requests.get(page_link,timeout=5)
			page_content = BeautifulSoup(page_response.content, "html.parser")
			print (type(page_content))
			#print (page_content.prettify())
			g_data = page_content.find_all('tr', attrs={'class': 'odd'})
			list_bhu = []
			for item in g_data:
				list_bhu.append(item.contents[3].text.replace("View full profile", ""))

			#print (type(g_data[0].contents[3]))
			# print ("\n\n\n hiii middle of both")
			#print "\n\n Stripped Data"
			# striped = prices.text.strip()
			# print (striped)
		if i == titles.index("ROORKEE"):
			url = "https://www.iitr.ac.in/departments/CSE/pages/People+Faculty_List.html"
			r = requests.get(url)
			soup = BeautifulSoup(r.content,"html.parser")
			g_data = soup.find_all("div", {"class": "detail"})
			list_rki = []
			for item in g_data:
				list_rki.append(item.contents[0].text)
		if i == titles.index("HYDERABAD"):
			url = "http://www.cse.iith.ac.in/?q=People/Faculty"
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			g_data = soup.find_all('tbody')
			list_hyd = []
			for item in g_data[0].contents:
				list_hyd.append(item.find_all("a")[0].text)
		if i == titles.index("INDORE"):
			url = "http://cse.iiti.ac.in/faculty.html"
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			g_data = soup.find_all('td')
			list_ind = []
			for item in g_data:
				try:
					list_ind.append(item.contents[0].find_all("u")[0].text)
				except:
					pass
		if i == titles.index("ROPAR"):
			url = "http://www.iitrpr.ac.in/computer-science-engineering"
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			g_data = soup.find_all("p")
			list_rpr = []
			for item in g_data:
				try:
					list_rpr.append(item.contents[1].text.replace("IT Services", ""))
				except:
					pass
		if i == titles.index("DELHI"):
			url = "http://www.cse.iitd.ernet.in/index.php/2011-12-29-23-14-30/faculty"
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			g_data = soup.find_all("table")up
			list = []
			for j in range(0, 41):
				try:
					print(list.append(g_data[0].find_all("a")[j].text))
					#print(list)
				except:
					pass

		if i == titles.index("BOMBAY"):
			url = "https://www.cse.iitb.ac.in/page14"
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			g_data = soup.find_all("table")
			query = g_data[0].find_all("a")
			length = len(query)
			list_bom = []
			for j in range(0, length):
				if (j%2) == 0:
					list_bom.append(query[j].text)
				else:
					pass
		if i == titles.index("GUWAHATI"):
			url = "http://www.iitg.ac.in/cse/csefaculty"
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			g_data = soup.find_all("tbody")
			list



	context = {
			 'list_bhu': list_bhu,
			 'list_rki': list_rki,
			 'list_hyd': list_hyd,
			 'list_ind': list_ind,
			 'list_rpr': list_rpr,
			 'list': list,
			 'list_bom': list_bom,
			 'title_bhu': titles[0],
			 'title_rki': titles[1],
	 		 'title_hyd': titles[2],
			 'title_ind': titles[3],
			 'title_rpr': titles[4],
			 'title_del': titles[5],
			 'title_bom': titles[6]
			 }
	return render(request, "facultys/index.html", context)