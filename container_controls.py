import flet as ft


def main(page: ft.Page):


    page.title = "Flet Example"                      # changes the title of the application to "Flet Example"
    text = ft.Text(value='This is a CheckBox')       # displays the text in the UI
    check_box = ft.Checkbox(label="Click to Check")  # creates a checkbox 

    # the below ft.Column() stacks the above two controls vertically in the UI
    page.add(
        ft.Column(
        [text,check_box]
        )
    )
    
    '''
    # the below ft.Row() stacks the above two controls horizontally in the UI
    page.add(
        ft.Row(
        [text,check_box]
        )
    )
    '''


ft.app(target=main)
