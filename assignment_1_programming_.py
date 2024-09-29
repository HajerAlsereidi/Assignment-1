# -*- coding: utf-8 -*-
"""Assignment 1 programming .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a1QlPyhShzFxA0Y40NbISSh2vZAubGA0
"""

# Class to represent a reservation
class Reservation:
    def __init__(self, reservation_id, room_type, check_in_date, check_out_date, num_nights, room_cost):
        self.reservation_id = reservation_id
        self.room_type = room_type
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_nights = num_nights
        self.room_cost = room_cost
        self.is_canceled = False
        self.is_checked_in = False

    # Reservation ID
    def get_reservation_id(self):
        return self.reservation_id

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    # Room type
    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    # Check-in date
    def get_check_in_date(self):
        return self.check_in_date

    def set_check_in_date(self, check_in_date):
        self.check_in_date = check_in_date

    # Check-out date
    def get_check_out_date(self):
        return self.check_out_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    # Number of nights
    def get_num_nights(self):
        return self.num_nights

    def set_num_nights(self, num_nights):
        self.num_nights = num_nights

    # Room cost
    def get_room_cost(self):
        return self.room_cost

    def set_room_cost(self, room_cost):
        self.room_cost = room_cost

    # Is canceled
    def get_is_canceled(self):
        return self.is_canceled

    def set_is_canceled(self, is_canceled):
        self.is_canceled = is_canceled

    # Is checked in
    def get_is_checked_in(self):
        return self.is_checked_in

    def set_is_checked_in(self, is_checked_in):
        self.is_checked_in = is_checked_in

    # Modify method
    def modify(self, new_room_type=None, new_check_in_date=None, new_check_out_date=None, new_num_nights=None, new_room_cost=None):
        if new_room_type is not None:
            self.room_type = new_room_type
        if new_check_in_date is not None:
            self.check_in_date = new_check_in_date
        if new_check_out_date is not None:
            self.check_out_date = new_check_out_date
        if new_num_nights is not None:
            self.num_nights = new_num_nights
        if new_room_cost is not None:
            self.room_cost = new_room_cost
        print("Reservation", self.reservation_id, "has been modified.")

    # Cancel method
    def cancel(self):
        self.is_canceled = True
        print("Reservation", self.reservation_id, "has been canceled.")

    # Calculate cost method
    def calculate_cost(self):
        return self.room_cost * self.num_nights


# Class to represent a hotel guest
class Guest:
    def __init__(self, name, email, phone, billing_name, credit_card):
        self.name = name
        self.email = email
        self.phone = phone
        self.billing_name = billing_name
        self.credit_card = credit_card
        self.reservation_list = []
        self.invoice = None

    # Name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    # Phone
    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    # Billing name
    def get_billing_name(self):
        return self.billing_name

    def set_billing_name(self, billing_name):
        self.billing_name = billing_name

    # Credit card
    def get_credit_card(self):
        return self.credit_card

    def set_credit_card(self, credit_card):
        self.credit_card = credit_card

    # Reservation list
    def get_reservation_list(self):
        return self.reservation_list

    def set_reservation_list(self, reservation_list):
        self.reservation_list = reservation_list

    # Invoice
    def get_invoice(self):
        return self.invoice

    def set_invoice(self, invoice):
        self.invoice = invoice

    # Add reservation method
    def add_reservation(self, reservation):
        self.reservation_list.append(reservation)

    # Generate invoice method
    def generate_invoice(self, invoice):
        self.invoice = invoice

    # Check-in method
    def check_in(self, reservation_id):
        for reservation in self.reservation_list:
            if reservation.reservation_id == reservation_id:
                if reservation.is_canceled:
                    print("Cannot check in. Reservation", reservation_id, "is canceled.")
                else:
                    reservation.is_checked_in = True
                    print("Guest", self.name, "has checked in for reservation", reservation_id)
                return
        print("No reservation found with ID", reservation_id)

    # Check-out method
    def check_out(self, reservation_id):
        for reservation in self.reservation_list:
            if reservation.reservation_id == reservation_id:
                if reservation.is_checked_in:
                    reservation.is_checked_in = False
                    print("Guest", self.name, "has checked out for reservation", reservation_id)
                else:
                    print("Guest", self.name, "has not checked in yet for reservation", reservation_id)
                return
        print("No reservation found with ID", reservation_id)


