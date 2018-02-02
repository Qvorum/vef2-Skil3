from bottle import *

@route('/')
def index():
    return template('index.tpl', title="Forsiða")
@route('/frettir/<id>')
def frettir(id):
    if id == 'Sigmundur-David':
        listi = ["Sögur frá fyrrverandi Sigmunds Davíðs", "Saga Ársins samkvæmt Davíð Oddson, Sigmundur Davíð káfaði oft á konu sinni án þess að spyrja um leyfi. Sigmundur Davíð vildi ekki tjá sig um málið!", "Qvorum@frettir.is"]
        return template('frettir.tpl', title = "Sögur Frá Fyrrverandi", listi = listi ,image = "simmisimmiDD.jpg")
    if id == 'Fyrverandi-Barnanidingur':
        listi = ["Viðtal við fyrverandi Barnanýðing", "Barnanýðingurinn Klaus segist hafa riðið mörgum stelpum en alltaf hafa notað smokk!", "Bergthor@frettir.is"]
        return template('frettir.tpl', title = "Barnanýðingur", listi = listi ,image = "EgNotaAlltafSmokk.jpg")
    if id == 'Hentai-Karlar':
        listi = ["98% Ungra Karlmanna fróa sér yfir Hentai", "Samkvæmt Gallup er 98% karlmanna hérlendis sem horfa á Hentai, Við náðum þessari mynd af notenda þess", "VidarMarel@frettir.is"]
        return template('frettir.tpl', title = "HentaiHaven", listi = listi ,image = "BeggiFappaHaHaHa.jpg")
    if id == 'Palli-Loksins-Daudur':
        listi = ["Páll Óskar lést af AIDS", "Það sást á Instagram mynd hjá honum að hann átti lyf fyrir AIDS, Hann Palli sagðist ætla að segja seinna en nú væri kötturinn úr búrinu kominn, Hann dó skömmu siðar", "Qvorum@frettir.is"]
        return template('frettir.tpl', title = "HentaiHaven", listi = listi ,image = "PallOskarFekkAidsOgDeyjaHaHa.jpg")
@route('/lidurA')
def lidurA():
    return template('lidurA.tpl', title = "Lidur A")
@route('/lidurA/<kt>')
def lidurA(kt):
    return template('kennit.tpl',title = "Kennitala", kt=kt)
run(host='0.0.0.0', port=os.environ.get('PORT'))
