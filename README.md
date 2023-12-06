# 📊 Analisando Postagens do HackerNews 📊

## Motivação: 

Você conhece o site [HackerNews](https://news.ycombinator.com/)? É um espaço onde as pessoas compartilham e comentam sobre temas como tecnologia, programação, empreendedorismo e muito mais. Se você quer usar esse site para fazer perguntas ou mostrar algum projeto para a comunidade, 
você pode aprender com as postagens anteriores como aumentar o seu engajamento e participação. Por exemplo, você pode descobrir quais são os melhores horários para tirar uma dúvida ou então apresentar algo e ter maiores chances de gerar engajamento em sua postagem. 

## Sobre o projeto:

Neste trabalho, vamos explorar dois tipos de publicações do HackerNews. Os tipos de publicações que vamos investigar são os Ask HN e os Show HN, publicações onde os usuários fazem uma questão específica para a comunidade ou onde eles apresentam um projeto, produto ou algo interessante para a comunidade, respectivamente.

Em nossa pesquisa, queremos responder as seguintes questões:

- Qual tipo de publicação costuma receber mais comentários?
- O horário da publicação influencia o número de interações?
- Existem horários em que há maior competição na visibilidade de uma publicação?
- Existem horários melhores para tirar dúvidas com a comunidade?
- A comunidade tem mais interesse publicações do tipo ASK ou SHOW?
- Existem horários melhores para mostrarmos algo para a comunidade?

Aqui estou usando um conjunto de dados baixados do [Kaggle](https://www.kaggle.com/). O CSV que estou usando é um subconjunto feito por mim do original, no qual estou apenas com publicações cujo número de comentários é maior que zero e os tipos de publicação são Ask HN e Show HN. O original pode ser baixado [aqui](https://www.kaggle.com/datasets/santiagobasulto/all-hacker-news-posts-stories-askshow-hn-polls).

Neste trabalho, realizamos etapas de filtragem do conjunto de dados em subconjuntos, classificação das publicações em faixas de hora ao longo do dia, cálculo das médias de comentários por publicação nas faixas de hora ao longo do dia e cálculo de pontuação média de publicações nas mesmas faixas de hora. Também produzimos tabelas e gráficos para visualizar as informações e fizemos as análises de padrões e também conclusões sobre a informação que trabalhamos.

Obs.: Todos os horários estão na Hora Padrão do Leste (Eastern Standard Time) EST: UTC-5.

## Conclusão: 

- Os posts do tipo ASK tendem a receber mais comentários do que os posts do tipo SHOW, indicando que eles provocam mais interação e discussão na comunidade do hackernews. A média de comentários por post do tipo ASK é de 15,56, enquanto a média de comentários por post do tipo SHOW é de 12,32. Esta conclusão é intuitiva, dada a finalidade da postagem.
- O horário do post influencia o número de interações, tanto em termos de quantidade de posts quanto de média de comentários e pontos. Há alguns horários que se sobressaem por terem mais atividade e interação do que outros, dependendo do tipo de post.
- Para os posts do tipo ASK, os horários com mais posts são entre as 15:00 e as 18:00, sendo esse o período de maior competição pela visibilidade de uma postagem. No entanto, o horário com a maior média de comentários é às 15:00 (26,14), indicando que esse é o melhor horário para fazer perguntas à comunidade. Outra alternativa é entre os horários 10:00 e 12:00, que têm um número de interações acima da média e ainda têm poucas postagens sendo criadas, indicando um horário ativo e com baixa concorrência de atenção dos outros usuários. Os horários com as menores médias de comentários são a partir das 19:00, sugerindo que esse é o pior horário para publicar uma pergunta no hackernews. A madrugada também não é um horário recomendado, a atividade tende a crescer somente no início da manhã, a partir das 06:00
- As postagens do tipo SHOW ganham muito mais pontos do que as postagens do tipo ASK, mostrando que elas são mais apreciadas e valorizadas pela comunidade do hackernews. Isso pode ser porque as postagens do tipo SHOW geralmente mostram projetos, produtos ou algo interessante que os usuários fizeram ou acharam, enquanto as postagens do tipo ASK são mais para fazer perguntas ou pedir ajuda.
- Para os posts do tipo SHOW, podemos observar que o intervalo entre 11:00 e 15:00 tem os melhores índices de média de comentários e de pontos recebidos, mostrando que é o horário em que a comunidade está mais ativa para interagir, se interessar e gerar maior visibilidade às postagens. No entanto, há uma intersecção com os horários em que há mais posts sendo feitos, compreendido entre 13:00 e 17:00. O usuário pode aproveitar os intervalos de 11:00 e 12:00 para fazer um post e ter menos competição de atenção (inclusive esses horários têm as maiores médias, mesmo entre 11:00 e 15:00). Depois das 18:00 e também no início da manhã não são bons horários para apresentar conteúdo à comunidade.