# Class to represent a hotel room
class Room:
    def __init__(self, room_number, room_type, is_available, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = is_available
        self.price_per_night = price_per_night

    # Room number
    def get_room_number(self):
        return self.room_number

    def set_room_number(self, room_number):
        self.room_number = room_number

    # Room type
    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    # Is available
    def get_is_available(self):
        return self.is_available

    def set_is_available(self, is_available):
        self.is_available = is_available

    # Price per night
    def get_price_per_night(self):
        return self.price_per_night

    def set_price_per_night(self, price_per_night):
        self.price_per_night = price_per_night

    # Check availability method
    def check_availability(self):
        return self.is_available

    # Assign room method
    def assign_room(self):
        self.is_available = False


# Class to represent an invoice
class Invoice:
    def __init__(self, invoice_id, confirmation_number, guest_name, guest_email, guest_billing_name, room_subtotal, taxes_fees, total_cost, credit_card_last_digits):
        self.invoice_id = invoice_id
        self.confirmation_number = confirmation_number
        self.guest_name = guest_name
        self.guest_email = guest_email
        self.guest_billing_name = guest_billing_name
        self.room_subtotal = room_subtotal
        self.taxes_fees = taxes_fees
        self.total_cost = total_cost
        self.credit_card_last_digits = credit_card_last_digits

    # Invoice ID
    def get_invoice_id(self):
        return self.invoice_id

    def set_invoice_id(self, invoice_id):
        self.invoice_id = invoice_id

# Confirmation number
    def get_confirmation_number(self):
        return self.confirmation_number

    def set_confirmation_number(self, confirmation_number):
        self.confirmation_number = confirmation_number

    # Guest name
    def get_guest_name(self):
        return self.guest_name

    def set_guest_name(self, guest_name):
        self.guest_name = guest_name

        # Guest email
    def get_guest_email(self):
        return self.guest_email

    def set_guest_email(self, guest_email):
        self.guest_email = guest_email

# Guest billing name
    def get_guest_billing_name(self):
        return self.guest_billing_name

    def set_guest_billing_name(self, guest_billing_name):
        self.guest_billing_name = guest_billing_name

    # Room subtotal
    def get_room_subtotal(self):
        return self.room_subtotal

    def set_room_subtotal(self, room_subtotal):
        self.room_subtotal = room_subtotal

    # Taxes and fees
    def get_taxes_fees(self):
        return self.taxes_fees

    def set_taxes_fees(self, taxes_fees):
        self.taxes_fees = taxes_fees

    # Total cost
    def get_total_cost(self):
        return self.total_cost

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    # Credit card last digits
    def get_credit_card_last_digits(self):
        return self.credit_card_last_digits

    def set_credit_card_last_digits(self, credit_card_last_digits):
        self.credit_card_last_digits = credit_card_last_digits

    # Calculate total method
    def calculate_total(self):
        self.total_cost = self.room_subtotal + self.taxes_fees
        return self.total_cost

    # Display invoice method
    def display_invoice(self, reservation):
        print("---------------------------------------------------------------------------------")
        print("Your Reservation Is Confirmed")
        print("Thank you for your reservation. Please print your hotel receipt and show it at check-in")
        print("Your Name:", self.guest_name)
        print("Your Email:", self.guest_email())
        print("Priceline Trip Number:", self.invoice_id)
        print("Hotel Confirmation Number:", self.confirmation_number)
        print("-------------------------------------------------------------------------------------------------")
        print("Comfort Inn & Suites Los Alamos")
        print("2455 Trinity Drive", " Check-In:", reservation.check_in_date)
        print("Los Alamos, NM", " Check-Out:", reservation.check_out_date)
        print("87544", " Number of Nights:", str(reservation.num_nights))
        print("Phone: 505-661-1110", " Number of Rooms:", str(1))
        print("-------------------------------------------------------------------------------------------------")
        print("Room 1:", self.guest_name)
        print("-------------------------------------------------------------------------------------------------")
        print("Room Type:", reservation.room_type)
        print("-------------------------------------------------------------------------------------------------")
        print("Summary of Charges")
        print("Billing Name:", self.guest_billing_name())
        print("Credit Card: Mastercard (ending in", self.credit_card_last_digits, ")")
        print("Room Cost: $", str(reservation.room_cost), "avg per room per night")
        print("Rooms:", str(1))
        print("Nights:", str(reservation.num_nights))
        print("Room Subtotal: $", str(round(self.room_subtotal, 2)))
        print("Taxes and Fees: $", str(round(self.taxes_fees, 2)))
        print("Total Charges: $", str(round(self.total_cost, 2)))
        print("Prices are in US dollars")
        print("-------------------------------------------------------------------------------------------------")


#Objects

# Guest 1: Everything works and available
reservation1 = Reservation("52523687", "2 Queen Beds/No Smoking Desk/Safe/Coffee Maker in Room/Hair Dryer", "Sun, Aug 22, 2010 - 03:00 PM", "Tue, Aug 24, 2010 - 12:00 PM", 2, 89.95)
guest1 = Guest("Ted Vera", "tedvera@mac.com", "555-1234", "Ted H Vera", "5504")
guest1.add_reservation(reservation1)

room1 = Room(101, "2 Queen Beds/No Smoking Desk/Safe/Coffee Maker in Room/Hair Dryer", True, 89.95)

# Calculate the room subtotal and generate the invoice
room_subtotal1 = reservation1.calculate_cost()
taxes_fees1 = 21.58
invoice1 = Invoice("15541850358", "52523687", guest1.get_name(), guest1.get_email, guest1.get_billing_name, room_subtotal1, taxes_fees1, 0.0, "5509")
invoice1.calculate_total()
guest1.generate_invoice(invoice1)

# Guest 2: Wants to modify their reservation
reservation2 = Reservation("222222", "2 Queen Beds", "2024-12-10", "2024-12-12", 2, 120.00)
guest2 = Guest("Maryam Fahad", "Maryam@gmail.com", "555-5678", "Maryam Fahad", "5678")
guest2.add_reservation(reservation2)

room2 = Room(102, "2 Queen Beds", True, 120.00)

# Modify the reservation before generating the invoice
reservation2.modify(new_room_type="1 King Bed", new_check_out_date="2024-12-13", new_num_nights=3, new_room_cost=140.00)

# Calculate the room subtotal and generate the invoice
room_subtotal2 = reservation2.calculate_cost()
taxes_fees2 = 25.00
invoice2 = Invoice("INV002", "52284627", guest2.get_name(), guest2.get_email, guest2.get_billing_name, room_subtotal2, taxes_fees2, 0.0, "5678")
invoice2.calculate_total()
guest2.generate_invoice(invoice2)

# Guest 3: Wants to cancel their reservation
reservation3 = Reservation("333333", "Suite", "2024-12-20", "2024-12-25", 5, 200.00)
guest3 = Guest("Mohammed Ahmed", "Mohammed@gmail.com", "555-9876", "Mohammed Ahmed", "9876")
guest3.add_reservation(reservation3)

room3 = Room(103, "Suite", True, 200.00)

# Cancel the reservation before generating the invoice
reservation3.cancel()

# Calculate the room subtotal and generate the invoice (will show cancellation status)
room_subtotal3 = reservation3.calculate_cost()
taxes_fees3 = 50.00
invoice3 = Invoice("INV003", "538264", guest3.get_name(), guest3.get_email, guest3.get_billing_name, room_subtotal3, taxes_fees3, 0.0, "9876")
invoice3.calculate_total()
guest3.generate_invoice(invoice3)

# Displaying invoices for each guest
print("   ")  # Three spaces between invoices
print("   ")
print("   ")
print("Guest 1's Invoice:")
invoice1.display_invoice(reservation1)
print("   ")  # Three spaces between invoices
print("   ")
print("   ")
print("Guest 2's Invoice (after modification):")
invoice2.display_invoice(reservation2)
print("   ")  # Three spaces between invoices
print("   ")
print("   ")
print("Guest 3's Invoice (canceled reservation):")
invoice3.display_invoice(reservation3)

# Showing the modification and cancellation actions at the end
print("   ")  # Three spaces before final status updates
print("   ")
print("   ")
print("--- Final Status Updates ---")

# Modify and display guest 2's reservation modification
print("Guest 2's Reservation Modified:")
reservation2.modify(new_room_type="Suite", new_num_nights=4)
invoice2.display_invoice(reservation2)
print("   ")  # Three spaces between modifications
print("   ")
print("   ")

# Cancel and display guest 3's reservation cancellation
print("Guest 3's Reservation Canceled:")
reservation3.cancel()
invoice3.display_invoice(reservation3)