from User import User
persona1=User("henry","torres")
persona2=User("samuel","zapata")
persona3=User("pedro","sanchez")

# print("********** Persona 1 **********")
# persona1.make_deposit(30)
# persona1.make_deposit(300)
# persona1.make_deposit(3000)
# persona1.make_withdraw(2000)
# persona1.display_user_balance()
persona1.make_deposit(30).make_deposit(300).make_deposit(3000).make_withdraw(2000).display_user_balance()

# print("********** Persona 2 **********")
# persona2.make_deposit(300)
# persona2.make_deposit(2000)
# persona2.make_withdraw(200)
# persona2.make_withdraw(500)
# persona2.display_user_balance()
persona2.make_deposit(300).make_deposit(2000).make_withdraw(200).make_withdraw(500).display_user_balance()

# print("********** Persona 3 **********")
# persona3.make_deposit(1000)
# persona3.make_withdraw(200)
# persona3.make_withdraw(100)
# persona3.make_withdraw(300)
# persona3.display_user_balance()
persona3.make_deposit(1000).make_withdraw(200).make_withdraw(100).make_withdraw(300).display_user_balance()

# print("********** transfer dinero persona 2 to persona 3 **********")
# persona2.transfer_dinero(persona3,600)

