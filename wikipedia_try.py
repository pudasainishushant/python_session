import wikipedia

class WikipediaSearch:
    def __init__(self,language):
        self.lang = language
        wikipedia.set_lang(self.lang)
    def generate_summary(self,user_query):
        summary = wikipedia.summary(user_query)
        return summary

if __name__=="__main__":
    user_ko_input = input("What do you want to search?")
    wikisearch_obj = WikipediaSearch("ne")
    print(wikisearch_obj.generate_summary(user_ko_input))

