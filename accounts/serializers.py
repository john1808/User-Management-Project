# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Profile

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password"]

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"]
#         )
#         return user

# class ProfileSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(source="user.email", read_only=True)

#     class Meta:
#         model = Profile
#         fields = ["full_name", "dob", "email", "address", "gender", "mobile"]


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password"]

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"]
#         )
#         Profile.objects.create(user=user)
#         return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = ["full_name", "dob", "email", "address", "gender", "mobile"]

    def validate_mobile(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits.")
        if value and len(value) not in [10, 12, 13]:
            raise serializers.ValidationError("Mobile number must be 10–13 digits long.")
        return value


# class ProfileSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(source="user.email", read_only=True)

#     class Meta:
#         model = Profile
#         fields = ["full_name", "dob", "email", "address", "gender", "mobile"]
