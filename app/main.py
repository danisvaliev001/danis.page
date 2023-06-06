import flet as ft


def highlight_link(e):
    e.control.style.color = ft.colors.BLUE
    e.control.update()


def unhighlight_link(e):
    e.control.style.color = None
    e.control.update()


def main(page: ft.Page):
    page.title = "danis’s webpage | danisvaliev001"
    page.fonts = {
        "JetBrainsMono-Regular":
            "https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/otf/JetBrainsMono-Regular.otf",
        "JetBrainsMono-Regular_SemiBold":
            "https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/otf/JetBrainsMono-SemiBold.otf",
        # "JetBrainsMono-Regular_Thin":
        #     "https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/otf/JetBrainsMono-Thin.otf",
    }
    page.theme = ft.Theme(font_family="JetBrainsMono-Regular")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    container_header = ft.Container(
        content=ft.Text(
            "bringing X's through DevOps as an SRE.",
            text_align=ft.TextAlign.CENTER,
            size=16,
        ),
        col={"sm": 12, "md": 12, "xl": 12},
    )

    container_photo = ft.CircleAvatar(
        content=ft.Image(
            src=f"imgs/photo.png",
            fit=ft.ImageFit.FIT_WIDTH,
            border_radius=50
        ),
        col={"sm": 12, "md": 12, "xl": 12},
        height=page.height / 8,
    )

    container_name = ft.Container(
        content=ft.Text(
            "DANIS VALIEV",
            text_align=ft.TextAlign.CENTER,
            size=16,
            font_family="JetBrainsMono-Regular_SemiBold",
        ),
        col={"sm": 12, "md": 12, "xl": 12},
    )

    container_button = ft.Container(
        content=ft.ElevatedButton(text="meet"),
        col={"sm": 6, "md": 4, "xl": 3},
    )

    container_footer = ft.Container(
        content=ft.Text(
            disabled=False,
            spans=[
                ft.TextSpan("works on "),
                ft.TextSpan(
                    "cloudflare",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://pages.cloudflare.com",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,
                ),
                ft.TextSpan(", "),
                ft.TextSpan(
                    "crafted",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://github.com/danisvaliev001/danis.page",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,
                ),
                ft.TextSpan(" on "),
                ft.TextSpan(
                    "flet",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://flet.dev",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,
                ),
                ft.TextSpan(" in "),
                ft.TextSpan(
                    "fleet",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://www.jetbrains.com/fleet",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,
                ),
                ft.TextSpan(""),
            ],
            text_align=ft.TextAlign.CENTER,
            size=10,
            font_family="JetBrainsMono-Regular",
        ),
        col={"sm": 12, "md": 12, "xl": 12},
    )

    def get_resp_row(name_of_container):
        responsive_row = ft.ResponsiveRow(
            [name_of_container],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return responsive_row

    page.add(
        get_resp_row(ft.Container(height=page.height / 10)),
        get_resp_row(container_header),
        get_resp_row(ft.Container(height=page.height / 10)),
        get_resp_row(container_photo),
        get_resp_row(container_name),
        get_resp_row(container_button),
        get_resp_row(ft.Container(height=page.height / 10)),
        get_resp_row(container_footer),
    )
    # page.update()


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    port=0,
    web_renderer="html",
    assets_dir="assets"
)
