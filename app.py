from utils.css_loader import global_page_style
from views.landing_view import landing_main

if __name__ == '__main__': 
    global_page_style('./style.css')
    landing_main()
