# Reads in the top.html
# print('reading in html variables')
top_html = open('./templates/top.html').read()
# print(top_html)

# Reads in the bottom.html
bottom_html = open('./templates/bottom.html').read()
# print(bottom_html)

# Reads in the middle index.html
middle_html = open('./content/about.html').read()
# print(middle_html)

# combining all 3 files
# Assembles hte new index.html file by combining the top middle and bottom in that order
combined_html = top_html + middle_html + bottom_html
# print(combined_html)

# Writes the new index.html file to a brand new file in the same directory
open('index.html', 'w+').write(combined_html)


# Reads in the middle index.html
middle_html = open('./content/projects.html').read()

combined_html = top_html + middle_html + bottom_html

# Writes the new index.html file to a brand new file in the same directory
open('projects.html', 'w+').write(combined_html)

# Reads in the middle index.html
middle_html = open('./content/blog.html').read()

combined_html = top_html + middle_html + bottom_html

# Writes the new index.html file to a brand new file in the same directory
open('blog.html', 'w+').write(combined_html)
