# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customeremail = models.CharField(db_column='customerEmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customerfirstname = models.CharField(db_column='customerFirstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customerlastname = models.CharField(db_column='customerLastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customercity = models.CharField(db_column='customerCity', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customerstate = models.CharField(db_column='customerState', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='customerAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customerzip = models.CharField(db_column='customerZIP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customerphone = models.CharField(db_column='customerPhone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    store = models.ForeignKey('Store', models.DO_NOTHING, db_column='store_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('id', 'store'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enterprise(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    enterprisename = models.CharField(db_column='enterpriseName', max_length=45)  # Field name made lowercase.
    inventory = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='inventory_ID')  # Field name made lowercase.
    store = models.ForeignKey('Store', models.DO_NOTHING, db_column='store_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enterprise'
        unique_together = (('id', 'inventory', 'store'),)


class Inventory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='product_ID')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING, db_column='store_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'
        unique_together = (('id', 'product', 'store'),)


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productupc = models.IntegerField(db_column='productUPC')  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=45)  # Field name made lowercase.
    productprice = models.FloatField(db_column='productPrice')  # Field name made lowercase.
    producttype = models.CharField(db_column='productType', max_length=45)  # Field name made lowercase.
    productbrand = models.CharField(db_column='productBrand', max_length=45)  # Field name made lowercase.
    productdescription = models.TextField(db_column='productDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Sales(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    store = models.ForeignKey('Store', models.DO_NOTHING, db_column='store_ID')  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_ID')  # Field name made lowercase.
    amountsold = models.IntegerField(db_column='amountSold')  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='totalPrice', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales'
        unique_together = (('id', 'store', 'product'),)


class Store(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=45)  # Field name made lowercase.
    storeaddress = models.CharField(db_column='storeAddress', max_length=45)  # Field name made lowercase.
    storestate = models.CharField(db_column='storeState', max_length=45)  # Field name made lowercase.
    storezip = models.CharField(db_column='storeZIP', max_length=45)  # Field name made lowercase.
    storeopentime = models.CharField(db_column='storeOpenTime', max_length=45)  # Field name made lowercase.
    storeclosetime = models.CharField(db_column='storeCloseTime', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class Vendor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vendorname = models.CharField(db_column='vendorName', max_length=45)  # Field name made lowercase.
    vendoraddress = models.CharField(db_column='vendorAddress', max_length=45)  # Field name made lowercase.
    vendorphone = models.CharField(db_column='vendorPhone', max_length=45)  # Field name made lowercase.
    store = models.ForeignKey(Store, models.DO_NOTHING, db_column='store_ID')  # Field name made lowercase.
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING, db_column='inventory_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendor'
        unique_together = (('id', 'store', 'inventory'),)
