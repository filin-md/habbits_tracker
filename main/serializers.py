from rest_framework import serializers

from main.models import Habit
from main.validators import validate_reward_and_linked, validate_length, validate_linked_is_pleasant, \
    validate_reward_if_not_pleasant, validate_period


class HabitSerializer(serializers.ModelSerializer):
    reward = serializers.CharField(max_length=100, validators=[validate_reward_and_linked, validate_reward_if_not_pleasant])
    length = serializers.IntegerField(validators=[validate_length])
    linked = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(),
        validators=[validate_linked_is_pleasant],
        allow_null=True
    )
    period = serializers.IntegerField(validators=[validate_period])


    class Meta:
        model = Habit
        fields = '__all__'
