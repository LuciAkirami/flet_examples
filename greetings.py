# importing libraries
import flet as ft

# defining main page
def main(page: ft.Page):

  
    page.title = "Greetings App"                                # sets the title of the applicaiton
    username = ft.TextField(label="Type your name",width=200)   # creates a user input box

    # function to display the greeting message
    def display(e):
        name = ft.Text("Hello " + username.value)
        page.add(name)

    # adding all the controls to the main page
    page.add(
        ft.Row(
        [username,
         ft.ElevatedButton('Submit',on_click=display)]         # creates a button for the user to interact, which triggers the display() function
        )
    )

# The below command runs the code as a Desktop application
ft.app(target=main)

# The below line runs the code as a Website
# ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
