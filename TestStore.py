#Marcelo Aguiar Coelho de Moura Filho
## para rodar os testes, digitar no terminal: python TestStore.py -v
## ou rodar este arquivo em uma IDE python. Os arquivos basePage.py e storePage.py devem estar na mesma pasta deste arquivo.
## versão do selenium selenium==3.141.0
## Python 3.8.1

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from storePage import StorePage
import time
import warnings
from selenium.webdriver.chrome.options import Options

class TesteStore(unittest.TestCase):
        def setUp(self):
            options = webdriver.ChromeOptions()
            #esta linha abaixo serve para não poluir a tela do console com logs não relacionado aos testes
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            #caso o avaliador deseje ver o browser realizando as ações na tela, basta comentar as duas linhas abaixo
            options.add_argument('headless')
            options.add_argument('--window-size=1920,1080')  
            #quando o avaliador for rodar o teste, é necessário retirar o primeiro parâmetro da instância do webdriver e colocar o chromedriver no /bin do seu SO
            #outra opção, é o avaliador colocar o diretório do chromedriver de sua máquina
    
            self.driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\motoProgramTest\\question5\\chromedriver.exe", options=options)
        
        def testAccessIceCreamStore(self):
            "Caso de teste #1"
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.enter_restaurants()
            time.sleep(5)
            page.choice_icecream()
            time.sleep(5)
            assert page.get_sorveteria_description().is_displayed()
            assert page.get_texto_sorveteria() == "A Ice Cream é uma sorveteria inovadora."
        
        def testAddTwoItens(self):
            "Caso de teste #2"
            #Acredito que possa haver uma falha na documentação deste caso de teste
            #A Soma do valor total dos picolés de chocolate deveriam ser 17 reais,
            #no entanto, o resultado esperado é de 7 reais
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.enter_restaurants()
            time.sleep(3)
            page.choice_icecream()
            time.sleep(3)
            page.get_sorvete_brigadeiro()
            time.sleep(3)
            page.get_sorvete_brigadeiro()
            time.sleep(3)
            self.assertEqual(page.check_dois_sorvetes_chocolate(), '(2x) Picolé de Brigadeiro')
            self.assertEqual(page.get_total_value(), 'R$ 7,00')

        def testRemoverItem(self):
            "Caso de teste #3"
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.enter_restaurants()
            time.sleep(3)
            page.choice_icecream()
            time.sleep(3)
            page.get_sorvete_brigadeiro()
            time.sleep(3)
            page.get_sorvete_brigadeiro()
            time.sleep(3)
            page.fechar_pedido()
            time.sleep(10)
            page.retirar_um_sorvete()
            
            time.sleep(3)
            self.assertEqual(page.get_texto_valor_itens(), "Itens:")
            self.assertEqual(page.get_valor_total_itens(), "R$ 8,50")
            
            self.assertEqual(page.get_texto_frete(), "Frete:")
            self.assertEqual(page.get_valor_frete(), "R$ 8,00")
            

            self.assertEqual(page.get_texto_valor_total(), 'Total:')
            self.assertEqual(page.get_valor_total_total_frete_mais_itens(), 'R$ 16,50')

        def testConcluirPedido(self):
            "Caso de teste #4"
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            time.sleep(3)
            page.enter_restaurants()
            time.sleep(3)
            page.choice_icecream()
            time.sleep(3)
            page.get_sorvete_brigadeiro()
            time.sleep(6)
            page.fechar_pedido()
            time.sleep(5)
            self.assertFalse(page.check_fechar_pedido_not_enabled().is_enabled())

        def test_preencher_formulario_erroneamente(self):
            "Caso de teste #5"
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.enter_restaurants()
            time.sleep(3)
            page.choice_icecream()
            time.sleep(3)
            page.get_sorvete_brigadeiro()
            time.sleep(6)
            page.fechar_pedido()
            time.sleep(5)
            page.preencher_campo_nome('Ana')
    
            page.preencher_campo_email('ana@gmail')
            page.confirmar_campo_email('ana@gmail')

            page.preencher_campo_endereco('Rua')

            page.preencher_campo_numero('abc')

            self.assertEqual(page.mensagem_de_erro_campo_nome().text, "Campo obrigatório e com 5 caracteres")
            assert page.mensagem_de_erro_campo_nome().is_displayed

            self.assertEqual(page.mensagem_de_erro_campo_email().text, "E-mail inválido")
            assert page.mensagem_de_erro_campo_email().is_displayed

            self.assertEqual(page.mensagem_de_erro_campo_numero().text, "Obrigatório e somente números")
            assert (page.mensagem_de_erro_campo_numero().is_displayed)
        

        def test_verificar_redirect_sobre(self):
            'Caso de teste #6'
            ''' cenário:  usuário está logado na página do iFrame Bom e clica em "sobre"'''
            ''' resultado esperado: usuário é fica na url http://training-wheels-protocol.herokuapp.com/nice_iframe e é exibido "Sobre" dentro do container'''
        
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            self.driver.implicitly_wait(3)
            page.botao_sobre()
            time.sleep(4)
            self.assertEqual(self.driver.current_url,"http://training-wheels-protocol.herokuapp.com/nice_iframe")
            self.assertEqual(page.texto_sobre().text, "Sobre")
            assert page.texto_sobre().is_displayed()

        def test_entrar_loja_de_cafe(self):
            'Caso de teste #7'
            '''cenário: usuário está logado na página do iFrame Bom e clica em resturantes. Em seguida, clica em Coffe Corner'''
            '''resultado esperado: é exibido na tela o texto " Coffee Corner" para o usuário'''
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            self.driver.implicitly_wait(3)
            page.enter_restaurants()
            self.driver.implicitly_wait(3)
            page.entrar_pagina_cafe()
            time.sleep(3)
            self.assertEqual(page.nome_pagina_cafe().text,"Coffee Corner" )
            assert page.nome_pagina_cafe().is_displayed()
        
        def test_comprar_cappuccino_com_chantilly(self):
            'Caso de teste #8'
            '''cenário: usuário está logado na página do iFrame Bom e clica em restaurantes. Em seguida, clica em Coffe Corner
            depois clica em "Adicionar" dentro da div do CAPPUCCINO COM CHANTILLY'''

            '''resultado esperado: "(1x) Cappuccino com Chantilly" é exibido em sua tela'''

            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.enter_restaurants()
            self.driver.implicitly_wait(3)
            page.entrar_pagina_cafe()
            page.adicionar_cafe_chantili()
            time.sleep(3)
            self.assertEqual(page.cafe_adicionado().text, "(1x) Cappuccino com Chantilly")

            time.sleep(3)

        
        def test_limpar_campo_carrinho(self):
            'Caso de teste #9'
            '''cenário: usuário está logado na página do iFrame Bom e clica em restaurantes. Em seguida, clica em Coffe Corner
            depois clica em "Adicionar" dentro da div do CAPPUCCINO COM CHANTILLY. Após isto, clica em Limpar'''

            '''resultado esperado: Cappuccino com Chantilly não é mais exibido na tela '''
            
            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.enter_restaurants()
            self.driver.implicitly_wait(3)
            page.entrar_pagina_cafe()
            page.adicionar_cafe_chantili()
            time.sleep(3)
            page.retirar_cafe()
            time.sleep(5)
            self.assertFalse("(1x) Cappuccino com Chantilly" in self.driver.page_source)
            self.assertTrue("Seu carrinho está vazio!" in self.driver.page_source)
        

        def test_clicar_em_enjoy_eat(self):
            'Caso de teste #10'
            '''cenário: usuário está logado na página do iFrame Bom e clica em "EnjoyEat"'''
            '''resultado esperado: deve ser exibido um botão escrito "Restaurantes"'''

            page = StorePage(self.driver)
            page.openpage()
            page.switchframe()
            page.maxwindow()
            page.clicar_enjoyeat()
            self.assertEqual(page.botao_restaurantes().text, 'Restaurantes')
            self.assertTrue(page.botao_restaurantes().is_displayed())


if __name__=="__main__":
    #suite = unittest.TestLoader().loadTestsFromTestCase(TesteStore)
    #unittest.TextTestRunner(verbosity=1).run(suite)
    #unittest.main()
    with warnings.catch_warnings():
        #warnings.simplefilter('ignore', category=ImportWarning)
        #utilizei esta lib pra não poluir a tela com informações desnecessárias
        warnings.simplefilter('always', DeprecationWarning)
        unittest.main()