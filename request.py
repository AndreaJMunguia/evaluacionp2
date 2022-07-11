import json
import requests
try:
    api_url = "http://localhost:8080/apiv1/employee/addemployee"
    #with open("empleados.json", "r") as file:
     #   data = json.load(file)
    diccionario1 = {
                        "firstname" : "Lucho",
                        "surname" : "Dominguez",
                        "country" : 
                            {	"code" : "mx",
                                "name" : "Mexico",
                                "airports" : [
                                        {"name" : "Aeropuerto Internacional de Toluca"}
                                    ]
                            },
                        "languages" : [
                            {
                                "code" : "es",
                                "name" : "espanol"
                            }
                        ]
                    }
    diccionario2 = {
                        "firstname" : "Jean",
                        "surname" : "Paul Gualtier",
                        "country" : 
                            {	"code" : "fr",
                                "name" : "Francia",
                                "airports" : [
                                        {"name" : "Aeropuerto Internacional de la Ciudad de México"}
                                    ]
                            },
                        "languages" : [
                            {
                                "code" : "fr",
                                "name" : "frances"
                            }
                        ]
                    }
except Exception as error:
    print(error)
else:
    response1 = requests.post(api_url, json = diccionario1)
    response2 = requests.post(api_url, json = diccionario2)
    print(str(response1) + str(response2))
    response1.json()
    response2.json()