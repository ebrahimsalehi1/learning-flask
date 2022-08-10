from app2 import db,User,Gender,UserType

try:
    db.session.query(Gender).delete()
    db.session.add(Gender(gender_id='F',gender_title='Female'))
    db.session.add(Gender(gender_id='M',gender_title='Male'))
    db.session.commit()
except Exception as ex:
    print(ex)


try:
    db.session.query(UserType).delete()
    db.session.add(UserType(id='TE',title='Teacher'))
    db.session.add(UserType(id='ST',title='Student'))
    db.session.add(UserType(id='GEN',title='General'))
    db.session.add(UserType(id='ADMIN',title='Admin'))
    db.session.add(UserType(id='EMP',title='Employee'))

    db.session.commit()
except Exception as ex:
    print(ex)


try:
    db.session.query(User).delete()

    db.session.add(User(user_name='ebrahim01',password='1234',first_name='Ebrahim',last_name='Salehi',user_type='Teacher',gender_id='M'))
    db.session.add(User(user_name='mahsa02',password='5678',first_name='Mahsa',last_name='Hakamiha',user_type='Student',gender_id='F'))
    db.session.add(User(user_name='anisa03',password='5678',first_name='Anisa',last_name='Hakamiha',user_type='Student',gender_id='F'))
    db.session.add(User(user_name='maryam04',password='5678',first_name='Maryam',last_name='Maryami',user_type='Student',gender_id='F'))
    
    db.session.commit()
except Exception as ex:
    print(ex)

