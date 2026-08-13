import requests
from bs4 import BeautifulSoup


url = "https://www.lipsum.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

data = soup.find("div", class_="divide-y divide-zinc-200 dark:divide-zinc-800")

questions = []
answers = []

for row in data.find_all("div", recursive=False):
    question = row.find("h2")

    if not question:
        continue

    questions.append(question.get_text(strip=True))

    answer = ""
    for paragraph in row.find_all("p"):
        answer += paragraph.get_text(strip=True) + " "

    answers.append(answer.strip())


for question, answer in zip(questions, answers):
    print(question)
    print(answer)
    print("-" * 80)
