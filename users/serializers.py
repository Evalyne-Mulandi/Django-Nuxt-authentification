from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class meta:
        model= User
        fields=['id','first_name','last_name','email','password']
        extra_kwargs={
            'password':{'write_only':True}

        }

        def create(self, validated_data):
            password= validated_data['password']
            instance= self.Meta.model(**validated_data)
            
            if password is not None:
                instance.set_password(password)
                instance.save()

            return instance    
