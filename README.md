# datagenerator-python
Datagenerator module for Python

Use it to make some data

```
from collections import namedtuple
from datagenerator import Datagenerator as dg
from datagenerator import Case

Person = namedtuple('Person', ['first_name', 'last_name', 'street', 'city', 'state', 'zipcode'])
addresses = []
for _ in range(20):
    person = Person(first_name=dg.first_name(),last_name=dg.last_name(),
          street="%d %s %s" % (dg.numeric(4), dg.street_name(), dg.street_type()), city=dg.city(), state=dg.state(), zipcode=dg.numeric(5))
    addresses.append(person)

print(addresses)

# output is similar to the following

[Person(first_name='David', last_name='Prince', street='1104 Maple Dr.', city='Jamestown', state='CN', zipcode='47121'), 
... 
Person(first_name='Michael', last_name='Everson', street='6346 Maple Dr.', city='Hell', state='OH', zipcode='843105')]

```

