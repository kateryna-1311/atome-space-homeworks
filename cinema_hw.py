class CinemaHall:
    def __init__(self, movie_title: str, total_seats: int, ticket_price: float) -> None:
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.__booked_seats = []

    @property
    def booked_seats(self) -> list:
        return self.__booked_seats.copy()
    
    @property
    def available_seats(self) -> int:
        return self.total_seats - len(self.__booked_seats) 
    
    @property
    def income(self) -> float:
        return len(self.__booked_seats) * self.ticket_price
    
    def book_seat(self, seat_number: int) -> None:
        if seat_number < 1 or seat_number > self.total_seats:
            print("Такого місця не уснує.")
            return
        if seat_number in self.__booked_seats:
            print("Це місце заброньовано. Оберіть інше.")
            return
        self.__booked_seats.append(seat_number)
        print("Місце заброньовано!")
    
    def cancel_booking(self, seat_number: int) -> None:
        if seat_number < 1 or seat_number > self.total_seats:
            print("Такого місця не уснує.")
            return
        if seat_number not in self.__booked_seats:
            print("Неможливо скасувати. Місце не було заброньовано.")
            return
        self.__booked_seats.remove(seat_number)
        print("Успішне скасування!")
        
    def show_hall_info(self) -> None:
        print(f"Фільм: {self.movie_title}")
        print(f"Загальна кількість місць: {self.total_seats}")
        print(f"Кількість заброньованих місць: {len(self.booked_seats)}")
        print(f"Кількість вільних місць: {self.available_seats}")
        print(f"Поточний дохід від продажу квитків: {self.income}")


def program_menu() -> None:
    print("\n1.Забронювати місце")
    print("2.Скасувати бронь")     
    print("3.Загальна информація про зал")     
    print("4.Вихід")     

def main() -> None:
    hall = CinemaHall("Жахливий 1", 70, 200.0)
    print("Вітаємо в кінотеатрі!")
    print("Наразі в прокаті фільм 'Жахливий 1'. \nКількість місць у залі: 70 \nЦіна: 200 грн")
    while True:
        program_menu()
        choice= input("Що ви хочете зробити?").lower()
        if choice in ('1', "забронювати місце"):
            seat_number = int(input("Яке місце бажаєте забронювати? "))
            hall.book_seat(seat_number)
        elif choice in ('2', "скасувати бронь"):
            seat_number = int(input("Бронь якого місця ви бажаєте скасувати? "))
            hall.cancel_booking(seat_number)
        elif choice in ('3', "загальна інформація про зал"):
            hall.show_hall_info()
        elif choice in ('4', "вихід"):
            break
        else:
            print("Такого пункта меню не існує.")

main()
