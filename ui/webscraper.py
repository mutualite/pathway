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

            if soup.find('head'):
                soup.head.decompose()

            # Remove the header
            header = soup.find('header')
            if header:
                header.decompose()

            # Remove the footer
            footer = soup.find('footer')
            if footer:
                footer.decompose()

            # Remove the nav
            nav = soup.find('nav')
            if nav:
                nav.decompose()

            script = soup.find_all("script")
            if script:
                for sc in script:
                    sc.decompose()


            all_tags = soup.find_all("a")

            # Insert a space character between the tags
            #for i in range(len(all_tags) - 1):
             #   all_tags[i].insert_after(' ')
            
            content_text = soup.get_text(" ", strip=True)

            link_content = ""
            for element in all_tags:
                link_content += f"{element.get_text(' ',strip=True)}:{element.get('href')},"

            
            data.append({
                "doc":
                f"url: {u}, title: {title}, content_text: {content_text}, links: '{link_content}'"
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

