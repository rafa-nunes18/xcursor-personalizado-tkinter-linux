<h1 align="center">Cursores personalilados para Tkinter no Linux</h1>

TkXcursor é uma biblioteca que gerencia cursores ARGB/animados personalizados sob o servidor X.org.
Permitindo que você utilize ponteiros de mouse com suporte a transparência e cores vibrantes em aplicações que usam o Tkinter no Linux.
Isso pode melhorar a estética e a funcionalidade da interface do usuário, permitindo designs mais sofisticados e a possibilidade de criar interações mais visuais.

## TkXcursor demo
![screenshot1](demo/Cursores_demo.gif)

## direitos autorais
O projeto original é de propriedade do sK1Project.

O arquivo original pode ser encontrado no repositório do sK1Project no GitHub, chamado tkxcursor. 

https://github.com/sk1project/tkxcursor

https://sk1project.net

@sK1ProjectOrg

Por se tratar de um projeto de 15 anos atrás, tive que modificá-lo e atualizá-lo para uma versão 2.0 .

## Requisitos do sistema

O TkXcursor, funcionará em distribuições Linux que utilizem o sistema X.org como gerenciador de janelas e que tenham o suporte adequado para as funcionalidades gráficas da biblioteca Tkinter. 
Além disso, verifique se a versão do Python está atualizada. 

## Instruções

Instalação:
   - Baixe todos os arquivos e os coloque em uma pasta.
   - Crie um ambiente virtual a partir do interpretador python instalado no seu PC.
   - Ative seu venv e em um novo terminal, navegue até o diretório da pasta que contém os arquivos baixados. Você pode usar o comando cd para mudar de diretório. Por exemplo:

     cd /caminho/para/o/diretorio
     
   - Use o Pip para executar o arquivo setup.py. Você pode usar o seguinte comando:

     pip install .
     
Existem apenas 3 funções:

   - x_xcursor_suporte:
   
     É uma função opcional que apenas verifica se o sistema suporta cursores ARGB/animados. Passe como argumento qualquer widget, retornando True para sim e False para não.
     
   - x_load_cursor:
     
     Retorna o xid para o Xcursor RGBA/animado personalizado. Passe um widget e o caminho do cursor.
   
   - x_set_cursor:
   
     Define um Xcursor para o widget fornecido. Passe novamente o mesmo widget junto do seu xid.

     Para voltar o cursor padrão use a função config do tkinter para usar o cursor arrow:
     widget.config(cursor="arrow")

O formato do arquivo de cursor: 

   - Somente o cursor criado com xcursorgen irá funcionar. Para mais informações de criação do cursor personalizado, acesse meu repositório criar-xcursor-personalizado-linux.

     https://github.com/rafa-nunes18/criar-xcursor-personalizado-linux

## Finalmente 

Obrigado por ler até aqui. 
Para ver um grande exemplo do uso de tkxcursor, acesse meu primeiro projeto em Phyton .

https://github.com/rafa-nunes18/3-in-1-Tkinter-Themes

Rafael A. Nunes ( rafa.nunes2018@hotmail.com ) 2024

Instagram: @rafa33alves

