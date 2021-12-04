# IF704-ChatBot
## ChatBot IF704 - Processamento de Linguagem Natural (2021.1)

### Integrantes do grupo

* Matheus Borba  - mlbas@cin.ufpe.br
* Tiago Moraes   - tbm2@cin.ufpe.br

### Run on shell
* Terminal 1
```bash
$ cd src/
$ rasa run actions
```
* Terminal 2
```bash
$ cd src/
$ rasa shell
```

### Run on telegram
* Terminal 1
```bash
$ ngrok http 5005
```
Add on `credential.yml`, the bot credentials, update '<\url>'  with the output from ngrok.
* Terminal 2
```bash
$ cd src/
$ rasa run actions
```
* Terminal 3
```bash
$ cd src/
$ rasa run
```
Open telegram and done!
