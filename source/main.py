from tkinter import *
from webbrowser import open

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()


def github():
    github_frame = Frame(root, bg="white")
    github_frame.place(relwidth=1, relheight=0.25)

    title_lable = Label(github_frame, text="Github")
    title_lable.pack()

    github_profile = Entry(github_frame, bg="white")
    github_profile.pack()

    def find_profile_fun():
        link = "https://github.com/"
        username = github_profile.get()

        link += username
        open(link)

    def find_profile_reps_fun():
        link = "https://github.com/"
        username = github_profile.get()

        link += username
        repositories_link = link + "?tab=repositories"
        open(repositories_link)

    find_profile = Button(
        github_frame, bg="white", text="Open Github Profile", command=find_profile_fun
    )
    find_profile.pack()

    find_profile_reps = Button(
        github_frame,
        bg="white",
        text="Open Github Repositories",
        command=find_profile_reps_fun,
    )
    find_profile_reps.pack()


def pinterest():
    pinterest_frame = Frame(root, bg="white")
    pinterest_frame.place(rely=0.285, relwidth=1, relheight=0.18)

    title_lable = Label(pinterest_frame, text="Pinterest")
    title_lable.pack()

    pinterest_tags = Entry(pinterest_frame, bg="white")
    pinterest_tags.pack()

    def pinterest_open():
        link = "https://pinterest.com"
        tags = pinterest_tags.get()
        link += "/search/pins/?q=" + tags + "&rs=typed"

        open(link)

    open_w_tags = Button(
        pinterest_frame,
        bg="white",
        text="Find Pinterest By Tags",
        command=pinterest_open,
    )
    open_w_tags.pack()


def translator():
    translator_frame = Frame(root, bg="white")
    translator_frame.place(rely=0.5, relwidth=1, relheight=0.22)

    title_lable = Label(translator_frame, text="Translator")
    title_lable.pack()

    translator_text = Entry(translator_frame, bg="white")
    translator_text.pack()

    translator_language = Entry(translator_frame, bg="white")
    translator_language.pack()

    def translator_open():
        link = "https://translate.google.com/?sl=auto&tl="

        language_to = translator_language.get()
        link += language_to + "&text="

        text = translator_text.get()
        link += text + "&op=translate"
        open(link)

    translate = Button(
        translator_frame,
        bg="white",
        text="Translate",
        command=translator_open,
    )
    translate.pack()


def youtube():
    youtube_frame = Frame(root, bg="white")
    youtube_frame.place(rely=0.76, relwidth=1, relheight=0.22)

    title_lable = Label(youtube_frame, text="Translator")
    title_lable.pack()

    youtube_find_text = Entry(youtube_frame, bg="white")
    youtube_find_text.pack()

    def search():
        link = "https://www.youtube.com/results?search_query=" + youtube_find_text.get()
        open(link)

    search_button = Button(
        youtube_frame,
        bg="white",
        text="Search",
        command=search,
    )
    search_button.pack()


root["bg"] = "#ccc"

root.title("Everyday Life")
root.geometry("400x400")
root.resizable(False, False)


def main():
    github()
    pinterest()
    translator()
    youtube()
    root.mainloop()


if __name__ == "__main__":
    main()
