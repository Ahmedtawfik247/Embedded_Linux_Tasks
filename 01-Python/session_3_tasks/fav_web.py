import webbrowser

links_dict = {
    "facebook" : "https://www.facebook.com/",
    "myrepo" : "https://github.com/Ahmedtawfik247/Embedded_Linux_Tasks",
    "youtube"  : "https://www.youtube.com/",
    "moatasem_channel"  : "https://www.youtube.com/@moatasemelsayed6226",
    "tasks"  : "https://docs.google.com/spreadsheets/d/19yIwp7JFG0EecRPTL2aIZUJZdoB33gEq7ThtpCxUbrE/edit#gid=2062191263",
    "attendance"  : "https://docs.google.com/spreadsheets/d/1dV1zoXoNs17x84_ww4Ac1YA5nG8RuH_gwRHLOM3AmOE/edit#gid=1402920523",
}
print("choose your favourite link by typing it's name.")

print("Avaialbe liks is :")

print(list(links_dict.keys()))

x = input("Enter the site name: ")

x = links_dict.get(x)

links = links_dict.values()



def firefox(x):
    webbrowser.get("/usr/bin/firefox %s").open(x)