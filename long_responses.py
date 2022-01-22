import random
def unknown():
    response = ["Could you please re-phrase that? ",
                "Sorry i didn't get you."][
        random.randrange(2)]
    return response