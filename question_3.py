"""


Q3 . Create a function that converts a date formatted as mm//dd/yyyy to yyyyddmm.
example ----> input 07/09/2020 to 20200907


"""


def date_converter(input_format_date):
    revered_date = input_format_date.split("/")[::-1]
    final_date = "".join(revered_date)
    return final_date

input_date = "07/09/2020"
converted_date = date_converter(input_date)
print(converted_date)


# paragraph = "Suzan is reading Python. He want to learn Python. He is a good learner."
# sentences = paragraph.split(" ")
# print(sentences)