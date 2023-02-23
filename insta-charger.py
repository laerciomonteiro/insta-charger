import instaloader
from tqdm import tqdm

L = instaloader.Instaloader()

# Ler nomes de usuário do arquivo
with open('agenda.txt', 'r') as f:
    usernames = f.readlines()
    usernames = [username.strip() for username in usernames]

results = []

for username in tqdm(usernames, desc="Coletando dados das contas", unit="contas"):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        # Iterar pelos posts do perfil em ordem cronológica
        for post in profile.get_posts():

            # Extrair informações relevantes do post mais recente
            post_info = {
                'username': username,
                'post_url': f"https://www.instagram.com/p/{post.shortcode}/",
                'timestamp': post.date_local.timestamp(),
                'likes': post.likes,
                'comments': post.comments,
                'caption': post.caption,
                'data': post.date_local.strftime("%d/%m/%Y")
            }

            results.append(post_info)
            break  # Sair do loop após o primeiro post

    except Exception as e:
        print(f"Não foi possível obter dados do usuário {username}: {str(e)}")

# Ordenar resultados por número de likes
results = sorted(results, key=lambda x: x['likes'], reverse=True)

# Exportar resultados para o arquivo resultados.txt
with open('resultados.txt', 'w') as f:
    f.write("==> AGENDA DE EVENTOS <==\n\n")
    for post_info in results:
        f.write(f"Usuário: {post_info['username']}\nLink de acesso: {post_info['post_url']}\n")
        f.write(f"Data do post: {post_info['data']}\n")
        f.write(f"Curtidas: {post_info['likes']}, Comentários: {post_info['comments']}\n")
        f.write(f"Legenda: {post_info['caption']}\n\n")

