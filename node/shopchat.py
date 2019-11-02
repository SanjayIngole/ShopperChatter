import sys, json
import pandas as pd
import numpy as np
import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import webcolors
from colour import Color

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()

    #return the sum to the output stream
    print(nlp_engine(lines))

def check_color(color):
        try:
            Color(color)
            return True
        except ValueError:
            return False

def get_query_values(search_query):
    rtnDict = {}
    colr = [i for i in search_query.split(' ') if check_color(i)]
    words = nltk.word_tokenize(search_query)
    pos = nltk.pos_tag(words)
    noun = [pos[0] for pos in pos if pos[1][0] == 'N']
    if len(noun) > 0:
        rtnDict["product"]= noun[0].lower()
    else:
        rtnDict["product"] = ""
    
    if len(colr) > 0:
        rtnDict["color"]= colr[0].lower()
    else:
        rtnDict["color"] = ""
    
    return rtnDict

def nlp_engine(search_query):
    
    criteria = get_query_values(search_query)
    data_1 = dict({'display_name': "Chair 1",
                   'image_url':"https://www.ikea.com/PIAimages/0728153_PE736122_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'brown', 
                   'price':49.00 , 
                   'dimensions': [16,19,35] , 
                   'delivery':'available' ,
                   'url':"https://www.ikea.com/us/en/p/ingolf-chair-brown-black-60217822/",
                   'material': 'Solid wood'}) 
    data_2 = dict({'display_name': "Chair 2", 
                   'image_url':"https://www.ikea.com/PIAimages/0728152_PE736113_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'white', 
                   'price':49.00 , 
                   'dimensions': [16,20,35] , 
                   'delivery':'available' ,
                   'url':"https://www.ikea.com/us/en/p/ingolf-chair-white-70103250/",
                   'material': 'Solid wood'})
    data_3 = dict({'display_name': "Chair 3", 
                    'image_url':"https://www.ikea.com/PIAimages/0727339_PE735611_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'white', 
                   'price':75.00 , 
                   'dimensions': [18,20,32] , 
                   'delivery':'available' ,
                   'url':"https://www.ikea.com/us/en/p/norraryd-chair-white-70273092/",
                   'material': 'Solid wood'})
    data_4 = dict({'display_name': "Chair 4", 
                   'image_url':"https://www.ikea.com/PIAimages/0728312_PE736183_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'white', 
                   'price':59.00 , 
                   'dimensions': [16,19,35] ,
                   'delivery':'available',
                   'url':"https://www.ikea.com/us/en/p/gamleby-chair-light-antique-stain-gray-60247051/",
                   'material': 'Solid wood'})
    data_5 = dict({'display_name': "Chair 5", 
                   'image_url':"https://www.ikea.com/PIAimages/0728155_PE736115_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'pine',
                   'price':49.00 , 
                   'dimensions': [16,19,35] , 
                   'delivery':'available',
                   'url':'https://www.ikea.com/us/en/p/ivar-chair-pine-90263902/',
                   'material': 'Solid wood'})
    data_6 = dict({'display_name': "Chair 6", 
                   'image_url':"https://www.ikea.com/PIAimages/0729768_PE737135_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'white', 
                   'price':49.00, 
                   'dimensions': [16,19,35], 
                   'delivery':'available',
                   'url':"https://www.ikea.com/us/en/p/leifarne-chair-white-broringe-black-s89197710/",
                   'material': 'Solid wood'})
    data_7 = dict({'display_name': "Chair 7", 
                   'image_url':"https://www.ikea.com/PIAimages/0728280_PE736170_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'white', 
                   'price':12.50, 
                   'dimensions': [16,19,35], 
                   'delivery':'available',
               'url':"https://www.ikea.com/us/en/p/adde-chair-white-10219178/",
                   'material': 'Solid wood'})
    data_8 = dict({'display_name': "Chair 8", 
                   'image_url':"https://www.ikea.com/PIAimages/0727322_PE735594_S5.JPG?f=l",
                   'product': 'chair', 
                   'color': 'black', 
                   'price':89.00 , 
                   'dimensions': [16,19,35],
                   'delivery':'available',
                   'url':"https://www.ikea.com/us/en/p/odger-chair-blue-00360002/",
                   'material': 'wooden plastic'})
    
    df = pd.DataFrame.from_dict([data_1,data_2,data_3,data_4,data_5,data_5,data_6,data_7,data_8])
    if criteria['product'] !="":
        df = df[(df['product']== criteria['product'] )]
    if criteria['color'] !="":
        df = df[(df['color']== criteria['color'])]
    df_filter_json = df.head(3).to_json(orient = "records")

    products = json.loads(df_filter_json)
    rtnObj = {}
    rtnObj['products']=products
    rtnObj['query']= criteria
    return json.dumps(rtnObj)

# Start process
if __name__ == '__main__':
    #nltk.download('popular')
    main()