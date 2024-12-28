# Português (english below)

### O que é?
Simple web scraping to detect if the Boosteroid gift card is available on GiftCardPro.

Web scraping simples pra detectar se o gift card do Boosteroid está disponivel no GiftCardPro.

### Como usar?
Tenha certeza de que está usando Linux, e tem o notify-send (Fedora vem com ele instalado, por exemplo)

1. Baixe o repositório: `git clone https://github.com/om1cael/giftcardpro-scraping.git && cd giftcardpro-scrapping`
2. Rode o script em background: `python scrap.py &`

A partir daí, o script vai rodar em background e, a cada 1 hora, vai fazer a checagem. Se o gift card estiver disponível, ele vai te mandar uma notificação.

# English

### What is it
Simple web scraping to detect if the Boosteroid gift card is available on GiftCardPro.

### How to use
Make sure you are using Linux and notify-send is available (Fedora has it by default).

1. Clone the repository: `git clone https://github.com/om1cael/giftcardpro-scraping.git && cd giftcardpro-scrapping`
2. Run script on the background: `python scrap.py &`

Then, it will run on the background and, each hour, it will check if the gift card is available. If so, it will send you a notification.
