import json
import requests

with open("sample_diction.json") as f:
	dict_file = f.read()

flick_resp = json.loads(dict_file)
pd = flick_resp["photo"]


class Photo(object):

	def __init__(self, photo_dict):
		self.tags = []
		for x in photo_dict["tags"]["tag"]:
			self.tags.append(x["_content"])
			#	for i in range(len(photo_dict["photo"]["tags"][x])):
			#		self.tags.append(photo_dict["photo"]["tags"][x][i]["raw"])
			#self.tags = [tag.encode('utf-8') for tag in self.tags]

		#self.description = photo_dict["photo"]["description"]["_content"]

		self.title = photo_dict["title"]["_content"]

		self.artist = photo_dict["owner"]["username"]

		self.id = photo_dict["id"]

		self.url = photo_dict["urls"]["url"][0]["_content"]

	def __str__(self): #description
		return "This photo, titled {}, is by {}.".format(self.title, self.artist)		

	def __repr__(self): #summary
		return '''Title: {0}
Author: {1}
URL: {2}
ID: {3}'''.format(self.title, self.artist, self.url, self.id)
		# Triple quotes create multi-line 

	def __contains__(self, tag_name):
		#if 'string x' in object: do something
		result = tag_name in self.tags
		return tag_name
		print(result)


p = Photo(pd)
print(repr(p))
if 'nature' in p:
	print("Nature is a tag of this object.")

