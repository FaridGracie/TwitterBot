#esse começo é padrão do tweepy que é pra conectar com o twitter developer
import tweepy
import time

#eu tirei os valores reais, mas são as keys pra validar o acesso
consumer_key = 'XXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#autoriza a conexão usando as keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

#simplifica o codigo. wait_on_rate_limit determina se o programa vai esperar o limite (tem um cooldown da api). wait_on_rate_limit_notify printa se ainda tem cooldown e quantos segundos faltam.
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

#Nome do arquivo que vai guardar o id dos ultimos tweets
FILE_NAME = 'last_seen_id_long_text.txt'

#função pra ler o arquivo que tem o id
def read_id(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

#função pra guardar o id no arquivo
def store_the_id(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

#teste é só o nome pq eu passei de outro arquivo que tava testando. os parenteses determinam que x é int
def teste(x: int):

    #determina oq são tweets. 2 é a quantidade de tweets que ele vai pegar por vez (quanto mais mais rapido o cooldown vem). depois ele verifica o ultimo id pra nao repetir os tweets. tweet_mode é como vão aparecer
    tweets = api.home_timeline(2, read_id(FILE_NAME), tweet_mode = 'extended')    

    #so pra confirmar 
    print('Setup is ok!')

    #loop for na lista de tweets
    for tweet in reversed(tweets):

        #procura pelas keywords
        if 'carente' in tweet.full_text.lower() or 'carência' in tweet.full_text.lower() or 'carencia' in tweet.full_text.lower() and '@faridisying esteve ' not in tweet.full.text.lower():
            
            #printa os tweets com as keywords e com o id
            print(str(tweet.id) + ' - ' + tweet.full_text)

            #da rt
            api.retweet(tweet.id)

            #coloca o id no arquivo
            store_the_id(FILE_NAME, tweet.id)

            #x = 1 (pra somar dps)
            x = 1

        #só pra lockar as palavras e colocar x = 0    
        elif 'carente' not in tweet.full_text.lower():

            #x = 0 (pra somar dps)
            x = 0

    #retorna x pro codigo        
    return x    

#função que pega o horario
def tweet_thingy():

    #determina a string status (y ta mais em baixo do codigo)
    status = '@faridisdying esteve carente ' + str(y) + ' vezes.'

    #pega o tempo em minutos e fala que se ele for == a 30
    if time.gmtime().tm_min == '30':

        #confirmação
        print('Succesefilly posted the hourly tweet')

        #tweeta o status por hora
        api.update_status(status)
    else:
        return

#loop do codigo
while True:

    #printa o tempo no console (só pra monitoração)
    print(time.gmtime().tm_min)

    #x = executar a func
    x = teste(0)

    #ve qual é o numero no arquivo (inicialmente 0)
    with open('number.txt', 'r') as f:
        read = f.readline

        #transforma o texto em int
        z = int(read())

    #y = numero do arquivo + resultado da função(1 ou 0)    
    y = z + x

    #coloca o tempo pra funcionar
    tweet_thingy()

    #printa y só pra ver
    print(y)

    #escreve o resultado de y
    with open('number.txt', 'w') as f:
        write = f.write(str(y))
        write

    #tempo de 60 segundos pra evitar o cooldown de 15 minutos do tweepy
    time.sleep(60)