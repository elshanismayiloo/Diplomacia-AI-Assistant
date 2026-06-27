from backend.search import search_knowledge

question = input("Search: ")

result = search_knowledge(question)

print(result)
