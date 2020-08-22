# ========== 1. Using wikipedia ==========
# Import packages
import wikipedia
import json
# Specify the title of the Wikipedia page
wiki = wikipedia.page('Guido van Rossum')

# Extract the plain text content of the page, excluding images, tables, and other data.
text = wiki.content
# print(text)
split_content = (text.split( ))
wiki_data = {}
wiki_data["content"] = {}
summary_found = False
heading_found = False
heading_started = False
heading_ended = False
data = ""
heading= ""

for word in split_content:
    if summary_found is False:
        if word!= "==" and word != "===":
            data = data +" "+ word
        else:
            wiki_data["content"]["summary"] = data.strip()
            summary_found = True
            data = ""
            heading_found = True
            heading_started = True
    else:
        if word == "==" or word == "===":
            if heading_started is True:
                heading_started = False
            else:
                heading_found = True
                heading_started = True
                heading = heading.strip()
                wiki_data["content"][heading] = data.strip()
                data = ""
                heading = ""
        else:
            if heading_found is True and heading_started is True:
                heading = heading +" " +word
            else:
                data = data+ " " +word

wiki_data["search_results"] = wikipedia.search('Guido van Rossum')
wiki_data["suggestions"] = wikipedia.suggest('Guido van Rossum')
page = wikipedia.page('Guido van Rossum')
wiki_data["title"] = page.title
wiki_data["categories"] = page.categories
wiki_data["references"] = page.references
wiki_data["links"] = page.links
wiki_data["images"] = page.images


with open('wiki_data.json', 'w', encoding="utf-8") as outfile:
    json.dump(wiki_data, outfile, indent=4, sort_keys=True)
