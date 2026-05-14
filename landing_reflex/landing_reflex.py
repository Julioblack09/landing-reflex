import reflex as rx

config = rx.Config(app_name="landing_reflex")


PURPLE = "#A855F7"
DARK = "#132033"
TEXT = "#5F6B7A"
LIGHT = "#F4F7FB"


def nav():
    return rx.hstack(
        rx.hstack(
            rx.box(
                "B",
                bg=PURPLE,
                color="white",
                width="32px",
                height="32px",
                border_radius="50%",
                display="flex",
                align_items="center",
                justify_content="center",
                font_weight="bold",
            ),
            rx.text("Brooklyn", font_weight="bold", font_size="20px", color=DARK),
            spacing="2",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Home", color=DARK, font_size="12px"),
            rx.link("About", color=DARK, font_size="12px"),
            rx.link("Services", color=DARK, font_size="12px"),
            rx.link("Process", color=DARK, font_size="12px"),
            rx.link("Portfolio", color=DARK, font_size="12px"),
            rx.link("Blog", color=DARK, font_size="12px"),
            rx.button(
                "Contact",
                bg=PURPLE,
                color="white",
                border_radius="4px",
                padding="10px 18px",
                font_size="12px",
            ),
            spacing="5",
            align_items="center",
        ),
        width="100%",
        padding="22px 70px",
        bg="white",
        align_items="center",
    )


def stats():
    return rx.hstack(
        rx.vstack(
            rx.heading("15 Y.", size="5", color=DARK),
            rx.text("Experience", color=TEXT, font_size="12px"),
            spacing="1",
            align_items="center",
        ),
        rx.vstack(
            rx.heading("250+", size="5", color=DARK),
            rx.text("Project Completed", color=TEXT, font_size="12px"),
            spacing="1",
            align_items="center",
        ),
        rx.vstack(
            rx.heading("58", size="5", color=DARK),
            rx.text("Happy Client", color=TEXT, font_size="12px"),
            spacing="1",
            align_items="center",
        ),
        bg="white",
        padding="18px 50px",
        border_radius="4px",
        spacing="8",
        box_shadow="0 10px 30px rgba(0,0,0,0.05)",
    )


def hero():
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "Hello, I’m\nBrooklyn Gilbert",
                size="9",
                color=DARK,
                white_space="pre-line",
                line_height="1.15",
                font_weight="800",
            ),
            rx.text(
                "I’m a Freelance UX/UI Designer and Developer based in London, England. "
                "I strive to build immersive and beautiful web applications through "
                "carefully crafted code and user-centric design.",
                color=TEXT,
                max_width="520px",
                font_size="14px",
                line_height="1.7",
            ),
            rx.button(
                "Say Hello!",
                bg=PURPLE,
                color="white",
                border_radius="4px",
                padding="12px 22px",
                font_size="13px",
            ),
            stats(),
            spacing="5",
            align_items="flex-start",
            width="50%",
        ),
        rx.image(
            src="/brooklyn_photo.jpg",
            width="360px",
            height="430px",
            object_fit="cover",
            border_radius="18px",
        ),
        justify="between",
        align_items="center",
        padding="90px 80px 130px 80px",
        width="100%",
        bg=LIGHT,
    )


