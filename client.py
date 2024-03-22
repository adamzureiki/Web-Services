# import requests
# import getpass
# from requests.exceptions import MissingSchema

# # global variable we use to track if logged in
# isLoggedIn = False  
# createSess = requests.Session()

# def loginClient(link, username, passcode):
#     global isLoggedIn
#     try:
#          # add the link inputted from client to login extension
#         linkIn = link.rstrip('/') + "/api/login"
#         # retrieve credentials to authenticate in server
#         credentials = {"username": username, "password": passcode}
#         typeOfrequest = {"Content-Type": "application/x-www-form-urlencoded"}
#         # use sessions 
#         inputtedLogin = createSess.post(linkIn, data=credentials, headers=typeOfrequest)

#         # authentication validation
#         if inputtedLogin.status_code == 200:
#             print(inputtedLogin.text)
#             isLoggedIn = True
#         else:
#             print(inputtedLogin.text)
#             isLoggedIn = False
#     # the exception below is an idea taken from generative AI to just give a better UI response for invalid URL
#     except MissingSchema:
#         print("Invalid URL")
#         isLoggedIn = False

# def logoutClient(link):
#     global isLoggedIn
#     try:
#         # add the link inputted from client to logout extension
#         linkOut = link.rstrip('/') + "/api/logout"
#         inputtedLogout = createSess.post(linkOut)
#         if inputtedLogout.status_code == 200:
#             print(inputtedLogout.text)
#             # set login variable to false so we can login again after logout
#             isLoggedIn = False
#         else:
#             print(inputtedLogout.text)
#     # the exception below is an idea taken from generative AI to just give a better UI response for invalid URL
#     except MissingSchema:
#         print("Not logged in, URL was invalid")

# def postingClient(link, headline, category, region, details):
#     # add the link inputted from client to stories extension, we remove trailing /
#     linkOfpost = link.rstrip('/') + "/api/stories"
#     # the categories specified in cwk pdf
#     metadataStory = {
#         "headline": headline,
#         "category": category,
#         "region": region,
#         "details": details
#     }
#     typeOfrequest = {"Content-Type": "application/json"}
#     inputtedStory = createSess.post(linkOfpost, json=metadataStory, headers=typeOfrequest)
#     if inputtedStory.status_code == 201:
#         print("Story has been posted.")
#     elif inputtedStory.status_code == 503:
#         print("Service unavailable. Reason:", inputtedStory.text)
#     else:
#         print("Failed to post story:", inputtedStory.text)

# def getstoryClient(link, cat, reg, date):
   
#     paramsToGet = {
#         "story_cat": cat,
#         "story_region": reg,
#         "story_date": date
#     }
#     linkOfget = link.rstrip('/') + "/api/stories"

#     # make the GET request with the session object
#     inputtedgetStory = createSess.get(linkOfget, params=paramsToGet)
    
#     # check the inputtedgetStory status code and process accordingly
#     if inputtedgetStory.status_code == 200:
#         newsStories = inputtedgetStory.json() 
#         if "stories" in newsStories:
#             for storyFromnews in newsStories['stories']:
#                 # provide all that is required by cwk
#                 print("\n")
#                 print(f"Story Key: {storyFromnews['key']}")
#                 print(f"Headline: {storyFromnews['headline']}")
#                 print(f"Category: {storyFromnews['story_cat']}")
#                 print(f"Region: {storyFromnews['story_region']}")
#                 print(f"Author: {storyFromnews['author']}")
#                 print(f"Date: {storyFromnews['story_date']}")
#                 print(f"Details: {storyFromnews['story_details']}")
#                 print("\n")
#     # if no stories, give below message as required by cwk
#     elif inputtedgetStory.status_code == 404:
#         print("No stories found.")

    
# def main():
#     inputtedUrl = None
#     CHOICES_CAT = [
#         ('pol', 'Politics'),
#         ('art', 'Art'),
#         ('tech', 'Technology'),
#         ('trivia', 'Trivia'),
#     ]
#     CHOICES_REG = [
#         ('uk', 'UK'),
#         ('eu', 'European Union'),
#         ('w', 'World'),
#     ]
#     categoryValidation = [catchoice[0] for catchoice in CHOICES_CAT]
#     regionValidation = [regchoice[0] for regchoice in CHOICES_REG]
#     try:
#         while True:
#             firstInput= input("\nEnter command (login url, post, news, logout, list exit): ").strip().lower()
#             # below is response to login, we ask for url, username and passcode
#             if firstInput== 'login':
#                 if isLoggedIn:
#                     print("\nYou are already logged in, logout to login again.")
#                 else:
#                     secondInput = input("\nEnter url: ").strip()
#                     inputtedUrl = secondInput
#                     userName = input("Enter username: ")
#                     passCode = getpass.getpass("Enter passcode: ")
#                     loginClient(inputtedUrl, userName, passCode)
#             # below is response to posting a story
#             elif firstInput.lower() == 'post':
#                 if isLoggedIn:
#                     headline = input("\nEnter story headline: ")
#                     while True:
#                         category = input("\nEnter story category:\n\npol for Politics\nart for Art\ntech for Technology\ntrivia for Trivia\n\n:").lower()
#                         if category not in categoryValidation:
#                             print("Category is not valid, please pick a valid category.")
#                         else:
#                             break  # Exit loop when valid
                    
#                     # Loop until a valid region is given
#                     while True:
#                         region = input("\nEnter story region:\n\nuk for UK\neu for European Union\nw for World\n\n:").lower()
#                         if region not in regionValidation:
#                             print("Region is not valid, please pick a valid region.")
#                         else:
#                             break

