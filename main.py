import requests
from bs4 import BeautifulSoup

print(
  'INFORMATIVO \n'
  'Subgrupos: B1, B2, B3, B4a, B4b \n'
  'Classificação: \nB1 => Residencial Normal - Residencial Baixa Renda até 30kWh - Residencial Baixa Renda de 31 a 100kWh - Residencial Baixa Renda de 101 a' '220kWh - Residencial Baixa Renda acima de 220kWh. \nB2 => Rural, não cooperativa - Cooperativa de Eletrificação - Serviço Público de Irrigação. \nB3 => '
  'Água, Esgoto e Saneamento - Demais Classes. \nB4a => Iluminação Pública - Rede de Distribuição. \nB4b => Iluminação Pública - Bulbo da Lâmpada'
)

subgrupo = str(input('Digite o subgrupo: '))
classificacao = str(input('Digite a classificação: '))

def obterHtmlSite():
  url = 'https://www.celesc.com.br/tarifas-de-energia'
  resposta = requests.get(url)

  if resposta.status_code == 200:
    html = resposta.content
    soup = BeautifulSoup(html, 'html.parser')
    linhasTabela = soup.find_all('tr')

    for linha in linhasTabela:
      coluna = linha.find_all('td')
      if coluna[0].text.strip() == subgrupo:
        if coluna[1].text.strip() == classificacao:
          valorKwh = coluna[2].text.strip()
          return 'O valor do kwh para a classificação {} é {}'.format(classificacao, valorKwh)

      if coluna[0].text.strip() == classificacao:
        valorKwh = coluna[1].text.strip()
        return 'O valor do kwh para a classificação {} é {}'.format(classificacao, valorKwh)
      
    return 'Nenhum valor encontrado para o subgrupo {} e a classificação {}'.format(subgrupo, classificacao)
  else:
    return 'Não foi possível encontrar o site informado'
  
print(obterHtmlSite())