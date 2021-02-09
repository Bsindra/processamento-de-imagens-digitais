# Processamento de Imagens Digitais
Aplicação em Python de OpenCV e Numpy para classificação de objetos em movimento de acordo com seu tamanho relativo a uma área de interesse.

[DEMO](https://youtu.be/dXddP89l0EI)

Instruções para customização do programa no fim do readme.

# Instalação e Execução (Sistemas Baseados em Linux)

## Clonando o Repositório
  
    $git clone https://github.com/Bsindra/processamento-de-imagens-digitais
  
## Instalando as dependências

    $cd processamento-de-imagens-digitais
    $sudo chmod +x setup.sh
    $./setup.sh
    
## Execute a aplicação

    &./main.py
    
# Instalação e Execução (Windows)

## Instalando as dependências

    Execute o arquivo setup_windows.sh
    (Isso irá executar seu navegador padrão para realizar o download dos pesos do YOLO v4. (aprox. 246MB))
    
## Execute a aplicação
  
    Execute o arquivo windows.sh
    (É necessário ter o python instalado e configurado no seu computador, 
    caso não o tenha o download pode ser realizado aqui: https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe)
    
# Customização

    Para mudar o arquivo fonte basta substituir o arquivo 'source.mp4' dentro do diretório.
    Todas as informações necessárias para que o programa seja executado normalmente serão extraídas do arquivo fonte.
    
    Ao executar o script serão dadas opções para selecionar a Região de Interesse e o tamanho mínimo do "Alvo".
    A primeira área deve obrigatóriamente ser demarcada, o tamanho mínimo pode ser ignorado pressionando-se "Esc".
    
    
### Autor

 <a href="https://github.com/Bsindra">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/78266135?s=460&u=467052ab9311be4a9b3a0aca9cfde718318c4cbe&v=4" width="100px;" alt=""/><br />
 <sub><b>Bryan Sindra </b></sub></a> <a href="https://github.com/Bsindra" title="GitHub"></a>


Entre em contato:

[![Linkedin Badge](https://img.shields.io/badge/-Bryan-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/bryan-sindra/)](https://www.linkedin.com/in/bryan-sindra/) 
[![Gmail Badge](https://img.shields.io/badge/-bsindra98@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:bsindra98@gmail.com)](mailto:bsindra98@gmail.com)
