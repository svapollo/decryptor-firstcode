# Projeto - Decoder
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/svapollo/decryptor-firstcode/blob/main/LICENSE)

# Sobre o projeto

Desenvolvido em novembro/2020 usando **Python** durante a seleção para bolsistas do RSI (Residência em Segurança da Informação) enquanto eu estava no 1º semestre do curso, aqui foi minha primeira aplicação de programação fora das atividades curriculares com gabarito.
  
  O desafio consistia em **Descriptografar o seguinte arquivo .txt** [Link do Arquivo no Repositório](https://github.com/svapollo/decoder-firstcode/blob/main/codigo.txt "Link rápido") e encontrar a Flag, referência aos eventos de CTF (Capture the Flag)
 
# Desafio

![desafio](https://github.com/svapollo/decoder-firstcode/blob/main/assets/desafio.png) 

## Construção da solução

      Entendendo o padrão
- Respondi usando Soma e Produto
- MMC
- Eliminei a opção que estava em negativo
- Encontrando o número ordinário indicando a Letra do alfabeto correspondente

![entendendo](https://github.com/svapollo/decoder-firstcode/blob/main/assets/entendendo.png) 

    Fiz o algoritmo para chegar ao número sem precisar fazer no papel cada calculo
    
![2c](https://github.com/svapollo/decoder-firstcode/blob/main/assets/2c.jpg) 

    Número ordinário 1 corresponde a 1ª letra do Alfabeto e ao código 3
    
![3c](https://github.com/svapollo/decoder-firstcode/blob/main/assets/3c.jpg) 

    Algoritmo para decodificar
    
![4c](https://github.com/svapollo/decoder-firstcode/blob/main/assets/4c.jpg) 

    Dei F5
    
![5c](https://github.com/svapollo/decoder-firstcode/blob/main/assets/5c.jpg) 

    E assim substitui o conteúdo do arquivo recebido.
    
O código da fonte de solução está [Link do Arquivo no Repositório](https://github.com/svapollo/decoder-firstcode/blob/main/decryptor.py "Link rápido") e o txt com o texto decodificado [Link do Arquivo no Repositório](https://github.com/svapollo/decoder-firstcode/blob/main/decrypted.txt "Link rápido")

A atualização utilizando os conhecimentos adquiridos de Novembro/2020 para cá **está em produção**.
