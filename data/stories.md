## affirm
* affirm
  - utter_pleased

## deny
* deny
 - utter_sorry

## greeting
* greet
  - utter_greet
  - utter_how_can_i_help

## booking_good_path
* book_room
  - utter_no_of_rooms
* number_of_rooms
  - utter_room_type
* type_of_room
  - utter_booking_confirm
  - utter_did_that_help



## booking_path1
* book_room{"room_count":"2"}
  - utter_room_type
* type_of_room
  - utter_booking_confirm  
  - utter_did_that_help


## booking_path2
* book_room{"room_count":"2","room_type":"Simple"}
  - utter_booking_confirm
  - utter_did_that_help


## booking_path3
* book_room{"room_type":"Simple"}
  - utter_no_of_rooms
* number_of_rooms
  - utter_booking_confirm
  - utter_did_that_help


## booking_path4
* book_room
  - utter_no_of_rooms
* number_of_rooms{"room_type":"Simple"}
  - utter_booking_confirm
  - utter_did_that_help


## cleaning_good_path
* cleaning_service
  - utter_after_how_much_time
* when_to_clean{"time_type":"right now"}
  - action_clean_confirm

## cleaning_good_path1
* cleaning_service
  - utter_after_how_much_time
* when_to_clean{"time_type":"hours","time_value":"2"}
  - action_clean_confirm

## cleaning_path1
* cleaning_service{"time_type":"hours","time_value":"2"}
  - action_clean_confirm

## cleaning_path1
* cleaning_service{"time_type":"right now"}
  - action_clean_confirm
  


## say goodbye
* bye
  - utter_bye

## thanks
* thank
  - utter_welcome

## bot challenge
* bot_challenge
  - utter_iamabot
