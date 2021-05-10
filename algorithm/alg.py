import json
import twint


def file_op():
	data = []
	j_data = []
		 # retype your json file path here
	with open("/home/ubuntu/Documents/documents/twitter_scraper/t_api/algorithm/tweets.json") as outjson:

		for i in outjson:
			data.append(i)
		for _ in range(0, len(data)):
			r = data[_]
			res = json.loads(r)
	
			j_data.append(res)

		
	#result = j_data[0]
	#return result

	return j_data			
"""
	print("---------------------------------------tweet-------------------------------------------")
	for _ in range(0, len(j_data)):
		print({f"tweet {_} => " : j_data[_]["tweet"]})
		print("\n\n\n")		
	

	print("----------------------------------------ID---------------------------------------------")
	for _ in range(0, len(j_data)):
		print({f"id {_} => " : j_data[_]['id']})
	
	
	print("--------------------------------------authors------------------------------------------")
	for _ in range(0, len(j_data)):
		print({f"author {_} => " : j_data[_]['username']})
"""	
	
def search_by_expression():
	c = twint.Config()
	c.Store_object = True
	c.Search = "request for startup"
	c.Store_json = True
	c.Output = "/home/ubuntu/Documents/documents/twitter_scraper/t_api/algorithm/tweets.json" # retype your path to export
	twint.run.Search(c)

#search_by_expression()
#file_op()
