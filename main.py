import flet as ft

def main(page: ft.Page):
    page.title = "Rutas"

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.AppBar(title=ft.Text("Inicio")),
                    ft.ElevatedButton("Ir a /perfil",
                                      on_click=lambda _: page.go("/perfil")),
                ])
            )
        elif page.route == "/perfil":
            page.views.append(
                ft.View("/perfil", [
                    ft.AppBar(
                        title=ft.Text("Perfil"),
                        leading=ft.IconButton(ft.icons.ARROW_BACK,
                                              on_click=lambda _: page.go("/"))
                    ),
                    ft.Text("Aquí iría la info del usuario…"),
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(main)