#                     details = input("\nEnter story details: ")
#                     postingClient(inputtedUrl, headline, category, region, details)
#                 else:
#                     print("You need to log in before posting a story.")
#             # below is for getting stories
#             elif firstInput.lower() == "get stories":
#                 thirdInput = input("\nEnter url: ").strip()
#                 cat = input("Enter category, * is for all: ")
#                 reg = input("Enter region, * is for all: ")
#                 date = input("Enter date, * is for all: ")
#                 getstoryClient(thirdInput, cat, reg, date)
#             # below is response to logout 
#             elif firstInput== 'logout':
#                 if inputtedUrl is not None:
#                     logoutClient(inputtedUrl)
#                 else:
#                     print("Cannot logout. You are not logged in")
#             # to exit client side
#             elif firstInput== 'exit':
#                 break
#             else:
#                 print("Invalid command. Use 'login', 'logout', or 'exit'.")
#     except KeyboardInterrupt:
#         print("\n Exit due to keyboard interrupt")

# if __name__ == '__main__':
#     main()


import requests
import getpass
from requests.exceptions import MissingSchema

# global variable we use to track if logged in
isLoggedIn = False  
createSess = requests.Session()

def loginClient(link, username, passcode):
    global isLoggedIn
    try:
         # add the link inputted from client to login extension
        linkIn = link.rstrip('/') + "/api/login"
        # retrieve credentials to authenticate in server
        credentials = {"username": username, "password": passcode}
        typeOfrequest = {"Content-Type": "application/x-www-form-urlencoded"}
        # use sessions 
        inputtedLogin = createSess.post(linkIn, data=credentials, headers=typeOfrequest)

        # authentication validation
        if inputtedLogin.status_code == 200:
            print(inputtedLogin.text)
            isLoggedIn = True
        else:
            print(inputtedLogin.text)
            isLoggedIn = False
    # the exception below is an idea taken from generative AI to just give a better UI response for invalid URL
    except MissingSchema:
        print("Invalid URL")
        isLoggedIn = False

def logoutClient(link):
    global isLoggedIn
    try:
        # add the link inputted from client to logout extension
        linkOut = link.rstrip('/') + "/api/logout"
        inputtedLogout = createSess.post(linkOut)
        if inputtedLogout.status_code == 200:
            print(inputtedLogout.text)
            # set login variable to false so we can login again after logout
            isLoggedIn = False
        else:
            print(inputtedLogout.text)
    # the exception below is an idea taken from generative AI to just give a better UI response for invalid URL
    except MissingSchema:
        print("Not logged in, URL was invalid")

def postingClient(link, headline, category, region, details):
    # add the link inputted from client to stories extension, we remove trailing /
    linkOfpost = link.rstrip('/') + "/api/stories"
    # the categories specified in cwk pdf
    metadataStory = {
        "headline": headline,
        "category": category,
        "region": region,
        "details": details
    }
    typeOfrequest = {"Content-Type": "application/json"}
    inputtedStory = createSess.post(linkOfpost, json=metadataStory, headers=typeOfrequest)
    if inputtedStory.status_code == 201:
        print("Story has been posted.")
    elif inputtedStory.status_code == 503:
        print("Service unavailable. Reason:", inputtedStory.text)
    else:
        print("Failed to post story:", inputtedStory.text)


    
def main():
    inputtedUrl = None
    CHOICES_CAT = [
        ('pol', 'Politics'),
        ('art', 'Art'),
        ('tech', 'Technology'),
        ('trivia', 'Trivia'),
    ]
    CHOICES_REG = [
        ('uk', 'UK'),
        ('eu', 'European Union'),
        ('w', 'World'),
    ]
    categoryValidation = [catchoice[0] for catchoice in CHOICES_CAT]
    regionValidation = [regchoice[0] for regchoice in CHOICES_REG]
    try:
        while True:
            firstInput= input("\nEnter command (login url, post, news, logout, list exit): ").strip().lower()
            # below is response to login, we ask for url, username and passcode
            if firstInput== 'login':
                if isLoggedIn:
                    print("\nYou are already logged in, logout to login again.")
                else:
                    secondInput = input("\nEnter url: ").strip()
                    inputtedUrl = secondInput
                    userName = input("Enter username: ")
                    passCode = getpass.getpass("Enter passcode: ")
                    loginClient(inputtedUrl, userName, passCode)
            # below is response to posting a story
            elif firstInput.lower() == 'post':
                if isLoggedIn:
                    headline = input("\nEnter story headline: ")
                    while True:
                        category = input("\nEnter story category:\n\npol for Politics\nart for Art\ntech for Technology\ntrivia for Trivia\n\n:").lower()
                        if category not in categoryValidation:
                            print("Category is not valid, please pick a valid category.")
                        else:
                            break  # Exit loop when valid
                    
                    # Loop until a valid region is given
                    while True:
                        region = input("\nEnter story region:\n\nuk for UK\neu for European Union\nw for World\n\n:").lower()
                        if region not in regionValidation:
                            print("Region is not valid, please pick a valid region.")
                        else:
                            break

                    details = input("\nEnter story details: ")
                    postingClient(inputtedUrl, headline, category, region, details)
                else:
                    print("You need to log in before posting a story.")
            # below is response to logout 
            elif firstInput== 'logout':
                if inputtedUrl is not None:
                    logoutClient(inputtedUrl)
                else:
                    print("Cannot logout. You are not logged in")
            # to exit client side
            elif firstInput== 'exit':
                break
            else:
                print("Invalid command. Use 'login', 'logout', or 'exit'.")
    except KeyboardInterrupt:
        print("\n Exit due to keyboard interrupt")

if __name__ == '__main__':
    main()