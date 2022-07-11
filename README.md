# Terminal File Transfer
## Trabalho Final - MATA49
### Grupo:

- Felipe Carvalho Passos
- Douglas

O projeto trata de um sistema para depósito e recuperação de arquivos em servidores remotos.

No **modo de depósito**, o cliente é capaz de depositar um arquivo com qualquer extensão, informando também o nível de tolerância a falhas desejado.

O nível de tolerância dita a quantidade de cópias a serem feitas nos servidores satélites. Por exemplo, um arquivo com nível de tolerância 3 deve ser depositado em três servidores satélites.

OBS: A quantidade máxima de servidores satélites que podem ser abertos é informada na variável MAX_SATELLITE_INSTANCES do projeto file-satellite-server.

Toda vez que um arquivo é depositado, primeiro limpamos qualquer cópia pré existente nos servidores. Isso serve para garantir que o número de cópias esteja consistente com a última solicitação do cliente.

No **modo de recuperação**, o servidor principal retorna o arquivo do primeiro servidor satélite que o contém. Por exemplo, se um arquivo "file.txt" está armazenado em três servidores satélites diferentes, quando o servidor principal encontra a primeira cópia ele a retorna para o cliente e finaliza a execução. Caso não encontre o arquivo, informa ao cliente.

### Tecnologia

O projeto utiliza como linguagem o python >= 3. A comunicação é feita através de socket, tendo   implementados métodos de baixo nível para tal comunicação, e utilizando confirmação interna dos dados.

### Estrutura

O projeto é separado em três módulos.

- O módulo de cliente é resposável por interagir com o usuário, através dos modos de recuperação e de depósito. Ele se comunica diretamente com o módulo de servidor principal, enviando os dados nececssários para execução das rotinas.

- O módulo de servidor principal é resposável por distribuir e recuperar os arquívos dos servidores satélites, nele é feita a verficicação de tolerância e sua correção.

- O módulo de servidor satélite serve para depositar e os arquívos, que posteriormente poderá ser recuperado pelo módulo de servidor principal.

### Execução do sitema

Para que o funcionamento do sistema, é necessário que os módulos de client, servidor principal e servidor satélite estejam em execução. Os servidores satélites podem estar sendo execultados em várias instancias, onde cada um terá uma porta definida para o recebimento e envio do arquivo.

A execução do sistema é simples, após ter o python instalado na máquina, basta executar o comando 'python main.py', no terminal, no diretório de cada um dos módulos.

As instâncias dos servidores satélites podem ser ser criadas a partir da cópia da pasta do projeto. Cada pasta será uma instância, e assim, executando o comando para cada diretório será criadas instâncias dos servidores, onde as portas de conexão serão selecionadas automaticamente para cada uma.

### Modo de depósito

Para o modo depósito é necessário colocar o arquivo dentro da pasta 'uploads', que está dentro da pasta do projeto. Após isto, e com o sistema rodando corretamente, no cliente, utilize a opção '1 - Depósito', após isto siga as intruções do terminal, informando o nome do arquivo, com extensão, e depois disto informe a tolerância. Feito isto, o seu arquivo será depositado em alguns dos servidores satélites, podendo ser verificado em suas pastas.

### Modo de recuperação

Para o modo de recuperação, é necessário apenas informar no terminal do cliente o nome do arquivo, junto com a estesão, que deseja recuperar. Assim o arquivo será recuperado, e salvo na pasta 'downloads'.