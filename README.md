# Automatização de Pedidos de Dietas
Automação num sistema simples em python, com a biblioteca pyautogui e Selenium, para automatizar o pedido de dietas em um hospital em que trabalhei.

## Introdução
Um princípio básico de qualquer profissional orientado à eficiência é a automação. Visto que percebi rapidamente a natureza repetitiva deste elemento de um cargo em que trabalhei, desenvolvi uma automação usando bibliotecas em Python para fazer os pedidos de dieta num sistema em Flash próprio deste hospital.

## Bibliotecas necessárias
* Pyautogui
* Selenium (incluindo acesso ao chromedriver adequado à versão do navegador)

## Desafio
Todo dia, neste hospital, é necessário fazer um pedido de dieta para os acompanhantes. Visto que todo paciente do setor pediátrico, onde estamos localizados, sempre possui um acompanhante, não há necessidade de uma conferência manual de quem precisa de dieta ou não. Isso significa que o sistema pode ser automatizado. No entanto, para complicar a situação, é usado um modelo de navegador específico, chamado CentBrowser, baseado no Chrome. Além disso, o sistema de pedido de dieta é desenvolvido em Adobe Flash, impedindo o acesso a trechos específicos de código como seria possível em HTML. Como facilitar o trabalho com automação e, assim, dedicar nossas energias a outras atividades mais úteis ao hospital??

## Solução
O acesso ao Browser é similar ao acesso ao Chrome, usando da biblioteca Selenium para gerenciar o driver do chrome e entrar no site específico. No entanto, visto que não é possível coletar dados dos elementos do site, o que permitiria uma automação mais eficaz com o próprio Selenium, o pyautogui é a solução mais eficiente, clicando em elementos fixos para fazer o login no site (em arquivo à parte, para garantir a segurança) e clicar nos botões, links e trechos de formulário para fazer o login, o pedido de dieta e transitar entre os pacientes. A lógica de programação funciona com um loop para avançar pela tela, incluindo uma verificação da presença de pacientes suficientes para ser necessária a rolagem da tela.

## Proposta de melhoria futura
Maior pesquisa na documentação do pyautogui pode permitir melhor entendimento de como fazer o acesso dos dados, coletando mais informações sobre os pacientes e permitindo uma escolha de quais receberão dieta ou não. Isso permitiria o uso do sistema para setores do hospital que não necessitam de pedido de acompanhante para todos os pacientes internados. Além disso, maior responsividade é necessária para que o sistema possa ser usado em monitores de diferentes resoluções.

## Conclusão
O sistema é eficaz dentro de sua proposta e consegue facilitar o trabalho e reduzir o tempo perdido com tarefas repetitivas e facilmente realizáveis pelo computador. A automação de tarefas é um dos pontos fortes da linguagem Python e muito auxiliar neste processo. Com o tempo economizado, podemos priorizar tarefas menos repetitivas e que exigem uma análise humana.
