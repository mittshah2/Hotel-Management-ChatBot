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
  - book_form
  - form{"name": "book_form"}
  - form{"name": null}

## booking_path1
* book_room
  - book_form
  - form{"name": "book_form"}
* faq
  - respond_faq
  - book_form
  - form{"name": null}



## cleaning_good_path1
* cleaning_service
  - clean_form
  - form{"name": "clean_form"}
  - form{"name": null}



## cleaning_path1
* cleaning_service
  - clean_form
  - form{"name": "clean_form"}
* faq
  - respond_faq
  - clean_form
  - form{"name": null}



## faq
* faq
  - respond_faq


## say goodbye
* bye
  - utter_bye

## thanks
* thank
  - utter_welcome

## bot challenge
* bot_challenge
  - utter_iamabot
