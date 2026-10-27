class InvalidSeatNumberError(Exception):
    pass


def book_ticket(movie, seat):
    if seat <= 0:
        raise InvalidSeatNumberError("Seat number must be positive")

    print("Ticket booked:", movie)


try:
    book_ticket("Avengers", -2)

except InvalidSeatNumberError as e:
    print("Error:", e)