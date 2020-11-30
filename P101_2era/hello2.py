def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)



# I did this one as a project earlier
