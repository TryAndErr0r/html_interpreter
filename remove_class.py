from bs4 import BeautifulSoup, Comment

# sample HTML content
html_content = ""
with open('html_dump/step1.html', 'r') as f:
    html_content = f.read()
# parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# find all elements with a "class" attribute and remove it
for tag in soup.find_all(True):
    tag.attrs = {key: val for key, val in tag.attrs.items() if key != 'class'}

# remove all the comments from the HTML
for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
    comment.extract()

# find all the div and span tags without an id attribute and replace them with their contents
for tag in soup.find_all(['div', 'span']):
    if 'id' not in tag.attrs:
        tag.unwrap()

# find all the img tags and remove them
for tag in soup.find_all('img'):
    tag.extract()

# find all the svg tags and remove them
for tag in soup.find_all('svg'):
    tag.extract()

# find all the elements with inline styles and remove those styles
for tag in soup.find_all(True):
    if 'style' in tag.attrs:
        del tag.attrs['style']


# find all the script tags and remove them
for tag in soup.find_all('script'):
    tag.extract()

# Get all the default HTML tags
default_tags = ['html', 'head', 'title', 'meta', 'link', 'body', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p',
                'a', 'img', 'ul', 'ol', 'li', 'table', 'tr', 'th', 'td', 'form', 'input', 'select', 'option', 'button']

# Find all the non-default tags and remove them
for tag in soup.find_all():
    if tag.name not in default_tags:
        tag.unwrap()
with open('html_clean/cleaned.html', 'w') as f:
    f.write(str(soup))
