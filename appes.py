from flask import Flask, render_template
app = Flask(__name__)
import random as rd




@app.route('/', methods=['GET'])
def index():
    return render_template('indexes.html')

@app.route('/meteo', methods=['GET'])
def meteo():
    n = rd.randint(0, 8)
    if n <= 2:
      previsione = 'pioggia'
      tempo = 'rain_s_cloudy'
    else:
      if n >= 3 & n < 5:
        previsione = 'nuvoloso'
        tempo = 'cloudy'
      if n > 5:
        previsione = 'sole'
        tempo = 'sunny'
    return render_template('indexesmeteo.html', pr = previsione, tempo = tempo)


@app.route('/frasi', methods=['GET'])
def frasi():
  frasi = {1 : 'Innamorati di te, della vita e dopo di chi vuoi, Frida Kahlo', 2 : 'Un giorno senza sorriso è un giorno perso, Charlie Chaplin', 3 : 'Sapere è potere , Francesco Bacone', 4 : 'Il divertimento è una cosa seria , Italo Calvino', 5 : 'Vola solo chi osa farlo, Luis Sepulveda', 6 : 'Se vuoi essere amato, ama, Lucio Anneo Seneca', 7:'Le lacrime di oggi sono gli arcobaleni di domani, Ricky Nelson', 'Non importa quanto vai piano, limportante è non fermarsi':'Confucio','Siate affamati, siate folli': 'Steve Jobs','Pensa,credi,sogna e osa':'Walt Disney'}
  n1 = rd.randint(1, 10)
  frase = frasi[n1]
  return render_template('indexfrasi.html', fr=frase)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)