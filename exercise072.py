import webbrowser

#url = "https://google.com"
query = input("Enter your Google query: ")

webbrowser.open_new_tab("https://google.com/search?q=%s" % query)