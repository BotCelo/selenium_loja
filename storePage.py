#Marcelo Aguiar Coelho de Moura Filho

from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import Page
import time 
class StorePage(Page):


    dic = {
            'restaurantes': (By.XPATH, '//*[@id="navbar-collapse"]/ul/li[1]/a'),
            'iframe': (By.XPATH,'//*[@id="burgerId"]'),
            'sorveteria': (By.XPATH, '/html/body/mt-app/div/div/div/mt-restaurants/section[2]/div/div[5]/mt-restaurant/a/div/div/span[1]'),
            'textsorveteria': (By.XPATH, '//*[@id="detail"]/dd[2]'),
            'doispicolesbrigadeiro':(By.XPATH, '//*[@id="cart"]/div[2]/div/table/tbody/tr[1]/th'),
            'addsorvetebrigadeiro': (By.XPATH, "/html/body/mt-app/div/div/div/mt-restaurant-detail/section[2]/div[2]/mt-menu/div[1]/mt-menu-item[2]/div/div/a"),
            'itenschart': (By.XPATH, "//*[@id='cart']/div[2]/div/table/tbody/tr[1]/th"),
            'pricebuy':(By.XPATH, "//*[@id='cart']/div[2]/div/table/tbody/tr[2]/td"),
            'fecharpedido':(By.XPATH, "//*[@id='cart']/div[3]/div/a"),
            'retirarsorvete': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[4]/mt-order-items/div/table/tbody/tr/td[1]/a[1]/i"),
            'valoritens': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[5]/div[2]/mt-delivery-costs/div/table/tbody/tr[1]/td"),
            'textoprecototal':(By.XPATH,"//*[@id='cart']/div[2]/div/table/tbody/tr[2]/td"),
            'valorfrete': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[5]/div[2]/mt-delivery-costs/div/table/tbody/tr[2]/td"),
            'textofrete': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[5]/div[2]/mt-delivery-costs/div/table/tbody/tr[2]/th"),
            'textovaloritens': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[5]/div[2]/mt-delivery-costs/div/table/tbody/tr[1]/th"),
            'valortotaltexto': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[5]/div[2]/mt-delivery-costs/div/table/tbody/tr[3]/th"),
            'valor_total_mais_frete':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[5]/div[2]/mt-delivery-costs/div/table/tbody/tr[3]/td"),
            'botao_concluir_pedido': (By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/div/div/button"),
            'nome':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[2]/div[3]/mt-input-container/div/input"),
            'email':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[2]/div[4]/mt-input-container/div/input"),
            'confirmemail':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[2]/div[5]/mt-input-container/div/input"),
            'endereco':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[3]/div[2]/mt-input-container/div/input"),
            'numero':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[3]/div[3]/mt-input-container/div/input"),
            'mensagemerronome':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[2]/div[3]/mt-input-container/div/span"),
            'mensagemerroemail':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[2]/div[4]/mt-input-container/div/span"),
            'mensagemerronumero':(By.XPATH, "/html/body/mt-app/div/div/div/mt-order/section[2]/section/form/div[3]/div[3]/mt-input-container/div/span"),
            'paginacafe':(By.XPATH, "/html/body/mt-app/div/div/div/mt-restaurants/section[2]/div/div[3]/mt-restaurant/a/div/div/span[3]"),
            'cafenomepagina':(By.XPATH, '//*[@id="restaurant"]/div[1]/h3'),
            'botaosobre':(By.XPATH, '//*[@id="navbar-collapse"]/ul/li[2]/a'),
            'textosobre': (By.XPATH, '/html/body/mt-app/div/div/div/mt-about/section[1]/h1'),
            'cafechantili':(By.XPATH, '/html/body/mt-app/div/div/div/mt-restaurant-detail/section[2]/div[2]/mt-menu/div[1]/mt-menu-item[1]/div/div/a'),
            'quantidadechantili':(By.XPATH, '//*[@id="cart"]/div[2]/div/table/tbody/tr[1]/th'),
            'retirarcafe':(By.XPATH, '//*[@id="cart"]/div[2]/div/table/tbody/tr[1]/td[2]/a/i'),
            'enjoyeat': (By.XPATH, '/html/body/mt-app/div/mt-header/header/nav/div/div[1]/a/img'),
            'botaoresturantes':(By.XPATH, '/html/body/mt-app/div/div/div/mt-home/section[2]/div/a'),
    }

    def __init__(self, selenium_driver, base_url='http://training-wheels-protocol.herokuapp.com/nice_iframe'):
        Page.__init__(self, selenium_driver) 
        self.url = ''
 
    # Actions

    def openpage(self):
        self.get_page(self.url)

    def switchframe(self):
        self.switch_frame(*self.dic['iframe'])

    def enter_restaurants(self):
        time.sleep(10)
        self.find_element(*self.dic['restaurantes']).click()

    def choice_icecream(self):
        self.find_element(*self.dic['sorveteria']).click()

    def get_sorveteria_description(self):
       return self.find_element(*self.dic['textsorveteria'])

    def get_texto_sorveteria(self):
        return self.find_element(*self.dic['textsorveteria']).text

    def get_texto_total(self):
        return self.find_element(*self.dic['textoprecototal']).text

    def get_sorvete_brigadeiro(self):
        self.find_element(*self.dic['addsorvetebrigadeiro']).click()

    def check_itens_chart(self):
        return self.find_element(*self.dic['itenschart']).text

    def check_dois_sorvetes_chocolate(self):
        return self.find_element(*self.dic['doispicolesbrigadeiro']).text

    def get_total_value(self):
        return self.find_element(*self.dic['pricebuy']).text

    def fechar_pedido(self):
        return self.find_element(*self.dic['fecharpedido']).click()
    
    def retirar_um_sorvete(self):
        return self.find_element(*self.dic['retirarsorvete']).click()


    def get_texto_valor_itens(self):
        return self.find_element(*self.dic['textovaloritens']).text

    def get_valor_total_itens(self):
        return self.find_element(*self.dic['valoritens']).text
    

    def get_texto_frete(self):
        return self.find_element(*self.dic['textofrete']).text

    def get_valor_frete(self):
        return self.find_element(*self.dic['valorfrete']).text
    
    def get_texto_valor_total(self):
        return self.find_element(*self.dic['valortotaltexto']).text
    
    def get_valor_total_total_frete_mais_itens(self):
        return self.find_element(*self.dic['valor_total_mais_frete']).text
    
    def check_fechar_pedido_not_enabled(self):
        return self.find_element(*self.dic['botao_concluir_pedido'])

    def preencher_campo_nome(self, valor):
        return self.find_element(*self.dic['nome']).send_keys(valor)

    def preencher_campo_email(self,valor):
        return self.find_element(*self.dic['email']).send_keys(valor)
    
    def confirmar_campo_email(self, valor):
        return self.find_element(*self.dic['confirmemail']).send_keys(valor)
    
    def preencher_campo_endereco(self, valor):
        return self.find_element(*self.dic['endereco']).send_keys(valor)
    
    def preencher_campo_numero(self, valor):
        return self.find_element(*self.dic['numero']).send_keys(valor)
    
    def mensagem_de_erro_campo_nome(self):
        return self.find_element(*self.dic['mensagemerronome'])
    
    def mensagem_de_erro_campo_email(self):
        return self.find_element(*self.dic['mensagemerroemail'])
    
    def mensagem_de_erro_campo_numero(self):
        return self.find_element(*self.dic['mensagemerronumero'])
    
    def entrar_pagina_cafe(self):
        self.find_element(*self.dic['paginacafe']).click()

    def nome_pagina_cafe(self):
        return self.find_element(*self.dic['cafenomepagina'])
    
    def maxwindow(self):
        self.maximize_window()
    
    def botao_sobre(self):
        self.find_element(*self.dic['botaosobre']).click()

    def texto_sobre(self):
        return self.find_element(*self.dic['textosobre'])
    
    def adicionar_cafe_chantili(self):
        return self.find_element(*self.dic['cafechantili']).click()
    
    def cafe_adicionado(self):
        return self.find_element(*self.dic['quantidadechantili'])
    
    def retirar_cafe(self):
        return self.find_element(*self.dic['retirarcafe']).click()
    
    def clicar_enjoyeat(self):
        return self.find_element(*self.dic['enjoyeat']).click()
    
    def botao_restaurantes(self):
        return self.find_element(*self.dic['botaoresturantes'])