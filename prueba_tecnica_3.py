import re

texto = '["Hydrogen trains](http://www.hydrogencarsnow.com/blog2/index.php/hydrogen-vehicles/i-hear-the-hydrogen-train-a-comin-its-rolling-round-the-bend/)'

urls = re.findall(r'(?:https?://)?(?:www\.)?([\w-]+\.[\w.-]+)', texto)

print('; '.join(urls))



"""
Se le proporcionara un fragmento de marcado HTML. Su tarea es identificar los nombres de dominio ´unicos de los enlaces o Urls que estan 
presentes en el fragmento de marcado.
"""