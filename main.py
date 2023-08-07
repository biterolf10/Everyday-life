import webbrowser as wbb
import os


def music():
    os.system("cls")
    music_name = input("Please write a music name ( you can leave it blank ): ")
    music_author = input("Please write a music author ( you can leave it blank ): ")
    
    link = (
        "https://www.youtube.com/results?search_query="
        + music_name
        + "+ - +"
        + music_author
    )
    wbb.open(link)



def translator():
    os.system("cls")
    link = 'https://translate.google.com/?sl=auto&tl='
    
    language_to = input('To what language you want to translate? (write first 2 letters): ')
    link += language_to + '&text='

    text = input('What text you want to translate?')
    link += text + '&op=translate'
    wbb.open(link)



def github():
    os.system("cls")
    link = 'https://github.com/'
    username = input('Write profile name in github: ')

    link += username
    wbb.open(link)



def pinterest():
    link = 'https://pinterest.com'
    tags = input('Write all tags to find images: ')
    link += '/search/pins/?q=' + tags + '&rs=typed'

    wbb.open(link)



def choose():
    choose = input('Which do you want to use:\n'
                       + '1 - Find music on youtube\n'
                       + '2 - Translator\n'
                       + '3 - Find Github Profile\n'
                       + '4 - Pinterest Find By Tags\n\n'
                       )
    if choose == '1':
        music()
        
    if choose == '2':
        translator()

    if choose == '3':
        github()

    if choose == '4':
        pinterest()



def main():
    while 1:
        os.system("cls")
        choose()



if __name__ == "__main__":
    main()
