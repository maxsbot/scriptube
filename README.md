# Projeto de Download Automatizado de Vídeos do YouTube

Este projeto foi desenvolvido com o objetivo de automatizar o processo de download de vídeos do YouTube com base em uma planilha Excel que contém o nome e a URL de cada vídeo.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python: `pandas` e `pytube`
- Planilha Excel com os nomes e URLs dos vídeos que deseja baixar

## Configuração

1. Instale as dependências do projeto utilizando o seguinte comando:
    ```
    pip install pandas pytube
    ```
2. Organize sua planilha no formato `.xlsx` com os nomes dos vídeos na primeira coluna e as respectivas URLs na segunda coluna. 

## Como obter a planilha com os vídeos

Para obter os dados necessários para a planilha, siga os passos abaixo:

1. Acesse o canal do YouTube do qual deseja baixar os vídeos.
2. Clique na aba "Vídeos".
3. Abra o console (Inspeção de elemento -> Console) no seu navegador.
4. No console, digite o seguinte comando para rolar automaticamente até o final da página:
    ```
    var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);
    ```
5. Quando a página terminar de rolar, interrompa o processo digitando no console:
    ```
    window.clearInterval(scroll);
    ```
6. Em seguida, insira o seguinte comando para obter os títulos e as URLs de cada vídeo:
    ```
    console.clear();
    urls = $$('a');
    urls.forEach(function(v,i,a){if (v.id=="video-title-link" && v.href){console.log('\t'+v.title+'\t'+v.href+'\t')}});
    ```
7. Os dados obtidos devem ser copiados para sua planilha `.xlsx`.

## Uso

Execute o script Python. Será solicitado o caminho completo da planilha e o local onde você deseja que os vídeos sejam armazenados. Informe esses caminhos e o download dos vídeos começará automaticamente.

## Problemas conhecidos e soluções

- Se encontrar algum erro ao tentar baixar um vídeo, certifique-se de que a URL está correta e acessível.
- O nome do vídeo é usado para criar o nome do arquivo. Alguns caracteres especiais não são permitidos em nomes de arquivos e são automaticamente removidos pelo script.

## Contribuindo

Este projeto é de código aberto. Sinta-se à vontade para contribuir com melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a licença MIT.