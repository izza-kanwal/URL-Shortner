import flet as ft
import pyshorteners

def shortner(input,output,page):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(input.value)
    output.value=shortened_url
    page.update()
    

def main(page:ft.Page):
    heading=ft.Text("PY URL SHORTNER",size=20 ,text_align="Center",color='GREEN')
    page.horizontal_alignment="Center"
    page.vertical_alignment="Center"
    page.padding = 30
    page.title = "URL Shortner"
    page.window_width = 370
    page.window_height = 726
    page.theme_mode = 'Light'

    def open_repo(output):
     page.launch_url(output.value)

    input=ft.TextField(label="Enter URL to shorten",border_radius=10,color="WHITE",border=ft.InputBorder.UNDERLINE,on_change=lambda _: shortner(input,output,page))
    output=ft.TextField(label="Your Shortened URL Is ",border_radius=10,color="WHITE",border=ft.InputBorder.UNDERLINE)
    button=ft.TextButton("Visit Now",on_click = lambda _: open_repo(output))

    
    
   
 

    box=ft.Column(
        [
         heading,input,output ,ft.Divider(thickness=6,color='TRANSPARENT'),
         button
        ]
    )
    container=ft.Container(
        content=box ,
        bgcolor='BLACK',
        padding=30,
        border_radius=16,
        height=320,
        
    )
    page.update()

    page.add(container)
ft.app(target=main)