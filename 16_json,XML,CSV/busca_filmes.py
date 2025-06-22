def get_movies(texto_busca: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


from urllib.parse import quote
def get_movies(texto_busca: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def search_movie(movie_name: dict) -> dict:
 pesquisa = movie_name.get('resultados') #Essa variável pega os valores dentro do json criado em get_movies.
 return get_movies(pesquisa)

nome = input("digite o nome do filme: ")
codifiq = quote(nome) # o 'quote', importado do urllib.parse, foi necessário pra que a pesquisa não desse erro ao escrever um espaço, por exemplo.

resultado = search_movie({'resultados': codifiq})
for f in resultado["description"]: #pra cada filme encontrado na parte 'description' do json (nome do filme, ano, capa, etc), ele pega e printa os valores que estão dentro dela.
    titulo = f.get('#TITLE')
    ano = f.get('#YEAR')
    capa = f.get('#IMG_POSTER')
    print(f"titulo: {titulo} \nano: {ano} \ncapa: {capa}\n")
    
#pra ser sincero, isso daqui não tá completamente perfeito, mas foi o que consegui no momento através de muita pesquisa... e isso me deixa meio mal, parece que não consigo aprender nada.
