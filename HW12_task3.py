# 3. Создайте класс который будет хранить параметры для подключения к физическому юниту(например switch).
# В своем списке атрибутов он должен иметь минимальный набор (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и сеттеров(@property).
# У вас должна быть возможность получения и назначения этих атрибутов в классе.


class Save:
    unit_name = None
    mac_address = None
    ip_address = None
    login = None
    password = None

    def get_unit_name(self):
        print('unit_name getter method called')
        return self.unit_name

    def set_unit_name(self, a):
        print('unit_name setter method called')
        self.unit_name = a

    def get_mac_address(self):
        print('mac_address getter method called')
        return self.mac_address

    def set_mac_address(self, a):
        print('mac_address setter method called')
        self.mac_address = a

    def get_ip_address(self):
        print('ip_address getter method called')
        return self.ip_address

    def set_ip_address(self, a):
        print('ip_address setter method called')
        self.ip_address = a

    def get_login(self):
        print('login getter method called')
        return self.login

    def set_login(self, a):
        print('login setter method called')
        self.login = a

    def get_password(self):
        print('password getter method called')
        return self.password

    def set_password(self, a):
        print('password setter method called')
        self.password = a

    property_unit_name = property(get_unit_name, set_unit_name)
    property_mac_address = property(get_mac_address, set_mac_address)
    property_ip_address = property(get_ip_address, set_ip_address)
    property_login = property(get_login, set_login)
    property_password = property(get_password, set_password)
    

class f(Save):
    s = Save
    s.property_unit_name = 'a unit'
    s.property_mac_address = '12312313'
    s.property_ip_address = '192.2312313'
    s.property_login = 'schnittke'
    s.property_password = 'F1298JHsf0_45'

    print(s.property_unit_name, s.property_mac_address, s.property_ip_address,
          s.property_login, s.property_password, sep='\n')
