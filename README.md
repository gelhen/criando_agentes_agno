## Passos para instalar node.js, npx, npm e agent-ui no Linux

### 1. Instalar o Node.js (e npm) no Linux

**Via terminal (distribuições baseadas em Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install nodejs npm -y
```

**Ou, para obter a versão mais recente via NodeSource:**

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

- Verifique as versões instaladas:
```bash
node -v
npm -v
```

### 2. npx no Linux

O `npx` já vem junto com o npm (>= 5.2), então normalmente já estará disponível:

```bash
npx -v
```

Se não estiver, atualize o npm:

```bash
sudo npm install -g npm
```

### 3. Instalar o agent-ui

- Se `agent-ui` for um pacote npm público:

```bash
npx agent-ui@latest
```
ou para instalar globalmente:

```bash
sudo npm install -g agent-ui
```

- Execute o `agent-ui`:

```bash
agent-ui
```

> Consulte a documentação do projeto para comandos ou configurações adicionais.

### Resumo

1. Instale o Node.js e npm: `sudo apt install nodejs npm -y` **ou** via NodeSource para versão mais recente
2. Verifique as versões: `node -v`, `npm -v`, `npx -v`
3. Use `npx agent-ui@latest` ou `sudo npm install -g agent-ui`
4. Execute `agent-ui` no terminal


## Para rodar o agent-ui
```bash
cd agent-ui
```
```bash
npm run dev
```

## para dorar o app
```bash
uv run test_my_os.py
```

