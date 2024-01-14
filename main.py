
import flet as ft
import fletcaluclator as fc


def main(page: ft.Page):
    page.title = "Point OF Sale"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_full_screen = True

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    leftDrawerBTN = ft.FloatingActionButton(
        icon=ft.icons.MENU, on_click=show_drawer)
    addCustomerBTN = ft.FloatingActionButton(icon=ft.icons.ADD_MODERATOR)
    customerListBTN = ft.FloatingActionButton(icon=ft.icons.PERSON)
    reprintBTN = ft.FloatingActionButton(icon=ft.icons.LOGOUT)
    newCartBTN = ft.FloatingActionButton(icon=ft.icons.SHOPPING_CART)
    deleteBTN = ft.FloatingActionButton(icon=ft.icons.DELETE)
    discountBTN = ft.FloatingActionButton(icon=ft.icons.DISCOUNT)
    printBTN = ft.FloatingActionButton(icon=ft.icons.PRINT_OUTLINED)
    deleteBTN = ft.FloatingActionButton(icon=ft.icons.DELETE)

    middleTable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Product Name")),
            ft.DataColumn(ft.Text("Quantity"), numeric=True),
            ft.DataColumn(ft.Text("Discount"), numeric=True),
            ft.DataColumn(ft.Text("Price"), numeric=True),
            ft.DataColumn(ft.Text("Tax"), numeric=True),
        ], column_spacing=200)
    calculator = ft.Container(content=fc.CalculatorApp(),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            width=400,
                            height=400,
                            border_radius=10,
                            alignment=ft.alignment.bottom_center)
    cartItems = ft.Container(content=ft.Row(controls=[middleTable]),
                            alignment=ft.alignment.top_left,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            height=400,
                            expand=True,
                            border_radius=10,)
    productsDisplay = ft.Container(bgcolor=ft.colors.SURFACE_VARIANT,
                                height=360,
                                expand=True,
                                border_radius=10,)
    categoriesdisplay = ft.Container(bgcolor=ft.colors.SURFACE_VARIANT,
                                    width=200,
                                    height=360,
                                    expand=False,
                                    border_radius=10,)
    topLeftBTNContainer = ft.Container(content=ft.Row(
        controls=[leftDrawerBTN, addCustomerBTN, customerListBTN, reprintBTN, newCartBTN, deleteBTN]))
    topRightBTNContainer = ft.Container(content=ft.Row(
        controls=[discountBTN, printBTN, deleteBTN]),
        # bgcolor=ft.colors.GREY_800,
        # #expand=True,
        # padding=10,
        # # opacity=0.5,
        # border_radius=10,
        # alignment= ft.alignment.top_right,
    )
    topMenuLeftContainer = ft.Container(content=ft.Row(controls=[topLeftBTNContainer,]),
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        expand=False,
                                        padding=10,
                                        # opacity=0.5,
                                        border_radius=10,
                                        )
    topMenuRightContainer = ft.Container(content=ft.Row(controls=[topRightBTNContainer,]),
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        expand=False,
                                        padding=10,
                                        # opacity=0.5,
                                        border_radius=10,
                                        )
    topDivider = ft.Divider(thickness=2),
    page.drawer = ft.NavigationDrawer(controls=[])
    topMenuRow = ft.Row(
        controls=[topLeftBTNContainer, topRightBTNContainer], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    middleRow = ft.Row(controls=[cartItems, calculator])
    bottomRow = ft.Row(controls=[categoriesdisplay, productsDisplay])
    page.add(topMenuRow, middleRow, bottomRow)


ft.app(target=main)
