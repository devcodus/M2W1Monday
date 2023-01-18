from app import app
from flask import render_template

@app.route('/')
def homePage():
    people = [{ "name" :'Kirk Franklin',
                "img" :  "https://upload.wikimedia.org/wikipedia/en/3/35/Kirk_Franklin_Hello_Fear.jpg" } , 
                { "name" : "Natanael Cano",
                    "img" : "https://cdns-images.dzcdn.net/images/cover/404d77c6f30e484a04e611981e99b88b/500x500.jpg" } , 
                    {"name" : "Ramón González",
                        "img" : "https://cdns-images.dzcdn.net/images/cover/8e76ca69a8fa1312636e67ac21449042/264x264.jpg"}, 
                        { "name" : "Wizkid",
                            "img" : "https://i.scdn.co/image/ab67616d0000b27379ab73f6bfebec7c0e85f922"},
                            { "name": 'Marino',
                                "img": "https://cdns-images.dzcdn.net/images/cover/f1b00c5716af38899ea880b685c079b5/264x264.jpg"}]
    text = "(this is dynamically served from python:) CLICK HERE TO SEE MY TOP FIVE!!!!"
    return render_template('index.html', people = people, my_text = text )


@app.route('/contact')
def contactPage():
    return render_template('contact.html')

@app.route('/topfive')
def topFivePage():
    people = [{ "name" :'Kirk Franklin',
                "img" :  "https://upload.wikimedia.org/wikipedia/en/3/35/Kirk_Franklin_Hello_Fear.jpg" } , 
                { "name" : "Natanael Cano",
                    "img" : "https://cdns-images.dzcdn.net/images/cover/404d77c6f30e484a04e611981e99b88b/500x500.jpg" } , 
                    {"name" : "Ramón González",
                        "img" : "https://cdns-images.dzcdn.net/images/cover/8e76ca69a8fa1312636e67ac21449042/264x264.jpg"}, 
                        { "name" : "Wizkid",
                            "img" : "https://i.scdn.co/image/ab67616d0000b27379ab73f6bfebec7c0e85f922"},
                            { "name": 'Marino',
                                "img": "https://cdns-images.dzcdn.net/images/cover/f1b00c5716af38899ea880b685c079b5/264x264.jpg"}]
    return render_template('topfive.html', people = people)