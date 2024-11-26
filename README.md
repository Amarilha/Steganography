# Aplicativo de Esteganografia com Interface Gráfica

Este projeto é uma aplicação gráfica que utiliza **Python**, **Tkinter** e a biblioteca **Stegano** para realizar esteganografia em imagens. A esteganografia é a prática de esconder informações dentro de outras mídias, como imagens, permitindo que mensagens sejam embutidas de maneira discreta.

---

## Funcionalidades

- **Carregar Imagem**: Permite selecionar uma imagem no formato `.png` ou `.jpg` para esconder ou revelar dados.
- **Esconder Dados**: Insira uma mensagem de texto para ser ocultada dentro da imagem.
- **Exibir Dados Ocultos**: Revela uma mensagem que foi previamente embutida em uma imagem.
- **Salvar Imagem**: Salva a imagem com a mensagem escondida no formato `.png`.

---

## Pré-requisitos

### Dependências

1. **Python 3.x**: Certifique-se de ter o Python instalado no sistema.
2. **Bibliotecas Python**:
   - **Pillow** (para manipulação de imagens):
     ```bash
     pip install pillow
     ```
   - **Stegano** (para esteganografia):
     ```bash
     pip install stegano
     ```

---

## Como Usar

### 1. Executar o Aplicativo
- Execute o script Python no terminal ou IDE de sua escolha:
  ```bash
  python steganography_app.py
  ```

### 2. Passos para Esconder Dados
1. Clique em **Open Image** para selecionar a imagem onde deseja ocultar a mensagem.
2. Digite a mensagem no campo de texto à direita.
3. Clique em **Hide Data** para esconder a mensagem na imagem selecionada.
4. Clique em **Save Image** para salvar a nova imagem com a mensagem oculta.

### 3. Passos para Exibir Dados Ocultos
1. Clique em **Open Image** para selecionar uma imagem que contenha dados ocultos.
2. Clique em **Show Data** para revelar a mensagem oculta, que será exibida no campo de texto à direita.

---

## Estrutura do Código

1. **Interface Gráfica com Tkinter**:
   - Janelas, botões e caixas de texto criadas para interação do usuário.
2. **Biblioteca Stegano**:
   - Funções `lsb.hide()` e `lsb.reveal()` usadas para esconder e revelar mensagens em imagens.
3. **Manipulação de Imagens com Pillow**:
   - Para exibir as imagens carregadas no aplicativo.

---

## Arquitetura do Aplicativo

### Componentes da Interface:

1. **Quadro Principal**:
   - Permite visualizar a imagem selecionada.
2. **Área de Texto**:
   - Campo para inserir ou visualizar mensagens ocultas.
3. **Botões**:
   - **Open Image**: Seleciona a imagem para processar.
   - **Save Image**: Salva a imagem com os dados escondidos.
   - **Hide Data**: Embute a mensagem na imagem.
   - **Show Data**: Revela a mensagem oculta na imagem.

---

## Possíveis Melhorias

- **Suporte a outros formatos de imagem** como `.bmp` ou `.gif`.
- **Criptografia adicional** para proteger a mensagem embutida.
- **Indicação visual** para confirmar que a mensagem foi embutida ou revelada com sucesso.
- **Função para limpar a mensagem embutida** sem alterar a imagem original.

---

## Licença

Este projeto é open-source e está disponível sob a licença MIT. Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo.

---

## Agradecimentos

- **Tkinter** por fornecer as ferramentas para criar interfaces gráficas.
- **Stegano** por tornar a implementação da esteganografia simples e eficiente.
- **Pillow** por facilitar a manipulação e exibição de imagens.

## Layout

![layout Lonig1](https://github.com/Amarilha/Steganography/blob/main/image/Layout_Steganography.png)
