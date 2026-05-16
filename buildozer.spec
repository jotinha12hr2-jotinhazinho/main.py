[app]

# (str) Título do teu aplicativo
title = Calculadora Diaria JJ Dinossauro Rex

# (str) Nome do pacote (apenas letras minúsculas e sem espaços)
package.name = jjdinossaurorex

# (str) Domínio do pacote (identificador único para a Google Play)
package.domain = jjdinossaurorex

# (str) Diretório onde o teu arquivo main.py está localizado
source.dir = .

# (list) Extensões de arquivos que devem ser incluídas no APK
source.include_exts = py,png,jpg,kv,atlas

# (str) Versão do aplicativo
version = 1.0.0

# (list) Dependências do projeto (O teu app apenas precisa do Python 3 e Kivy)
requirements = python3,kivy

# (str) Orientação suportada (pode ser landscape, portrait ou all)
# Como o teu layout é vertical, o formato 'portrait' (em pé) é o ideal.
orientation = portrait

# ----------------------------------------------
# Configurações Específicas do Android
# ----------------------------------------------

# (bool) Se o ecrã deve permanecer ativo enquanto o app está aberto
android.wakelock = False

# (list) Permissões do Android (O teu app atual não precisa de internet ou câmara)
# android.permissions = INTERNET

# (int) API do Android que serve como alvo (Target SDK)
android.api = 33

# (int) API mínima do Android suportada (Min SDK)
android.minapi = 21

# (int) Versão do Build Tools do Android SDK
# android.sdk_build_tools_version = 33.0.0

# (bool) Copiar bibliotecas partilhadas para a pasta do projeto
android.copy_libs = 1

# (str) Arquiteturas do processador para as quais queres compilar o APK
# Compilar para armeabi-v7a (32 bits) e arm64-v8a (64 bits) garante que roda em quase todos os telemóveis
android.archs = armeabi-v7a, arm64-v8a

# (bool) Permitir que o buildozer faça o download e atualize o SDK automaticamente
android.skip_update = False

# (bool) Aceitar automaticamente as licenças do Android SDK
android.accept_sdk_license = True

# ----------------------------------------------
# Configurações de Aparência (Opcional)
# ----------------------------------------------

# Se quiseres adicionar um ícone ou ecrã de carregamento no futuro, 
# basta criares as imagens e descomentar (retirar o #) das linhas abaixo:
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

[buildozer]
# (int) Nível de detalhes nos logs (0 = apenas erros, 2 = tudo detalhado)
log_level = 2

# (int) Exibir aviso se o buildozer for executado como root (0 = Falso, 1 = Verdadeiro)
warn_on_root = 1
