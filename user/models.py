import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="user_id")    # user 식별하는 ID값
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=255, verbose_name="이름")
    nickname = models.CharField(max_length=255, verbose_name="닉네임")
    password = models.CharField(max_length=255, verbose_name="비밀번호")
    user_phone_number = models.CharField(max_length=255, verbose_name="전화번호")
    car_or_bike = models.BooleanField(default=False, verbose_name="보유 차량")
    is_active = models.BooleanField(default=True)   # 가입 하는 순가 기본값 True = 활동중
    is_staff = models.BooleanField(default=False)   # 가입 하는 처음에는 기본적으로 관리자 권한 X
    is_superuser = models.BooleanField(default=False) # staff 권한과 동일

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def get_full_name(self):
        return self.user_id

class Company(models.Model):
    COMPANY_CHOICES = (
        ("Boss", "Boss"),
        ("Employee", "Employee"),
    )


class Repair_Shop(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="user_id")    # user 식별하는 ID값
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=255, verbose_name="이름")
    password = models.CharField(max_length=255, verbose_name="비밀번호")
    user_phone_number = models.CharField(max_length=255, verbose_name="전화번호")
    shop_name = models.CharField(max_length=255, verbose_name="Shop 이름")
    spot_name = models.CharField(max_length=20, verbose_name="지점 이름")
    car_or_bike = models.BooleanField(default=False, verbose_name="수리하는 차량(종류)")
    company = models.CharField(choices=Company, max_length="20", verbose_name="직급")
    is_active = models.BooleanField(default=True)   # 가입 하는 순가 기본값 True = 활동중
    is_staff = models.BooleanField(default=False)   # 가입 하는 처음에는 기본적으로 관리자 권한 X
    is_superuser = models.BooleanField(default=False) # staff 권한과 동일


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def get_full_name(self):
        return self.user_id

class Online_Shop(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="user_id")    # user 식별하는 ID값
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=255, verbose_name="이름")
    password = models.CharField(max_length=255, verbose_name="비밀번호")
    user_phone_number = models.CharField(max_length=255, verbose_name="전화번호")
    shop_name = models.CharField(max_length=255, verbose_name="Shop 이름")
    company = models.CharField(choices=Company, max_length="20",  verbose_name="직급")
    is_active = models.BooleanField(default=True)   # 가입 하는 순가 기본값 True = 활동중
    is_staff = models.BooleanField(default=False)   # 가입 하는 처음에는 기본적으로 관리자 권한 X
    is_superuser = models.BooleanField(default=False) # staff 권한과 동일

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def get_full_name(self):
        return self.user_id


class Businesses(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="user_id")
    b_no = models.IntegerField(verbose_name="사업자 등록번호")
    stat_dt = models.DateField(verbose_name="사업일자")
    p_nm = models.CharField(verbose_name="대표자 성명")
    b_nm = models.CharField(verbose_name="상호명")

# 차량 정보에데한 DB Model은 Open API 찾아보고 넣어야함
#  필수로 들어가야하는 기능
# class Car_Or_Bike(models.Model):
#     Car_Or_Bike_CHOICES = (
#         ("Car", "Car"),
#         ("Bike", "Bike"),
#     )
#     car_or_bike = models.CharField(choices=Car_Or_Bike_CHOICES, max_length=20)
#