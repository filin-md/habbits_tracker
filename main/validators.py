from rest_framework.serializers import ValidationError


def validate_reward_and_linked(value):
    if value['reward'] and value['linked']:
        raise ValidationError("Поля 'reward' и 'linked' не могут быть заполнены одновременно.")


def validate_length(value):
    if value > 120:
        raise ValidationError("Значение поля 'length' не должно превышать 120.")


def validate_linked_is_pleasant(value):
    if value and not value.is_pleasant:
        raise ValidationError("Связанный объект должен иметь значение 'is_pleasant' равное True.")


def validate_reward_if_not_pleasant(value):
    if value and not value.is_pleasant:
        raise ValidationError("Поле 'reward' может быть задано только если значение поля 'is_pleasant' равно False.")


def validate_period(value):
    if value > 7:
        raise ValidationError("Значение поля 'period' не должно быть больше 7.")

