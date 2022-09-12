import sqlite3
from json_extractor import extract_values as ev
import json

# connection
con = sqlite3.connect('ygo_db.sqlite')
# cursor pour executer des commandes dans la bdd
cur = con.cursor()

# create database with col
# cur.execute('create table mes_cartes(id text, name text, type text, desc text, atk int, def int, level int, race text, attribute text, archetype text, card_sets_name text, card_sets_rarity text, qty int)')

# Pour dire qu'on a fini
cur.close()


def add_card(json_card):
	# connection
	con = sqlite3.connect('ygo_db.sqlite')
	# cursor pour executer des commandes dans la bdd
	cur = con.cursor()

	card_id = ev(json_card, 'id')[0]
	card_name = ev(json_card, 'name')[0]
	card_type = ev(json_card, 'type')[0]
	card_desc = ev(json_card, 'desc')[0]
	card_atk = ev(json_card, 'atk')[0]
	card_def = ev(json_card, 'def')[0]
	card_level = ev(json_card, 'level')[0]
	card_race = ev(json_card, 'race')[0]
	card_attribute = ev(json_card, 'attribute')[0]
	card_archetype = ev(json_card, 'archetype')[0]
	card_sets = ev(json_card, 'card_sets')
	if len(card_sets) > 1:
		i = 0
		for i in range(len(card_sets)):
			print(i, card_sets[i]['set_name'])
	try:
		choice = int(input("De quel set vient-il ? (Par défaut le choix est à 0) "))
	except Exception:
		choice = 0
	card_card_sets_name = ev(json_card, 'set_name')[choice]
	card_card_sets_rarity = ev(json_card, 'set_rarity')[choice]

	try:
		card_qty = int(input("Combien d'exemplaires de cette cartes avez vous ? (Par défaut le choix est à 1) "))
	except Exception:
		card_qty = 1

	cur.execute(
		"insert into mes_cartes (id, name, type, desc, atk, def, level, race, attribute, archetype, card_sets_name, card_sets_rarity, qty) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
		(card_id, card_name, card_type, card_desc, card_atk, card_def, card_level, card_race, card_attribute,
		 card_archetype, card_card_sets_name, card_card_sets_rarity, card_qty))
	con.commit()
	cur.close()


def get_posts():
	con = sqlite3.connect('ygo_db.sqlite')
	cur = con.cursor()
	with con:
		cur.execute("SELECT * FROM mes_cartes")
		print(json.dumps(cur.fetchall(), sort_keys=True, indent=4))


def already_there(name, card_sets, quantity):
    pass
