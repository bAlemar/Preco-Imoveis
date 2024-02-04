from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time


class WebDriver(object):
    def __init__(self):
        self.options = Options()
        
        #Roda Chrome driver sem interface gráfica
        self.options.add_argument('--headless')
        
        #Evitar CloudFlare
        self.options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        self.options.add_argument("--window-size=1280x1696")


        pass
    
    def get(self):
        """
        Executa o Driver
        """
        
        driver = Chrome(options=self.options)
        self.driver = driver
        return driver
    
    def manual_scroll(self,scroll_percentage):
        """
        Imita um scroll manual
        
        Isso foi necessário, uma vez que caso utilizasse script de scrollar
        imediatamente até o final da página, os dados não carregavam.

        Argumentos:
        - scroll_percentage: Porcentagem que você quer scrollar da página
          Exemplo: scroll_percentage = 100, você scrola até final da página
        """
       
        # Simulação do Scroll
        for i in range(18):
            # Calcula a altura total da página
            total_height = self.driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
            # Calcula a posição em pixels para rolar até a porcentagem desejada
            scroll_position = int((scroll_percentage / 100) * total_height)
            # Rola até o final da página
            self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            
            #Time Sleep Necessário se não vai direto
            time.sleep(1)
            
            if scroll_percentage > 50:
                scroll_percentage +=3
            else:
                scroll_percentage += 5
    
    def extraindo_dados(self,soup):
        """
        Essa função extrai a informações do site por meio da SOPA
        

        Argumentos:
        - soup: Sopa com conteúdo do site(html.parser)
        
        """

        dict_resultado = {'preco_imovel':[],
                        'metro_quadrado':[],
                        'localizacao_rua':[]}
        lista_anuncios = soup.find_all('div',class_='listing-wrapper__content')
        #Tentando percorrer os anuncios:
        card_content = lista_anuncios[0].find_all('div',class_='l-card__content')

        for i in card_content:
            preco_imovel = i.find_all('p',class_="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-bold undefined")[0].text
            metro_quadrado = i.find_all('p',class_='l-text l-u-color-neutral-28 l-text--variant-body-small l-text--weight-regular card__amenity')[0].text
            localizacao_rua = i.find_all('p',class_='l-text l-u-color-neutral-28 l-text--variant-body-small l-text--weight-regular card__street')[0].text
            dict_resultado['preco_imovel'].append(preco_imovel)
            dict_resultado['metro_quadrado'].append(metro_quadrado)
            dict_resultado['localizacao_rua'].append(localizacao_rua)
        print(dict_resultado)
        return dict_resultado

    def Scraping_Zap(self,url):
        """
        Scraping de uma página do Zap Imóveis

        Argumentos:

        - url: URL da página Zap Imóveis (De preferência Galpões)

        """
        
        #Executando nosso driver
        self.get()

        #Entrando no Site
        self.driver.get(url)

        #Evitar erros/bugs
        time.sleep(5)

        # Acionando Scroll Manual
        self.manual_scroll(scroll_percentage=20)

        # Obtém o HTML após o scroll
        html = self.driver.page_source

        # Criando um objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        
        # Gerando dicionário com as informações
        
        return self.extraindo_dados(soup=soup)
    
if __name__ == "__main__":
    bot = WebDriver()
    bot.Scraping_Zap(url='https://www.zapimoveis.com.br/venda/galpao-deposito-armazem/rj+rio-de-janeiro+zona-norte+s-cristovao/?__ab=seo-texts:control,exp-aa-test:control,deduplication:select,new-area-logada:variant,preco-metro-quadrado:deslog&transacao=venda&onde=,Rio%20de%20Janeiro,Rio%20de%20Janeiro,Zona%20Norte,S%C3%A3o%20Crist%C3%B3v%C3%A3o,,,neighborhood,BR%3ERio%20de%20Janeiro%3ENULL%3ERio%20de%20Janeiro%3EZona%20Norte%3ESao%20Cristovao,-22.899642,-43.222749,&tipos=galpao_comercial&pagina=1')
