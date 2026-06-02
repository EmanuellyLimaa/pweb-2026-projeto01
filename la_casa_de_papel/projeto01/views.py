from django.shortcuts import render

site = {
    "título": "La Casa de Papel",
    "descricao": "Site oficial do elenco da série La Casa de Papel",
    "ano": 2026,
    "autores": ["Emanuelly Maria", "Almira Beatriz"]
}

elenco = [
    "nome": "Professor", "idade": 45, "posicao": "Líder", "nascimento": "Espanha", "foto": "professor.webp",
    "nome": "Tóquio", "idade": 34, "posicao": "Narradora", "nascimento": "Brasil", "foto": "tokio.webp",
    "nome": "Rio", "idade": 25, "posicao": "Hacker", "nascimento": "Brasilo", "foto": "rio.webp",
    "nome": "Nairobi", "idade": 30, "posicao": "Especialista", "nascimento": "Quênia", "foto": "nairobi.webp",
    "nome": "Moscú", "idade": 40, "posicao": "Operações", "nascimento": "Rússia", "foto": "moscú.webp",
    "nome": "Professor", "idade": 45, "posicao": "Líder", "nascimento": "Espanha", "foto": "professor.webp" 
    "nome": "Helsinki", "idade": 38, "posicao": "Segurança", "nascimento": "Filândia", "foto": "helsinki.webp",
    "nome": "Denver", "idade": 28, "posicao": "Combater", "nascimento": "Espanha", "foto": "denver.webp",
    "nome": "Berlim", "idade": 42, "posicao": "Vice-líder", "nascimento": "Alemanhã", "foto": "berlim.webp",
    "nome": "Arturo", "idade": 50, "posicao": "Refém", "nascimento": "Espanha", "foto": "arturo.webp",
    "nome": "Raquel", "idade": 35, "posicao": "Inspetora", "nascimento": "Espanha", "foto": "raquel.webp",
    "nome": "Angel", "idade": 33, "posicao": "Negociador", "nascimento": "Espanha", "foto": "angel.webp",
]

def inicio(request):
    return render(request, "time/inicio.html", {"site": site})

def elenco_view(request):
    return render(request, "time/elenco.html", {"site": site, "elenco": elenco})

def sobre(request):
    return render(request, "time/sobre.html", {"site": site})