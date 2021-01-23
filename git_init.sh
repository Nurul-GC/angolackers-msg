# este shell script automatiza
# a criação da pasta .git e faz o primeiro upload (push)
# para o repositório já criado na plataforma github

git init # criando a pasta .git
git add ./* # adicionando todos os arquivos existentes na pasta atual ao repositorio
git commit -m "updating commit" # criando o primeiro commit
git remote add origin https://github.com/Nurul-GC/angolackers-msg.git # conectando com o repositorio origem
git branch -M main # conectando com o ramo principal (default main)
git push -u origin main # fazendo o upload (push)