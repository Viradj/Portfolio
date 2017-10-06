from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/nl/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

# opening connecten and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# soup parsing
page_soup = soup(page_html, "html.parser")

#Graps products
containders = page_soup.findAll("div", {"class" : "item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, true_price\n"
f.write(headers)

for container in containders:
	brand = container.div.div.a.img["title"] 

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	price = container.findAll("li", {"class" : "price-current"})
	true_price = price[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("true_price: " + true_price)

	f.write(brand + "," + product_name + "," + true_price +  "\n")
	
f.close()