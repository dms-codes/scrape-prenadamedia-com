import requests as r
import csv
from bs4 import BeautifulSoup as bs
HOME_URL = 'https://prenadamedia.com/kategori/'
COLUMNS = ["Title", 
            "Penulis", 
            "Price",
            "Tahun Terbit", 
            "Description",
            "Stock",
            "ISBN",
            "Berat",
            "Dimensi",
            "Halaman",
            "Jenis Cover",
            "Img URL"]
STOCK = 10
books = []

def get_pages_category(last_page,category_url_page):
    """This function returns list of pages per category"""
    if last_page == 0:
        return [category_url_page]
    else:
        return [category_url_page+str(i) for i in range(2, int(last_page)+1)]
    
def scrape():
    """Scrape function"""
    html = r.get(HOME_URL).content
    soup = bs(html,'html.parser')
    categories = soup.find_all('li', class_='product-category product first')
    with open('data.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        col_names = COLUMNS
        writer.writerow(col_names)
        f.flush()
            
        for category in categories:
            category_url = category.find('a')['href']
            category_text = category.find('a').text.strip().title().split('(')[0]
            #print(category_text,category_url,)
            category_url_page = category_url+'page/'
            category_html = r.get(category_url).content
            category_soup = bs(category_html,'html.parser')
            page_num_soup = category_soup.find_all('a', class_='page-numbers')
            try:
                last_page = page_num_soup[-2].text
            except:
                last_page = 0
            for page in get_pages_category(last_page,category_url_page):
                page_category_html = r.get(page).content
                products_soup = bs(page_category_html,'html.parser') 
                for a in products_soup.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link'):
                    title,pengarang,price,tahun_terbit,deskripsi,stock,isbn,berat,dimensi,halaman,jenis_cover,img_url='','','','','','','','','','','',''
                    product_url = a['href']
                    product_html = r.get(product_url).content
                    product_soup = bs(product_html,'html.parser')
                    stock_habis = product_soup.find('p', class_='stock out-of-stock')
                    if stock_habis == None:
                        stock = STOCK
                    else: 
                        stock = 0 

                    try:
                        title = product_soup.find('h1').text
                        price = product_soup.find('span', class_='woocommerce-Price-amount amount').text
                        pengarang = product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_pengarang').find('p').text
                        tahun_terbit = product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_tahun-terbit').find('p').text
                        deskripsi = product_soup.find('div', id='tab-description').text
                        #print(deskripsi)
                        isbn= product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_isbn').find('p').text
                        berat = product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_berat-buku-gram').find('p').text
                        dimensi = product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_ukuran').find('p').text
                        halaman = product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_halaman').find('p').text
                        jenis_cover = product_soup.find('tr', class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_jenis-cover').find('p').text
                        img_url = product_soup.find('div', class_='woocommerce-product-gallery__image').find('a')['href']
                    except:pass
                    row =[title,pengarang,price,tahun_terbit,deskripsi,stock,isbn,berat,dimensi,halaman,jenis_cover,img_url]
                    print(row)
                    writer.writerow(row)
                    f.flush()
                #break
            #break
            
if __name__ == '__main__':
    scrape()
