import datetime
import time
import random 
import sys
from flask import Flask, jsonify

app = Flask(__name__)

#N = random.randint(1, sys.maxsize)

articles = ['Boules de Noël', 'Guirlandes lumineuses', 'Sapins de Noël', 'Chaussettes de Noël', 'Calendriers de l Avent', 'Tasses festives', 'Bougies parfumées', 'Papiers cadeaux', 'Peluches de Noël', 'Ornements de table']

def gen_article():

    nom = random.choice(articles)
    prix = int(round(random.uniform(5, 40))) #prix entre 5 et 50 euros
    quantite = random.randint(1,5)

    return (nom, prix, quantite)

# Generer un nombre aleatoire d'article
def gen_ticket_random():
    num_articles = random.randint(1,10)
    #return [gen_article() for _ in range(num_articles)]
    ticket = []

    for _ in range(num_articles):
        nom, prix, quantite = gen_article()

        #verification si l'article existe deja
        found = False
        for item in ticket:
            if item[0] == nom:
                item[1] += prix
                item[2] += quantite
                found = True
                break
        if not found:
            ticket.append([nom, prix, quantite])
    return ticket

# Class Ticket
class Ticket():
    # ticket d'achat
    def __init__(self):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #date actuelle (et heure)
        self.article = gen_ticket_random() # nombre aleatoire d'article
        self.total = sum(a[1] * a[2] for a in self.article) #là on calcule le total

@app.route('/tickets', methods=['GET']) # API route

def gen_tickets_api():

    while True:
          ticket = Ticket() 

          return jsonify({
            "date": ticket.date,
            "articles": [{"Product": a[0], "price": a[1], "quantity": a[2]} for a in ticket.article],
            "total": round(ticket.total, 2),
          })

          time.sleep(2)

if __name__ == '__main__':
    app.run(debug=True)
