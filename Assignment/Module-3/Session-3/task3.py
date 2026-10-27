def book_movie_ticket():
    wallet = 1000

    try:
        tickets = int(input("Enter number of tickets: "))
        price = wallet / tickets

        print("Price per ticket:", price)

    except ZeroDivisionError:
        print("Error: Tickets cannot be zero!")

    except ValueError:
        print("Error: Enter a valid number!")


book_movie_ticket()