import requests
from bs4 import BeautifulSoup
import datetime
import json


def scrape_webpage(url_list):


    """
    #this creates the file name
    now = datetime.datetime.now()

    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    #file_name = f"webl_{timestamp}.jsonl"
    """
    data = []

    for u in url_list:
        response = requests.get(u)

        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.title.string

            soup.head.decompose()

            # Remove the header
            header = soup.find('header')
            header.decompose()

            # Remove the footer
            footer = soup.find('footer')
            footer.decompose()

            all_tags = soup.find_all()

            # Insert a space character between the tags
            for i in range(len(all_tags) - 1):
                all_tags[i].insert_after(' ')
            
            content_text = soup.get_text(" ", strip=True)

            
            

            
            data.append({
                "doc":
                f"url: {u}, title: {title}, content_text: {content_text}"
            })
        else :
            raise ValueError(f"Error in url: {u}")


            return

        
    with open(f"../data/data.jsonl", "w") as f:
        for d in data:
            json.dump(d, f)
            f.write("\n")
            '''
            data.append({
                "doc":
                f"url: {u}, content_text: {content_text}"
                })
            '''

        

   
    #with open(f"../data/{file_name}", "a") as f:

