room_count = 1
num_of_valid_rooms = 0

while True:
  if bool('5' in str(room_count)) ^ bool('7' in str(room_count)):
    num_of_valid_rooms += 1
    if num_of_valid_rooms == 1000:
      break

  room_count += 1

print('room_number: {}'.format(room_count))
