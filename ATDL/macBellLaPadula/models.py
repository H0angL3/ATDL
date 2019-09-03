from django.db import models
SECRET_LEVEL = {'Top Secret': 4, 'Secret': 3, 'Confidential': 2, 'Unclassified': 1}
#user table
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 100)
    password = models.CharField(max_length=100)
    def get_secret_classifications(self):
        property = {}
        secret_classifications = Sc_User.objects.filter(user_id=self)
        for sc in secret_classifications:
            property[sc.category] = sc.classification
        return property

    #xax dinh quyen cua user voi object
    def have_read(self, object):
        user_privilege = self.get_secret_classifications()
        user_categories = user_privilege.keys()
        if object.category in user_categories:
            if SECRET_LEVEL[user_privilege[object.category]] >= SECRET_LEVEL[object.classification]:
                return True
        return False

    def have_modify(self):
        user_privilege = self.get_secret_classifications()
        user_categories = user_privilege.keys()
        if object.category in user_categories:
            if SECRET_LEVEL[user_privilege[object.category]] == SECRET_LEVEL[object.classification]:
                return True
        return False
    #xac dinh cac classification user duoc phep viet
    def types_write(self):
        types = {}
        user_privilege = self.get_secret_classifications()
        for cate in user_privilege.keys():
            privilege = []
            for classif, level in SECRET_LEVEL.items():
                if SECRET_LEVEL[user_privilege[cate]] <= level:
                    privilege.append(classif)
            types[cate] = privilege
        return types

    # tim tat ca cac object nguoi dung co the doc
    def all_objects_can_read(self):
        read_list = []
        for obj in Object.objects.all():
            if self.have_read(obj):
                read_list.append(obj)
        return read_list

class Sc_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user')
    category = models.CharField(max_length=100)
    classification = models.CharField(max_length= 100)

class Object(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length= 100)
    title = models.CharField(max_length= 100)
    filename = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)

