from pick import pick

#Just a test to see if pick works well:
def select_language ():
    title = "select language"
    options = ["English", "Français", "日本語"]
    choice, index = pick(options, title)
    print(choice)
    print(index)
