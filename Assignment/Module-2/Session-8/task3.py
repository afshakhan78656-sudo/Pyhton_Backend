def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat:", seat_type)
    print("Snacks:", snacks)
    print()


book_movie_ticket("Jawan", "Regular", "Popcorn")

book_movie_ticket(movie_name="Pathaan", seat_type="VIP", snacks="Pizza")

book_movie_ticket("Jawan", snacks="Cold Drink", seat_type="VIP")