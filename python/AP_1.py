'''
   API: Application Programming Interface
   Nasa API: https://api.nasa.gov/
   API_KEY_NASA: YOU NASA API_key
   Developer: Angel Damian Bravo Enriquez 
   Date: 09/11/2025
   Script Description: Get and read data from NASA API about comets and others
   https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}
'''
 
import requests
import os
 
os.system('cls')
 
def get_nasa_data(api_key):
    print("::: COMET INFORMATTION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"
 
    #Realizar la solicitud a la API
    response = requests.get(url)
    response.raise_for_status() # Valida si se presenta algún error en la partición
    data = response.json() #Covertir la respuesta a formato JSON (JS Object Notation)
 
    print(data)
 
API_KEY_NASA = 'D5psYmDkbLhl0Cky3qXzvw38YFyN66yqghFGSsv8'
get_nasa_data(API_KEY_NASA)