snowballs = int(input())

snowball_weight_record = -1
snowball_time_record = 0
snowball_quality_record = -1
snowball_value_record = -1

for snowball in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > snowball_value_record:
        snowball_weight_record = snowball_weight
        snowball_time_record = snowball_time
        snowball_quality_record = snowball_quality
        snowball_value_record = snowball_value

else:
    print(f"{snowball_weight_record} : {snowball_time_record} = {int(snowball_value_record)} ({snowball_quality_record})")