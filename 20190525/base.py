class BaseTPshop():

    def get_verify(self,session):
        respouse=session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        return respouse

    def login1(self,session,mydata):
        respouse=session.post("http://localhost/index.php?m=Home&c=User&a=do_login",data=mydata)
        return respouse

    def order(self,session):
        respouse = session.get("http://localhost/Home/Order/order_list.html")
        return respouse
