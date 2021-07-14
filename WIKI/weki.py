import wikipedia
# class mywiki:
#     def __init__(self,lang):
#         self.lang  =lang
    
#     def get_data_from_search(self,search_input,sentences = 2):
#             data= wikipedia.summary(search_input,sentences)
#             print(data)
#         # searched_items = {
#         #     "name":search_input,
#         #     "sentences":sentences,

#         # }


# wiiki = mywiki('en')
# print(wiiki.get_data_from_search(input('ENter word')))
        
class WekiModule:
    def generatesumary(self,input):
        data  = wikipedia.summary(input)
        return data







    