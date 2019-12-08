class e_book():
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False

    def next_page(self):
        if self.current_page == self.page_count:
            print("Jesteś na ostatniej stronie")
        else:
            self.current_page += 1

    def previous_page(self):
        if self.current_page == 1:
            print("Jesteś na pierwszej stronie")
        else:
            self.current_page -= 1
    
    def read(self):
        if self.is_open:   
            print("Przeczytano stronę")
        else:
            print("Książka jest zamknięta")

    def show_status(self):
        print(f"Tytuł: {self.title}\nAutor: {self.author}\nIlość stron: {self.page_count}\nObecna stona: {self.current_page}")