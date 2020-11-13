
# cd templates
cat ./templates/top.html ./content/about.html ./templates/bottom.html > docs/about.html

cat templates/top.html content/projects.html templates/bottom.html > docs/projects.html

cat templates/top.html content/blog.html templates/bottom.html > docs/blog.html


# cat templates/top.html ./content/about.html templates/bottom.html > about.html


cat docs/about.html docs/projects.html docs/blog.html > docs/index.html
