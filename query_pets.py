import sqlite3

conn=sqlite3.connect("pets.db")
cur=conn.cursor()

def main():
     while True:
         person_id = input("'Please enter person's ID number: '")
         if person_id == '-1':
             print ('Exiting the program')
             exit()
         elif person_id == '0':
             print ('Invalid ID number')
             continue
              
         cur.execute("SELECT first_name, last_name, person.age, name, breed,"
                     "pet.age, dead FROM person, pet, person_pet "
                     "WHERE person.id = person_pet.person_id AND "
                     "pet.id = person_pet.pet_id AND person.id=(?)", (person_id))

         person = cur.fetchall()
         for row in person:
             first_name = row[0]
             last_name = row[1]
             age = row[2]
             pet_name = row[3]
             pet_breed = row[4]
             pet_age = row[5]
             pet_dead = row[6]
             if pet_dead == 1:
                 print ("{} {} is {} years old.").format(first_name, last_name, age)
                 print ("{} {} owned {}, a {}, that was {} years old.").format(first_name, last_name, pet_name, pet_breed, pet_age)
             else:
                 print ("{} {} is {} years old.").format(first_name, last_name, age)
                 print ("{} {} owns {}, a {}, that is {} years old.").format(first_name, last_name, pet_name, pet_breed, pet_age)
               
if __name__ == "__main__":
    main()
