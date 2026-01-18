# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_customers = []
    for customer in customers:
        list_customers.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    for customer_el in list_customers:
        CinemaBar.sell_product(customer = customer_el.name, product = customer_el.food)
    hall.movie_session(movie_name = movie, customers = list_customers, cleaning_staff= cleaner_staff)
