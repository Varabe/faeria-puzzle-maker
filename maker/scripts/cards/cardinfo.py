from collections import namedtuple
import os


LAND_FIELDS = 4, 5, 6, 7, 8, 9
IMAGE_TEMPLATE = "/static/cards/English/{card_id}.png"
IMAGE_NOT_FOUND = "/static/cards/notfound.png"
CARD_FIELDS = "id color name type wild faeria lake forest mountain desert power life text codex count_in_codex codex_id rarity image"
Card_metaclass = namedtuple("Card", field_names=CARD_FIELDS)


def Card(card_fields): # as if it was a class, lol
	for field_id in LAND_FIELDS:
		if not card_fields[field_id]:
			card_fields[field_id] = "0"
	card_id = format_id(card_fields[0])
	card_fields.append(get_image(card_id))
	return Card_metaclass(*card_fields)


def format_id(raw_card_id):
	card_id = str(raw_card_id)
	size = len(card_id)
	if size == 1:
		return "00{}".format(card_id)
	elif size == 2:
		return "0{}".format(card_id)
	else:
		return card_id


def get_image(card_id):
	django_path = IMAGE_TEMPLATE.format(card_id=card_id)
	real_path = "frontend" + django_path
	if not os.path.exists(real_path):
		django_path = IMAGE_NOT_FOUND
	return django_path
