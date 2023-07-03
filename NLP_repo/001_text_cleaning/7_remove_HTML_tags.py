from bs4 import BeautifulSoup

# Sample HTML text data
html_text = '<html><body><p>This is an example <b>HTML</b> text with <a href="https://example.com">hyperlinks</a> and other <i>markup</i>.</p></body></html>'

# Create a BeautifulSoup object
soup = BeautifulSoup(html_text, 'html.parser')

# Remove HTML tags and markup from the text
processed_text = soup.get_text()

# Print the processed text
print(processed_text)

print(300)


