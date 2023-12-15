import instaloader
from tqdm import tqdm
from datetime import datetime
from instaloader.exceptions import ProfileNotExistsException

def ler_usernames(arquivo):
    with open(arquivo, 'r') as f:
        return [username.strip() for username in f.readlines()]

def obter_posts_recentes(usernames, mes_atual):
    L = instaloader.Instaloader()
    resultados = []

    for username in tqdm(usernames, desc="Coletando dados das contas", unit="contas"):
        try:
            perfil = instaloader.Profile.from_username(L.context, username)
            for post in perfil.get_posts():
                if post.date_local.month != mes_atual:
                    break
                resultados.append({
                    'username': username,
                    'post_url': f"https://www.instagram.com/p/{post.shortcode}/",
                    'timestamp': post.date_local.timestamp(),
                    'likes': post.likes,
                    'comments': post.comments,
                    'caption': post.caption,
                    'data': post.date_local.strftime("%d/%m/%Y")
                })
                break
        except ProfileNotExistsException:
            print(f"O usuário {username} não existe no Instagram. Ignorando...")
        except Exception as e:
            print(f"Não foi possível obter dados do usuário {username}: {str(e)}")

    return sorted(resultados, key=lambda x: x['likes'], reverse=True)

def salvar_resultados(resultados, arquivo):
    with open(arquivo, 'w') as f:
        f.write("==> AGENDA DE EVENTOS <==\n\n")
        for post_info in resultados:
            f.write(f"Usuário: {post_info['username']}\nLink de acesso: {post_info['post_url']}\n")
            f.write(f"Data do post: {post_info['data']}\n")
            f.write(f"Curtidas: {post_info['likes']}, Comentários: {post_info['comments']}\n")
            f.write(f"Legenda: {post_info['caption']}\n\n")

if __name__ == "__main__":
    usernames = ler_usernames('agenda.txt')
    mes_atual = datetime.now().month
    resultados = obter_posts_recentes(usernames, mes_atual)
    salvar_resultados(resultados, 'resultados.txt')
    print("Processo finalizado!")
    print("Os resultados da coleta podem ser encontrados no arquivo 'resultados.txt'.")
