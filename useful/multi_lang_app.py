"""multi language application with python
"""

lang = input('Enter Your Language(fa, en, ar, gr): ')

texts = {
    'Greeting': {
        'fa': 'درود', 'en': 'hi', 'ar': 'السلام', 'gr': 'hallo'
    },
    'Exiting': {
        'fa': 'خداحافظ', 'en': 'bye', 'ar': 'الالقا', 'gr': 'Tshuss'
    }
}

print(texts['Greeting'].get(lang, 'hi'))
print('..........')
print(texts['Exiting'].get(lang, 'bye'))
