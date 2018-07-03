import bs4, requests, pyperclip

url = pyperclip.paste()

productData = []

def geteMAGData(productUrl):
    res = requests.get(productUrl)
    try :
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Service Unavailable from URL: ' + productUrl + '\n\n')

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    productName = soup.select('head > title')
    productName = productName[0].text.strip().replace(' - eMAG.ro', '', 1)

    
    pr = soup.select('''#page-skin > div.container > div > div:nth-of-type(2) >
    div.col-sm-5.col-md-7.col-lg-7 > div > div > div.col-sm-12.col-md-6.col-lg-5  >
    form > div.product-highlight.product-page-pricing > p.product-new-price''')
    strPrice = pr[0].text.strip().replace(' Lei', '')
    strPrice = strPrice.replace('.', '', 1)
    
    try :
        price = float(strPrice) /100
        price = str(price) + ' Lei'
        dictObj = {'name': productName, 'price': price}
        productData.append(dictObj)
    except IndexError:
        print('Something went wrong')


geteMAGData(url)

for item in productData:
    print('Name of product: ' + item['name'])
    print('Price of product: ' + item['price'])

