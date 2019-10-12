from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False)
	description = serializers.CharField()
	status = serializers.CharField(required=True)


	def create(self, validated_data):
		return Todo.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.description = validated_data.get('description', instance.description)
		instance.status = validated_data.get('status', instance.status)
		instance.save()
		return instance

