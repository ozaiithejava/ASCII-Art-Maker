from pyfiglet import Figlet

def generate_ascii_art(text, font="standard"):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(text)
    return ascii_art

if __name__ == "__main__":
    text_to_convert = input("Enter the text to convert to ASCII art: ")
    selected_font = input("Enter the font type (standard, slant, banner, ...): ")

    ascii_art_result = generate_ascii_art(text_to_convert, font=selected_font)
    print("\nGenerated ASCII Art:")
    print(ascii_art_result)
