# insta-charger

Um coletor que busca os posts recentes de vários perfis do Instagram de locais em Fortaleza - CE e gera um relatório com métricas e informações relevantes sobre cada post.

Funciona da seguinte maneira:

1. Lê os nomes de usuário do Instagram de um arquivo texto chamado "agenda.txt".

2. Usa a biblioteca Instaloader para acessar o Instagram e obter os dados dos perfis.

3. Para cada usuário, obtém o post mais recente dentro do mês atual.

4. Extrai informações como número de curtidas, comentários, data e legenda desse post.

5. Salva os resultados em um arquivo "resultados.txt", ordenando os posts pelo número de curtidas.

6. Trata possíveis erros, como perfis inexistentes.

7. Exibe mensagem de conclusão do processo de coleta.

Pode ser útil para a análise de engajamento de influenciadores, concorrentes ou hashtags, permitindo identificar posts de sucesso e tendências.

Os resultados são exibidos em uma ordem dos posts mais curtidos até os menos curtidos. A ideia é auxiliar na tomada de decisão para onde ir em um final de semana com a galera ou com a namorada a partir de informações como URL do flyer da casa de shows e dados de atrações, horários e ingressos disponíveis nesse post.

Para executar a ferramenta, após clonar o repositório, acesse o diretório `insta-charger` e execute o comando:

`python3 insta-charger.py`

Em seguida, o script começa a rodar automaticamente, exibindo a barra de progresso da coleta. Finalizado o procedimento, basta abrir o arquivo resultados.txt para verificar as informações.

Meu nome é Laercio Monteiro, sou policial, engenheiro de software e entusiasta de Segurança da Informação/Ethical Hacking.

💼 Linkedin: https://www.linkedin.com/in/laercio-monteiro

📱 Instagram: https://instagram.com/laercio.monteiro_

📩 E-mail: laercio@betacoding.com.br
