import abc, interface_veiculo

class Veiculo (interface_veiculo.InterfaceVeiculo,abc.ABC):
    """Essa é a classe veiculo. Esta classe é utilizada para instanciar novos veiculos"""
    def __init__ (self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0
    
    def __del__ (self):
        print('o objeto foi deletado')

    
    def pintar (self,cor):
        self._cor = cor
    
    def ligar (self):
        if self.__is_ligado == True :
           print('O veiculo ja esta ligado')
        else:
            self.__is_ligado = True
    
    def desligar (self):
        if self.__is_ligado == False :
           print('O veiculo ja esta desligado')
        else:
            self.__is_ligado = False

    @property
    def cor (self):
        return self._cor

    def acelerar (self, velocidade):
        self.__velocidade = velocidade

    
    def abastecer (self, qtd_combustivel):
        self._qtd_combustivel += qtd_combustivel
