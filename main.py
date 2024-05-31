from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.planetary.org/articles/p2#list').text

soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('article', class_="flex mb-12 md:mb-6")
article_data = []

for article in articles:
    title_tag = article.find('h2')
    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        title = None
    
    link_tag = article.find('a', href=True)
    if link_tag:
        link = link_tag['href']
    else:
        link = None
    
    summary_tag = article.find('p', class_=None)
    if summary_tag:
        summary = summary_tag.get_text(strip=True)
    else:
        summary = None
    
    article_data.append({
        'title': title,
        'link': link,
    })

# Print the extracted article data
for article in article_data:
    print(article)


print("--------------------------------------------------")
print("                                                    ")
print("                                                    ")
print("                                                    ")
print("                                                    ")
# for article in article_data:
#     if article['link']:
#         response = requests.get(article['link'])
#         article_soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Find all article tags in the detailed page
#         detailed_articles = article_soup.find_all('article')
        
#         detailed_texts = []
        
#         for detailed_article in detailed_articles:
#             # Extract the main content within the specific structure
#             main_content_divs = detailed_article.find_all('div', class_='flex justify-center mx-auto')
            
#             for main_content_div in main_content_divs:
#                 container_div = main_content_div.find('div', class_='container-med w-full px-6')
#                 if container_div:
#                     paragraphs = container_div.find_all('p')
#                     detailed_text = ' '.join(paragraph.get_text(strip=True) for paragraph in paragraphs)
#                     detailed_texts.append(detailed_text)
        
#         article['detailed_texts'] = detailed_texts
        
#         detailed_article_data.append(article)

# # Print the detailed article data
# for article in detailed_article_data:
#     print(article)

detailed_article_data = []

for article in article_data:
    if article['link']:
        response = requests.get(article['link'])
        article_soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all article tags in the detailed page
        detailed_articles = article_soup.find_all('article')
        
        detailed_texts = []
        
        for detailed_article in detailed_articles:
            # Extract the main content within the specific structure
            main_content_divs = detailed_article.find_all('div', class_='flex justify-center mx-auto')
            
            for main_content_div in main_content_divs:
                container_div = main_content_div.find('div', class_='container-med w-full px-6')
                if container_div:
                    paragraphs = container_div.find_all('p')
                    detailed_text = ' '.join(paragraph.get_text(strip=True) for paragraph in paragraphs)
                    detailed_texts.append(detailed_text)
        
        article['detailed_texts'] = detailed_texts
        
        detailed_article_data.append(article)

# Write the detailed article data to a text file
with open('articles.txt', 'a', encoding='utf-8') as file:
    for article in detailed_article_data:
        file.write(f"Title: {article['title']}\n")
        file.write(f"Link: {article['link']}\n")
        file.write("Detailed Text:\n")
        for detailed_text in article['detailed_texts']:
            file.write(detailed_text + "\n")
        file.write("\n" + "="*50 + "\n\n")

print("Articles have been written to 'articles.txt'")