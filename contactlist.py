# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
 

class ContactBook:

    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self._store()
        print('Contact added')

    def show_all(self):
        if len(self.contacts) == 0:
            print('No contacts stored')
        else:
            for contact in self.contacts:
                self.print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[idx]
                self._store()
                break

    def search(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.print_contact(contact)
                break
        else:
            self.not_found()

    def update(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                contact.name = str(input('Enter new name: '))
                contact.tel = str(input('Enter new phone number: '))
                contact.email = str(input('Enter new email address: '))
                self.contacts[i] = contact
                self._store()
                break

        else:
            self.not_found()

    def print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('Telephone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def not_found(self):
        print('*******')
        print('¡Not Found!')
        print('*******')

    def _store(self):
        #Save contacts to file
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self.contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

def create():
    #Create file to store contacts
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))


def run():

    contact_book = ContactBook()
    try:
        with open('contacts.csv','r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                elif row == []:
                    continue
                else:
                    contact_book.add(row[0],row[1],row[2])
    except FileNotFoundError:
        create()
    while True:
        command = str(input('''
            What do you wish to do?

            [a]dd contact
            [u]pdate contact
            [s]earch contact
            [d]elete contact
            [l]ist contacts
            [e]xit
            '''))

        if command == 'a':
            name = str(input('Write contact name: '))
            phone = str(input('Add contact phone number: '))
            email = str(input('Add contact email address: '))

            contact_book.add(name, phone, email)

        elif command == 'u':
            name = str(input('Enter the contact name: '))

            contact_book.update(name)

        elif command == 's':

            name = str(input('Enter the contact name: '))

            contact_book.search(name)

        elif command == 'd':
            name = str(input('Enter the contact name: '))

            contact_book.delete(name)

        elif command == 'l':

            contact_book.show_all()

        elif command == 'e':
            break
        else:
            print('Command not found.')


if __name__ == '__main__':
    print('W E L C O M E  T O  Y O U R  C O N T A C T  L I S T')
    run()