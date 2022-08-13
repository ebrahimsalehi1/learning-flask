from app2 import db,User,Gender,Usertype

try:
    db.session.query(Gender).delete()
    db.session.add(Gender(title='Female'))
    db.session.add(Gender(title='Male'))
    db.session.commit()
except Exception as ex:
    print(ex)
    db.session.rollback()

try:
    db.session.query(Usertype).delete()
    db.session.add(Usertype(title='Teacher'))
    db.session.add(Usertype(title='Student'))
    db.session.add(Usertype(title='General'))
    db.session.add(Usertype(title='Admin'))
    db.session.add(Usertype(title='Employee'))

    db.session.commit()
except Exception as ex:
    print(ex)
    db.session.rollback()


try:
    db.session.query(User).delete()

    db.session.add(User(user_name='ebrahim01',password='1234',first_name='Ebrahim',last_name='Salehi',usertype_id=1,gender_id=2))
    db.session.add(User(user_name='mahsa02',password='5678',first_name='Mahsa',last_name='Hakamiha',usertype_id=2,gender_id=1))
    db.session.add(User(user_name='anisa03',password='5678',first_name='Anisa',last_name='Hakamiha',usertype_id=2,gender_id=1))
    db.session.add(User(user_name='maryam04',password='5678',first_name='Maryam',last_name='Maryami',usertype_id=2,gender_id=1))
    
    db.session.commit()
except Exception as ex:
    print(ex)
    db.session.rollback()

