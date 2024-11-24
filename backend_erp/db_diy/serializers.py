from rest_framework import serializers
from .models import Role, Entity, RolePermission, Employees
from rest_framework import serializers
from .models import Clients
from supplier.models import BankingDetail

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ['entity_id', 'entity_name']

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ['role_id', 'role_name', 'description']

class RolePermissionSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = RolePermission
        fields = ['entity', 'role', 'view', 'create', 'edit', 'delete', 'full_access']

    def create(self, validated_data):
        role_data = validated_data.pop('role')
        role = Role.objects.get(role_id=role_data['role_id']) 

      
        role_permission = RolePermission.objects.create(
            role=role,
            entity=validated_data['entity'],
            view=validated_data.get('view', False),
            create=validated_data.get('create', False),
            edit=validated_data.get('edit', False),
            delete=validated_data.get('delete', False),
            full_access=validated_data.get('full_access', False),
        )
        return role_permission

    def update(self, instance, validated_data):
        role_data = validated_data.pop('role') 
        role = Role.objects.get(role_id=role_data['role_id'])

        instance.role = role
        instance.entity = validated_data.get('entity', instance.entity)
        instance.view = validated_data.get('view', instance.view)
        instance.create = validated_data.get('create', instance.create)
        instance.edit = validated_data.get('edit', instance.edit)
        instance.delete = validated_data.get('delete', instance.delete)
        instance.full_access = validated_data.get('full_access', instance.full_access)

        instance.save()
        return instance

    

class EmployeesSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = Employees
        fields = ['id', 'username', 'password', 'name', 'birth', 'email', 'tel', 'address', 'gender', 'role']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }

    def create(self, validated_data):
    
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()  
        return instance

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
from rest_framework import serializers
from .models import Clients, Role  # Import đúng mô hình và Role
from supplier.models import BankingDetail  # Import BankingDetail nếu cần

class ClientsSerializer(serializers.ModelSerializer):
    bank_account = serializers.PrimaryKeyRelatedField(queryset=BankingDetail.objects.all(), allow_null=True)  # Liên kết với BankingDetail

    class Meta:
        model = Clients 
        fields = ['id', 'username', 'password', 'name', 'birth', 'email', 'tel', 'address', 'gender', 'bank_account', 'avatar', 'isDelete', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
      
        password = validated_data.pop('password', None) 
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password) 
        instance.save()  
        return instance

    def update(self, instance, validated_data):
    
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        instance.save()
        return instance
