from app.models import (
    Author,
    Articles,
)

from faker import Faker
Faker.seed(10)
fake = Faker('ru_RU')

authors_list = []

for _ in range(25):
    
    full_name = fake.name().split()

    author = Author(
            login=fake.user_name(),
            password=fake.password(length=20),
            email=fake.email(),
            lastname=full_name[0],
            name=full_name[1],
            surname=full_name[2],
            postal_address=fake.address(),
            articles=[Articles(article_heading=fake.text(max_nb_chars=20),article_body=fake.text(max_nb_chars=1000)),
                      Articles(article_heading=fake.text(max_nb_chars=20),article_body=fake.text(max_nb_chars=1000)),
                            ]
            )
    


    authors_list.append(author)

if __name__=='__main__':
    print(authors_list)