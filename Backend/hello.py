from flask import Flask
app = Flask(__name__) 

def create_programming_language(new_lang):
   in_memory_datastore[language_name] = new_lang
   return "HI"
    
@app.route('/images', methods=['GET', 'POST'])
def images_route():
   if request.method == 'GET':
      return "hi";
   elif request.method == "POST":
      print("it works :)")
      return create_programming_language(request.get_json(force=True))