def about():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="/brooklyn_photo.jpg",
                    width="300px",
                    height="360px",
                    object_fit="cover",
                    border_radius="10px",
                ),
                rx.hstack(
                    rx.text("f", color=PURPLE),
                    rx.text("♥", color=PURPLE),
                    rx.text("◎", color=PURPLE),
                    rx.text("in", color="white", bg=PURPLE, padding="6px 8px"),
                    rx.text("Be", color=PURPLE),
                    bg="white",
                    padding="12px 26px",
                    border_radius="6px",
                    spacing="4",
                    margin_top="-30px",
                    box_shadow="0 8px 20px rgba(0,0,0,0.08)",
                ),
                align_items="center",
                spacing="0",
            ),
            rx.vstack(
                rx.heading(
                    "I am Professional User\nExperience Designer",
                    size="8",
                    color=DARK,
                    white_space="pre-line",
                    line_height="1.2",
                ),
                rx.text(
                    "I design and develop services for customers specializing creating "
                    "stylish, modern websites, web services and online stores.",
                    color=TEXT,
                    font_size="14px",
                    line_height="1.7",
                ),
                rx.text(
                    "My passion is to design digital user experiences through meaningful "
                    "interactions.",
                    color=TEXT,
                    font_size="14px",
                    line_height="1.7",
                ),
                rx.hstack(
                    rx.button("My Project", bg=PURPLE, color="white", padding="12px 22px"),
                    rx.button(
                        "Download CV",
                        bg="white",
                        color=PURPLE,
                        border=f"1px solid {PURPLE}",
                        padding="12px 22px",
                    ),
                    spacing="3",
                ),
                spacing="4",
                align_items="flex-start",
                width="50%",
            ),
            spacing="8",
            align_items="center",
        ),
        bg="white",
        padding="70px",
        border_radius="14px",
        box_shadow="0 20px 60px rgba(0,0,0,0.08)",
        margin="-70px auto 120px auto",
        width="82%",
    )


def process_card(icon, title):
    return rx.vstack(
        rx.box(
            icon,
            bg="#F3E8FF",
            color=PURPLE,
            width="54px",
            height="54px",
            display="flex",
            align_items="center",
            justify_content="center",
            border_radius="8px",
            font_size="24px",
        ),
        rx.text(title, font_weight="bold", color=DARK),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla purus arcu.",
            color=TEXT,
            font_size="13px",
            line_height="1.6",
        ),
        bg="white",
        padding="28px",
        border_radius="10px",
        box_shadow="0 10px 30px rgba(0,0,0,0.05)",
        spacing="3",
        align_items="flex-start",
    )


def work_process():
    return rx.hstack(
        rx.vstack(
            rx.heading("Work Process", size="8", color=DARK),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla purus arcu, "
                "varius eget velit non, laoreet imperdiet.",
                color=TEXT,
                line_height="1.7",
                font_size="14px",
            ),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla purus arcu.",
                color=TEXT,
                line_height="1.7",
                font_size="14px",
            ),
            spacing="4",
            width="38%",
            align_items="flex-start",
        ),
        rx.grid(
            process_card("▣", "1. Research"),
            process_card("⌁", "2. Analyze"),
            process_card("✎", "3. Design"),
            process_card("▰", "4. Launch"),
            columns="2",
            spacing="4",
            width="48%",
        ),
        justify="between",
        align_items="center",
        bg=LIGHT,
        padding="120px 80px",
        width="100%",
    )


def portfolio():
    return rx.vstack(
        rx.heading("Portfolio", size="8", color=DARK),
        rx.text(
            "There are many variations of passages of Lorem Ipsum available,\nbut the majority have suffered alteration.",
            color=TEXT,
            text_align="center",
            white_space="pre-line",
            font_size="14px",
        ),
        rx.grid(
            rx.image(src="/portfolio1.jpg", width="100%", height="230px", object_fit="cover"),
            rx.image(src="/portfolio2.jpg", width="100%", height="230px", object_fit="cover"),
            rx.image(src="/portfolio3.jpg", width="100%", height="230px", object_fit="cover"),
            columns="3",
            spacing="5",
            width="100%",
        ),
        spacing="5",
        align_items="center",
        padding="80px",
        bg="white",
        width="100%",
    )


def index():
    return rx.box(
        rx.box(
            nav(),
            hero(),
            about(),
            work_process(),
            portfolio(),
            width="86%",
            margin="40px auto",
            bg="white",
            border_radius="22px",
            overflow="hidden",
            box_shadow="0 30px 100px rgba(0,0,0,0.18)",
        ),
        bg="linear-gradient(135deg, #DDE7F0 0%, #F8FAFC 45%, #DCEAF6 100%)",
        min_height="100vh",
        padding="30px 0",
    )


app = rx.App()
app.add_page(index)