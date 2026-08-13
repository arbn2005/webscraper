from bs4 import BeautifulSoup
import requests as req


url = "https://blog.python.org/blog/"
res = req.get(url)
doc = BeautifulSoup(res.text, "html.parser")
data = doc.find_all("div", attrs={"class": "min-w-0 flex-1"})

for row in data:
    title = row.find("h3")
    print(title.text)

    author = row.find("a", attrs={"class":
                                  "font-medium text-zinc-600 hover:text-[#306998] dark:text-zinc-300 dark:hover:text-[#ffd43b] transition-colors"
                    })
    print(author.text)

    time = row.find("time")
    print(time.text)

    print("---------------------")

