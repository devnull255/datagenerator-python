# datagenerator-python
Datagenerator module for Python

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

[Person(first_name='David', last_name='Prince', street='1104 Maple Dr.', city='Jamestown', state='CN', zipcode='47121'), Person(first_name='Patricia', last_name='Williams', street='1465 Pine Dr.', city='Three Oaks', state='TX', zipcode='95270'), Person(first_name='Paul', last_name='Furman', street='9542 Main St.', city='Paradise', state='AL', zipcode='79160'), Person(first_name='Richard', last_name='Anderson', street='61030 Oak Rd.', city='Concepcion', state='CO', zipcode='46901'), Person(first_name='Richard', last_name='Jackson', street='6402 Oak Dr.', city='Paradise', state='LA', zipcode='29981'), Person(first_name='Richard', last_name='Vulcan', street='63310 Maple St.', city='Newville', state='LA', zipcode='341310'), Person(first_name='David', last_name='Furman', street='06108 Pine St.', city='Three Oaks', state='NV', zipcode='103510'), Person(first_name='Madison', last_name='ODoole', street='11103 Main St.', city='Concepcion', state='MT', zipcode='941010'), Person(first_name='Foster', last_name='Xavier', street='6195 Main Rd.', city='Three Oaks', state='MT', zipcode='50860'), Person(first_name='Yvonne', last_name='Lamb', street='6313 Pine Ave.', city='Concepcion', state='LA', zipcode='48035'), Person(first_name='David', last_name='Quayle', street='1978 Main Dr.', city='Hell', state='WA', zipcode='710878'), Person(first_name='Yvonne', last_name='Quayle', street='0195 Oak St.', city='Jamestown', state='SD', zipcode='61874'), Person(first_name='Cheryl', last_name='Martin', street='6307 Pine Dr.', city='Jamestown', state='NJ', zipcode='04116'), Person(first_name='Michael', last_name='Everson', street='6520 Maple Ave.', city='Paradise', state='ID', zipcode='105392'), Person(first_name='David', last_name='Zane', street='109010 Pine St.', city='Hell', state='NE', zipcode='70681'), Person(first_name='Joseph', last_name='Smith', street='3174 Oak Ave.', city='Hell', state='SC', zipcode='102459'), Person(first_name='Paul', last_name='Vulcan', street='104108 Oak Rd.', city='Newville', state='CO', zipcode='310548'), Person(first_name='Patricia', last_name='Martin', street='4317 Pine Rd.', city='Paradise', state='UT', zipcode='77415'), Person(first_name='Keegan', last_name='Haynes', street='2525 Main Ave.', city='Three Oaks', state='ID', zipcode='44616'), Person(first_name='Michael', last_name='Everson', street='6346 Maple Dr.', city='Hell', state='OH', zipcode='843105')]



