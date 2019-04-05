import requests
import json

def main():
        print('###Consulta CEP###')

        cep_input = input('Digite o cep para a consulta :')
        if len(cep_input) != 8:
            print('Quantidade de digitos invalidos !')
            exit()
            
        r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

        addres_data = r.json()
            

        if 'erro' not in addres_data:
            print('==> CEP ENCONTRADO <=')
            
            print('CEP: {}'.format(addres_data['cep']))
            print('logradouro: {}'.format(addres_data['logradouro']))
            print('Complemento: {}'.format(addres_data['complemento']))
            print('Bairro: {}'.format(addres_data['bairro']))
            print('Cidade: {}'.format(addres_data['localidade']))  
            print('Estado: {}'.format(addres_data['uf']))  
   #


if __name__ == "__main__":
    main()