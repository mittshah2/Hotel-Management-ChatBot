## booking_good_path
* greet
  - utter_greet
  - utter_how_can_i_help
* book_room
  - utter_no_of_rooms
* number_of_rooms
  - utter_room_type
  - action_booking_confirm
* thanks
  -utter_welcome

## booking_path1
* greet
  - utter_greet
  - utter_how_can_i_help
* book_room{"room_count"="2"}
  - utter_room_type
  - action_booking_confirm  
* thanks
  -utter_welcome

## booking_path2
* greet
  - utter_greet
  - utter_how_can_i_help
* book_room{"room_count"="2","room_type"="Simple"}
  - action_booking_confirm  
* thanks
  -utter_welcome

## booking_path3
* greet
  - utter_greet
  - utter_how_can_i_help
* book_room{"room_type"="Simple"}
  - utter_no_of_rooms
  - action_booking_confirm  
* thanks
  -utter_welcome

## booking_path4
* greet
  - utter_greet
  - utter_how_can_i_help
* book_room
  - utter_no_of_rooms
* number_of_rooms{"room_type"="Simple"}
  - action_booking_confirm
* thanks
  -utter_welcome





## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
