from bs4 import BeautifulSoup
# with open('home.html','r') as redd:
soup=BeautifulSoup(open('home.html'),'lxml')
s=soup.find_all('div',class_='stm_archive_product_inner_grid_content')
# for title in s:
s=soup.find_all('li',class_=['col-md-4' ,'col-sm-4' ,'col-xs-6'])
p=soup.find_all('h5')
print(s)
    
    # print(title.text)